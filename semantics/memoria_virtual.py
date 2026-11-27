"""
Memoria virtual de BabyDuck (tiempo de compilacion).

El compilador no guarda valores: solo reparte DIRECCIONES. Cada variable,
temporal y constante recibe un numero que indica a que segmento y a que tipo
pertenece. La maquina virtual usa ese numero para saber donde leer o escribir.

Mapa de memoria (cada bloque tiene 1000 direcciones):

    Segmento     int           float         bool          string
    ---------    -----------   -----------   -----------   -----------
    Global       1000 - 1999   2000 - 2999   3000 - 3999        -
    Local        4000 - 4999   5000 - 5999   6000 - 6999        -
    Temporal     7000 - 7999   8000 - 8999   9000 - 9999        -
    Constante   10000 -10999  11000 -11999  12000 -12999  13000 -13999

Ejemplo:  5002  ->  segmento local, tipo float, desplazamiento 2
"""


class MemoriaVirtual:
    """Reparte direcciones virtuales por segmento y por tipo."""

    # Direccion donde empieza cada bloque:  segmento -> tipo -> direccion
    INICIO = {
        "global":    {"int": 1000,  "float": 2000,  "bool": 3000},
        "local":     {"int": 4000,  "float": 5000,  "bool": 6000},
        "temporal":  {"int": 7000,  "float": 8000,  "bool": 9000},
        "constante": {"int": 10000, "float": 11000, "bool": 12000, "string": 13000},
    }

    # Cuantas direcciones caben en cada bloque
    TAMANO_BLOQUE = 1000

    def __init__(self):
        """Todos los contadores empiezan en el inicio de su bloque."""
        # Siguiente direccion libre de cada bloque:  segmento -> tipo -> direccion
        self.siguiente = {}
        for segmento, tipos in self.INICIO.items():
            self.siguiente[segmento] = dict(tipos)

        # Tabla de constantes:  (tipo, texto) -> direccion
        # Sirve para que la misma constante (ej. el 2) tenga una sola direccion.
        self.constantes = {}

    # ------------------------------------------------------------------
    # Reservar direcciones
    # ------------------------------------------------------------------
    def asignar_variable(self, ambito, tipo):
        """
        Reserva la direccion de una variable (o parametro).

        Args:
            ambito (str): "global" para variables del programa, "local" para
                variables y parametros de una funcion.
            tipo (str): "int", "float" o "bool".

        Returns:
            int: la direccion virtual asignada.
        """
        if tipo not in ("int", "float", "bool"):
            raise ValueError(f"Tipo no valido para variable: {tipo}")

        if ambito == "global":
            return self._reservar("global", tipo)
        else:
            return self._reservar("local", tipo)

    def asignar_temporal(self, tipo):
        """
        Reserva la direccion de un temporal (resultado intermedio, ej. t1).

        Args:
            tipo (str): "int", "float" o "bool".

        Returns:
            int: la direccion virtual asignada.
        """
        if tipo not in ("int", "float", "bool"):
            raise ValueError(f"Tipo no valido para temporal: {tipo}")
        return self._reservar("temporal", tipo)

    def asignar_constante(self, texto, tipo):
        """
        Devuelve la direccion de una constante. Si ya existia, reutiliza la misma.

        Args:
            texto (str): la constante tal como aparece en el programa ("3", "2.5", '"hola"').
            tipo (str): "int", "float", "bool" o "string".

        Returns:
            int: la direccion virtual de la constante.
        """
        llave = (tipo, str(texto))

        # 1. Si la constante ya tiene direccion, se reutiliza
        if llave in self.constantes:
            return self.constantes[llave]

        # 2. Si no, se reserva una nueva y se anota en la tabla
        direccion = self._reservar("constante", tipo)
        self.constantes[llave] = direccion
        return direccion

    def _reservar(self, segmento, tipo):
        """
        Toma la siguiente direccion libre del bloque (segmento, tipo) y avanza el contador.

        Raises:
            OverflowError: si el bloque ya no tiene direcciones libres.
        """
        if tipo not in self.INICIO[segmento]:
            raise ValueError(f"El segmento {segmento} no tiene tipo {tipo}")

        direccion = self.siguiente[segmento][tipo]
        usadas = direccion - self.INICIO[segmento][tipo]
        if usadas >= self.TAMANO_BLOQUE:
            raise OverflowError(f"Sin direcciones disponibles en {segmento} {tipo}")

        self.siguiente[segmento][tipo] = direccion + 1
        return direccion

    # ------------------------------------------------------------------
    # Funciones: cada una tiene su propio espacio local
    # ------------------------------------------------------------------
    def reiniciar_locales(self):
        """
        Regresa los contadores locales y temporales al inicio de su bloque.

        Se llama al empezar cada funcion y al empezar main: en ejecucion cada
        llamada tiene su propio registro de activacion, asi que las direcciones
        locales de funciones distintas pueden repetirse sin chocar.
        """
        for segmento in ("local", "temporal"):
            for tipo, inicio in self.INICIO[segmento].items():
                self.siguiente[segmento][tipo] = inicio

    def tamano(self, segmento):
        """
        Cuantas direcciones de cada tipo se han usado en un segmento.

        Returns:
            dict: tipo -> cantidad.  Ej. {"int": 2, "float": 0, "bool": 1}
        """
        usadas = {}
        for tipo, inicio in self.INICIO[segmento].items():
            usadas[tipo] = self.siguiente[segmento][tipo] - inicio
        return usadas

    def tamano_funcion(self):
        """
        Recursos que necesita la funcion que se acaba de compilar.
        La maquina virtual lo usa en ERA para reservar su memoria.

        Returns:
            dict: {"local": {tipo: n}, "temporal": {tipo: n}}
        """
        return {
            "local": self.tamano("local"),
            "temporal": self.tamano("temporal"),
        }

    # ------------------------------------------------------------------
    # Traducir una direccion
    # ------------------------------------------------------------------
    @classmethod
    def decodificar(cls, direccion):
        """
        Dice a que segmento y tipo pertenece una direccion.

        Args:
            direccion (int): direccion virtual, ej. 5002.

        Returns:
            tuple: (segmento, tipo, desplazamiento), ej. ("local", "float", 2).
        """
        for segmento, tipos in cls.INICIO.items():
            for tipo, inicio in tipos.items():
                if inicio <= direccion < inicio + cls.TAMANO_BLOQUE:
                    return segmento, tipo, direccion - inicio
        raise ValueError(f"Direccion virtual fuera del mapa: {direccion}")
