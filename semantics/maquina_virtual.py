"""
Maquina Virtual de BabyDuck.

Ejecuta la fila de cuadruplos usando direcciones virtuales.

Memoria de ejecucion
--------------------
    MemoriaEjecucion
    ├── globales    Segmento (int / float / bool)       vive todo el programa
    ├── constantes  dict direccion -> valor             solo lectura
    └── pila de RegistroActivacion (main, f, g, ...)
            ├── locales     Segmento (int / float / bool)
            ├── temporales  Segmento (int / float / bool)
            └── ip_regreso  cuadruplo al que se vuelve tras ENDFUNC/RETURN

Un Segmento tiene un arreglo por tipo, del tamano exacto que calculo el
compilador (funcion.tamano). Una direccion se traduce asi:

    direccion virtual -> (segmento, tipo, desplazamiento)
    5002              -> ("local", "float", 2)  -> frame.locales["float"][2]

Las direcciones locales y temporales se interpretan siempre en el registro de
activacion que esta en el tope de la pila (la funcion que se esta ejecutando).

Estructuras auxiliares:
    pila_registros:   registros de activacion activos (main en el fondo).
    registros_nuevos: registros creados por ERA que aun esperan su GOSUB
                      (es pila porque puede haber llamadas dentro de argumentos:
                      f(g(1))).
    ip:               apuntador al cuadruplo actual (0-based).
"""
from .memoria_virtual import MemoriaVirtual


LIMITE_LLAMADAS = 1000       # profundidad maxima de la pila (recursion infinita)
VALOR_INICIAL = None         # una celda sin asignar se marca con None


class ErrorEjecucion(Exception):
    pass


def convertir(tipo, valor):
    """Ajusta un valor al tipo de la celda donde se va a guardar."""
    if tipo == "int":
        return int(valor)
    if tipo == "float":
        return float(valor)
    if tipo == "bool":
        return bool(valor)
    return valor


class Segmento:
    """Bloque de memoria con un arreglo por tipo (int, float, bool)."""

    def __init__(self, nombre, tamanos):
        self.nombre = nombre                     # "global", "local" o "temporal"
        # Un arreglo por tipo, del tamano que calculo el compilador
        self.bloques = {
            tipo: [VALOR_INICIAL] * tamanos.get(tipo, 0)
            for tipo in ("int", "float", "bool")
        }

    def _celda(self, direccion):
        segmento, tipo, desplazamiento = MemoriaVirtual.decodificar(direccion)
        if segmento != self.nombre:
            raise ErrorEjecucion(f"La direccion {direccion} no pertenece al segmento {self.nombre}")
        bloque = self.bloques[tipo]
        if desplazamiento >= len(bloque):
            raise ErrorEjecucion(
                f"Direccion {direccion} fuera del espacio reservado ({self.nombre} {tipo}: {len(bloque)})"
            )
        return tipo, bloque, desplazamiento

    def leer(self, direccion):
        _, bloque, desplazamiento = self._celda(direccion)
        valor = bloque[desplazamiento]
        if valor is VALOR_INICIAL:
            raise ErrorEjecucion(f"Variable sin valor asignado (direccion {direccion})")
        return valor

    def escribir(self, direccion, valor):
        tipo, bloque, desplazamiento = self._celda(direccion)
        bloque[desplazamiento] = convertir(tipo, valor)

    def __getitem__(self, direccion):
        return self.leer(direccion)

    def __contains__(self, direccion):
        try:
            _, bloque, desplazamiento = self._celda(direccion)
        except (ErrorEjecucion, ValueError):
            return False
        return bloque[desplazamiento] is not VALOR_INICIAL


class RegistroActivacion:
    """Memoria de UNA llamada a funcion (o de main)."""

    def __init__(self, funcion, nombre, tamano):
        self.funcion = funcion
        self.nombre = nombre
        self.locales = Segmento("local", tamano.get("local", {}))
        self.temporales = Segmento("temporal", tamano.get("temporal", {}))
        self.ip_regreso = None

    def segmento(self, nombre):
        return self.locales if nombre == "local" else self.temporales


