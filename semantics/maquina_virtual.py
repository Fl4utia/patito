"""
Maquina Virtual de BabyDuck.

Ejecuta la fila de cuadruplos usando direcciones virtuales.
"""


class ErrorEjecucion(Exception):
    pass


class FrameActivacion:
    def __init__(self, funcion=None, nombre="main", inicio=None, return_address=None):
        self.funcion = funcion
        self.nombre = nombre
        self.inicio = inicio
        self.return_address = return_address
        self.return_ip = None
        self.memoria = {}

    def escribir(self, direccion, valor):
        self.memoria[direccion] = valor

    def leer(self, direccion, default=None):
        return self.memoria.get(direccion, default)


class MaquinaVirtual:
    def __init__(self, fila, directorio=None, constantes=None, entradas=None):
        self.fila = fila
        self.directorio = directorio
        self.constantes = {} if constantes is None else dict(constantes)
        self.entradas = list(entradas or [])
        self.indice_entrada = 0
        self.globales = {}
        self.frames = []
        self.frames_pendientes = []
        self.return_values = {}
        self.salida = []
        self.ip = 0
        self.detener = False

        self._cargar_constantes()
        self._crear_main()

    def _cargar_constantes(self):
        if not hasattr(self.fila, "cuadruplos"):
            raise ErrorEjecucion("La fila no contiene cuadruplos")

        for cuadruplo in self.fila.cuadruplos:
            for nombre, direccion in (
                (cuadruplo.izquierdo, cuadruplo.izquierdo_address),
                (cuadruplo.derecho, cuadruplo.derecho_address),
                (cuadruplo.resultado, cuadruplo.resultado_address),
            ):
                if direccion is None or direccion not in range(10000, 14000):
                    continue
                if direccion in self.constantes:
                    continue
                if nombre is None:
                    continue

                texto = str(nombre)
                if 10000 <= direccion < 11000:
                    self.constantes[direccion] = int(texto)
                elif 11000 <= direccion < 12000:
                    self.constantes[direccion] = float(texto)
                elif 12000 <= direccion < 13000:
                    if texto.lower() in ("true", "1"):
                        self.constantes[direccion] = True
                    elif texto.lower() in ("false", "0"):
                        self.constantes[direccion] = False
                    else:
                        raise ErrorEjecucion(
                            "Constante booleana invalida: " + texto
                        )
                else:
                    if len(texto) >= 2 and texto[0] == '"' and texto[-1] == '"':
                        texto = texto[1:-1]
                    self.constantes[direccion] = texto

    def _crear_main(self):
        if self.directorio is not None:
            nombre = self.directorio.nombre_programa
            programa = self.directorio.obtener_funcion(nombre)
            if programa is not None and programa.inicio is not None:
                self.ip = programa.inicio - 1
        main = FrameActivacion(nombre="main", inicio=self.ip + 1)
        self.frames.append(main)

    def frame_activo(self):
        if not self.frames:
            return None
        return self.frames[-1]

    def leer(self, direccion):
        if direccion is None:
            raise ErrorEjecucion("Se intento leer una direccion None")
        if 10000 <= direccion < 14000:
            if direccion not in self.constantes:
                raise ErrorEjecucion(
                    "Constante virtual no registrada: " + str(direccion)
                )
            return self.constantes[direccion]
        if 1000 <= direccion < 4000:
            return self.globales.get(direccion, 0)

        frame = self.frame_activo()
        if frame is None:
            return 0
        return frame.leer(direccion, 0)

    def leer_retorno(self, direccion):
        if direccion in self.return_values:
            return self.return_values[direccion]
        return self.leer(direccion)

    def escribir(self, direccion, valor):
        if direccion is None:
            raise ErrorEjecucion("Se intento escribir en una direccion None")
        if 10000 <= direccion < 14000:
            raise ErrorEjecucion(
                "No se puede escribir en memoria constante: " + str(direccion)
            )
        if 1000 <= direccion < 4000:
            self.globales[direccion] = valor
            return

        frame = self.frame_activo()
        if frame is None:
            raise ErrorEjecucion("No existe un frame activo")
        frame.escribir(direccion, valor)

    def ejecutar(self):
        while not self.detener and 0 <= self.ip < len(self.fila.cuadruplos):
            self.ejecutar_cuadruplo_actual()
        return self.salida

    def ejecutar_cuadruplo_actual(self):
        cuadruplo = self.fila.cuadruplos[self.ip]
        operador = cuadruplo.operador

        if operador in ("+", "-", "*", "/", ">", "<", "!=", "="):
            self._ejecutar_operacion(cuadruplo)
        elif operador == "GOTO":
            destino = cuadruplo.resultado_address
            if destino is None:
                destino = cuadruplo.resultado
            self.ip = int(destino) - 1
            return
        elif operador == "GOTOF":
            direccion = cuadruplo.izquierdo_address
            destino = cuadruplo.resultado_address
            if destino is None:
                destino = cuadruplo.resultado
            if not bool(self.leer(direccion)):
                self.ip = int(destino) - 1
                return
        elif operador == "PRINT":
            direccion = cuadruplo.resultado_address
            if direccion is None:
                valor = cuadruplo.resultado
            else:
                valor = self.leer(direccion)
            self.salida.append(valor)
            print(valor)
        elif operador == "READ":
            direccion = cuadruplo.resultado_address
            if direccion is None:
                raise ErrorEjecucion("READ no tiene direccion destino")
            if self.indice_entrada >= len(self.entradas):
                valor = input()
                try:
                    if 1000 <= direccion < 2000 or 4000 <= direccion < 5000:
                        valor = int(valor)
                    elif 2000 <= direccion < 3000 or 5000 <= direccion < 6000:
                        valor = float(valor)
                except ValueError:
                    raise ErrorEjecucion(
                        "Entrada incompatible con la direccion " + str(direccion)
                    )
            else:
                valor = self.entradas[self.indice_entrada]
                self.indice_entrada += 1
                if 1000 <= direccion < 2000 or 4000 <= direccion < 5000:
                    valor = int(valor)
                elif 2000 <= direccion < 3000 or 5000 <= direccion < 6000:
                    valor = float(valor)
            self.escribir(direccion, valor)
        elif operador == "ERA":
            self._crear_frame_pendiente(cuadruplo)
        elif operador == "PARAM":
            self._copiar_parametro(cuadruplo)
        elif operador == "GOSUB":
            self._iniciar_llamada(cuadruplo)
            return
        elif operador == "RETURN":
            self._retornar(cuadruplo)
            return
        elif operador == "ENDFUNC":
            self._terminar_funcion()
            return

        self.ip += 1

    def _ejecutar_operacion(self, cuadruplo):
        operador = cuadruplo.operador
        destino = cuadruplo.resultado_address

        if operador == "=":
            origen = cuadruplo.izquierdo_address
            if cuadruplo.izquierdo is not None and str(cuadruplo.izquierdo).endswith("()"):
                valor = self.leer_retorno(origen)
            else:
                valor = self.leer(origen)
            self.escribir(destino, valor)
            return

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
                resultado = izquierdo // derecho
            else:
                resultado = izquierdo / derecho
        elif operador == ">":
            resultado = izquierdo > derecho
        elif operador == "<":
            resultado = izquierdo < derecho
        elif operador == "!=":
            resultado = izquierdo != derecho
        else:
            raise ErrorEjecucion("Operador no reconocido: " + operador)

        self.escribir(destino, resultado)

    def _crear_frame_pendiente(self, cuadruplo):
        nombre = cuadruplo.resultado
        if self.directorio is None:
            raise ErrorEjecucion("La maquina no tiene directorio de funciones")
        funcion = self.directorio.obtener_funcion(nombre)
        if funcion is None:
            raise ErrorEjecucion("Funcion no registrada: " + str(nombre))

        frame = FrameActivacion(
            funcion=funcion,
            nombre=nombre,
            inicio=funcion.inicio,
            return_address=funcion.retorno_address,
        )
        for nombre_parametro, tipo_parametro in funcion.parametros:
            del tipo_parametro
        for nombre_variable, info in funcion.variables.variables.items():
            frame.escribir(info["address"], 0)
        self.frames_pendientes.append(frame)

    def _copiar_parametro(self, cuadruplo):
        if not self.frames_pendientes:
            raise ErrorEjecucion("PARAM sin ERA")
        valor = self.leer(cuadruplo.izquierdo_address)
        destino = cuadruplo.resultado_address
        self.frames_pendientes[-1].escribir(destino, valor)

    def _iniciar_llamada(self, cuadruplo):
        if not self.frames_pendientes:
            raise ErrorEjecucion("GOSUB sin ERA")

        frame = self.frames_pendientes.pop()
        frame.return_ip = self.ip + 1
        destino = cuadruplo.resultado_address
        if destino is None:
            destino = cuadruplo.resultado
        self.frames.append(frame)
        self.ip = int(destino) - 1

    def _retornar(self, cuadruplo):
        frame = self.frame_activo()
        if frame is None:
            raise ErrorEjecucion("RETURN sin frame activo")
        valor = self.leer(cuadruplo.izquierdo_address)
        direccion_retorno = cuadruplo.resultado_address
        if direccion_retorno is not None:
            self.return_values[direccion_retorno] = valor

        frame = self.frames.pop()
        self.ip = frame.return_ip

    def _terminar_funcion(self):
        if not self.frames:
            self.detener = True
            return
        frame = self.frames[-1]
        if frame.nombre == "main":
            self.frames.pop()
            self.detener = True
            return
        self.frames.pop()
        self.ip = frame.return_ip
