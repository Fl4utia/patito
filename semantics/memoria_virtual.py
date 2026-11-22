"""
Administrador de direcciones virtuales de BabyDuck.
"""


class MemoriaVirtual:
    GLOBAL = {
        "int": 1000,
        "float": 2000,
        "bool": 3000,
    }
    LOCAL = {
        "int": 4000,
        "float": 5000,
        "bool": 6000,
    }
    TEMPORAL = {
        "int": 7000,
        "float": 8000,
        "bool": 9000,
    }
    CONSTANTE = {
        "int": 10000,
        "float": 11000,
        "bool": 12000,
        "string": 13000,
    }

    LIMITES = 1000

    def __init__(self):
        self.contadores = {
            ("global", "int"): self.GLOBAL["int"],
            ("global", "float"): self.GLOBAL["float"],
            ("global", "bool"): self.GLOBAL["bool"],
            ("local", "int"): self.LOCAL["int"],
            ("local", "float"): self.LOCAL["float"],
            ("local", "bool"): self.LOCAL["bool"],
            ("temporal", "int"): self.TEMPORAL["int"],
            ("temporal", "float"): self.TEMPORAL["float"],
            ("temporal", "bool"): self.TEMPORAL["bool"],
            ("constante", "int"): self.CONSTANTE["int"],
            ("constante", "float"): self.CONSTANTE["float"],
            ("constante", "bool"): self.CONSTANTE["bool"],
            ("constante", "string"): self.CONSTANTE["string"],
        }
        self.constantes = {}

    def asignar_variable(self, ambito, tipo):
        segmento = "global" if ambito == "global" else "local"
        if tipo not in ("int", "float", "bool"):
            raise ValueError("Tipo no valido para variable: " + str(tipo))
        clave = (segmento, tipo)
        direccion = self.contadores[clave]
        self._incrementar(clave)
        return direccion

    def asignar_temporal(self, tipo):
        if tipo not in self.TEMPORAL:
            raise ValueError("Tipo no valido para temporal: " + str(tipo))
        clave = ("temporal", tipo)
        direccion = self.contadores[clave]
        self._incrementar(clave)
        return direccion

    def asignar_constante(self, valor, tipo):
        tipo_clave = "string" if tipo == "string" else tipo
        clave = (tipo_clave, str(valor))
        if clave in self.constantes:
            return self.constantes[clave]
        if tipo_clave not in self.CONSTANTE:
            raise ValueError("Tipo no valido para constante: " + str(tipo))
        contador = ("constante", tipo_clave)
        direccion = self.contadores[contador]
        self._incrementar(contador)
        self.constantes[clave] = direccion
        return direccion

    def _incrementar(self, clave):
        direccion = self.contadores[clave]
        if direccion - self._base(clave) + 1 >= self.LIMITES:
            raise OverflowError("Sin direcciones disponibles en " + str(clave))
        self.contadores[clave] = direccion + 1

    def _base(self, clave):
        segmento, tipo = clave
        if segmento == "global":
            return self.GLOBAL[tipo]
        if segmento == "local":
            return self.LOCAL[tipo]
        if segmento == "temporal":
            return self.TEMPORAL[tipo]
        return self.CONSTANTE[tipo]