class MaquinaVirtual:
    def __init__(self, fila, directorio, entradas=None):
        if not hasattr(fila, "cuadruplos"):
            raise ErrorEjecucion("La fila no contiene cuadruplos")
        if directorio is None:
            raise ErrorEjecucion("La maquina necesita el directorio de funciones")
        self.fila = fila
        self.directorio = directorio
        self.entradas = list(entradas or [])
        self.indice_entrada = 0
        self.salida = []
        self.ip = 0
        self.detener = False

        programa = directorio.obtener_funcion(directorio.nombre_programa)
        tamano = programa.tamano or {}
        self.globales = Segmento("global", tamano.get("global", {}))
        self.constantes = {}
        self._cargar_constantes()
        self.pila_registros = [RegistroActivacion(programa, "main", tamano)]
        self.registros_nuevos = []

    # ---------- Carga inicial ----------
    def _cargar_constantes(self):
        """Llena la tabla de constantes con la que genero el compilador."""
        memoria = self.directorio.memoria
        if memoria is None:
            return
        for (tipo, texto), direccion in memoria.constantes.items():
            if tipo == "string":
                if len(texto) >= 2 and texto[0] == '"' and texto[-1] == '"':
                    texto = texto[1:-1]
                self.constantes[direccion] = texto
            elif tipo == "bool":
                self.constantes[direccion] = texto.lower() in ("true", "1")
            else:
                self.constantes[direccion] = convertir(tipo, texto)

    # ---------- Acceso a memoria ----------
    def registro_activo(self):
        return self.pila_registros[-1]

    def _segmento_de(self, direccion, para_escribir=False):
        if direccion is None:
            raise ErrorEjecucion("Direccion None en un cuadruplo")
        try:
            segmento, _, _ = MemoriaVirtual.decodificar(direccion)
        except ValueError as e:
            raise ErrorEjecucion(str(e))
        if segmento == "constante":
            if para_escribir:
                raise ErrorEjecucion(f"No se puede escribir en memoria constante: {direccion}")
            return None
        if segmento == "global":
            return self.globales
        return self.registro_activo().segmento(segmento)

    def leer(self, direccion):
        segmento = self._segmento_de(direccion)
        if segmento is None:
            if direccion not in self.constantes:
                raise ErrorEjecucion(f"Constante virtual no registrada: {direccion}")
            return self.constantes[direccion]
        return segmento.leer(direccion)

    def escribir(self, direccion, valor):
        self._segmento_de(direccion, para_escribir=True).escribir(direccion, valor)

    # ---------- Ciclo de ejecucion ----------
    def ejecutar(self):
        while not self.detener:
            if not 0 <= self.ip < len(self.fila.cuadruplos):
                raise ErrorEjecucion(f"Apuntador fuera de la fila de cuadruplos: {self.ip + 1}")
            self.ejecutar_cuadruplo_actual()
        return self.salida

    def ejecutar_cuadruplo_actual(self):
        cuadruplo = self.fila.cuadruplos[self.ip]
        operador = cuadruplo.operador

        if operador in ("+", "-", "*", "/", ">", "<", "!="):
            self._operacion(cuadruplo)
        elif operador == "=":
            self.escribir(cuadruplo.resultado_address, self.leer(cuadruplo.izquierdo_address))
        elif operador == "GOTO":
            self._saltar(cuadruplo.resultado)
            return
        elif operador == "GOTOF":
            if not self.leer(cuadruplo.izquierdo_address):
                self._saltar(cuadruplo.resultado)
                return
        elif operador == "PRINT":
            valor = self.leer(cuadruplo.resultado_address)
            self.salida.append(valor)
            print(valor)
        elif operador == "READ":
            self._leer_entrada(cuadruplo.resultado_address)
        elif operador == "ERA":
            self._era(cuadruplo.resultado)
        elif operador == "PARAM":
            self._param(cuadruplo)
        elif operador == "GOSUB":
            self._gosub(cuadruplo)
            return
        elif operador == "RETURN":
            self._return(cuadruplo)
            return
        elif operador == "ENDFUNC":
            self._endfunc()
            return
        elif operador == "END":
            self.detener = True
            return
        else:
            raise ErrorEjecucion(f"Codigo de operacion desconocido: {operador}")

        self.ip += 1

    def _saltar(self, numero_cuadruplo):
        if numero_cuadruplo is None:
            raise ErrorEjecucion("Salto sin destino")
        self.ip = int(numero_cuadruplo) - 1     # los cuadruplos se numeran desde 1

    # ---------- Operaciones ----------
    def _operacion(self, cuadruplo):
        operador = cuadruplo.operador
        izquierdo = self.leer(cuadruplo.izquierdo_address)
        derecho = self.leer(cuadruplo.derecho_address)

        if operador == "+":
            resultado = izquierdo + derecho
        elif operador == "-":
            resultado = izquierdo - derecho
        elif operador == "*":
            resultado = izquierdo * derecho
        elif operador == "/":
            if derecho == 0:
                raise ErrorEjecucion("Division entre cero")
            if isinstance(izquierdo, int) and isinstance(derecho, int):
                resultado = izquierdo // derecho          # division entera
            else:
                resultado = izquierdo / derecho
        elif operador == ">":
            resultado = izquierdo > derecho
        elif operador == "<":
            resultado = izquierdo < derecho
        else:  # "!="
            resultado = izquierdo != derecho

        self.escribir(cuadruplo.resultado_address, resultado)

    def _leer_entrada(self, direccion):
        if direccion is None:
            raise ErrorEjecucion("READ no tiene direccion destino")
        if self.indice_entrada < len(self.entradas):
            texto = self.entradas[self.indice_entrada]
            self.indice_entrada += 1
        else:
            texto = input()
        _, tipo, _ = MemoriaVirtual.decodificar(direccion)
        try:
            valor = convertir(tipo, texto)
        except ValueError:
            raise ErrorEjecucion(f"Entrada '{texto}' no es de tipo {tipo}")
        self.escribir(direccion, valor)

    # ---------- Funciones ----------
    def _era(self, nombre):
        """Reserva el registro de activacion con el tamano que calculo el compilador."""
        funcion = self.directorio.obtener_funcion(nombre)
        if funcion is None:
            raise ErrorEjecucion(f"Funcion no registrada: {nombre}")
        self.registros_nuevos.append(RegistroActivacion(funcion, nombre, funcion.tamano or {}))

    def _param(self, cuadruplo):
        """Copia el argumento (leido en el llamador) al parametro del registro nuevo."""
        if not self.registros_nuevos:
            raise ErrorEjecucion("PARAM sin ERA")
        valor = self.leer(cuadruplo.izquierdo_address)
        destino = cuadruplo.resultado_address
        nuevo = self.registros_nuevos[-1]
        segmento, _, _ = MemoriaVirtual.decodificar(destino)
        nuevo.segmento(segmento).escribir(destino, valor)

    def _gosub(self, cuadruplo):
        if not self.registros_nuevos:
            raise ErrorEjecucion("GOSUB sin ERA")
        if len(self.pila_registros) >= LIMITE_LLAMADAS:
            raise ErrorEjecucion("Desbordamiento de pila (demasiadas llamadas anidadas)")
        registro = self.registros_nuevos.pop()
        registro.ip_regreso = self.ip + 1
        self.pila_registros.append(registro)
        self._saltar(registro.funcion.inicio)

    def _return(self, cuadruplo):
        """Deja el valor en la global de retorno y regresa al llamador."""
        valor = self.leer(cuadruplo.izquierdo_address)
        self.escribir(cuadruplo.resultado_address, valor)
        self._regresar()

    def _endfunc(self):
        registro = self.registro_activo()
        if registro.funcion.retorno in ("int", "float"):
            raise ErrorEjecucion(f"La función '{registro.nombre}' terminó sin ejecutar return")
        self._regresar()

    def _regresar(self):
        if len(self.pila_registros) <= 1:
            raise ErrorEjecucion("Regreso de funcion sin llamada activa")
        registro = self.pila_registros.pop()
        self.ip = registro.ip_regreso
