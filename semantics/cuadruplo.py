"""
Cuadruplo y Fila de cuadruplos.

Un cuadruplo es una instruccion de la forma (operador, izquierdo, derecho, resultado).
Los espacios que no se usan se guardan como None y se muestran como '-'.

    a = b + c * 2;      se traduce a:
        1  (*, c, 2, t1)
        2  (+, b, t1, t2)
        3  (=, t2, -, a)
"""


class Cuadruplo:
    """
    Atributos:
        operador (str): '+', '-', '*', '/', '>', '<', '!=', '=', 'PRINT', 'READ', 'RETURN'.
        izquierdo: primer operando (nombre, constante o temporal) o None.
        derecho: segundo operando o None.
        resultado: donde se guarda el resultado (temporal o variable) o None.
    """

    def __init__(self, operador, izquierdo, derecho, resultado,
                 izquierdo_address=None, derecho_address=None, resultado_address=None):
        self.operador = operador
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.resultado = resultado
        self.izquierdo_address = izquierdo_address
        self.derecho_address = derecho_address
        self.resultado_address = resultado_address

    def __str__(self):
        partes = [self.operador, self.izquierdo, self.derecho, self.resultado]
        textos = []
        for parte in partes:
            if parte is None:
                textos.append("-")
            else:
                textos.append(str(parte))
        return "(" + ", ".join(textos) + ")"

    def mostrar_virtual(self):
        partes = [
            self.operador,
            self.izquierdo_address if self.izquierdo_address is not None else self.izquierdo,
            self.derecho_address if self.derecho_address is not None else self.derecho,
            self.resultado_address if self.resultado_address is not None else self.resultado,
        ]
        textos = ["-" if parte is None else str(parte) for parte in partes]
        return "(" + ", ".join(textos) + ")"


class FilaCuadruplos:
    """
    Fila (cola) donde se van formando los cuadruplos en el orden en que se generan.
    Se agrega siempre al final; el numero de cuadruplo es su posicion + 1.

    Atributos:
        cuadruplos (list): lista de Cuadruplo.
    """

    def __init__(self):
        self.cuadruplos = []

    def agregar(self, operador, izquierdo, derecho, resultado,
                izquierdo_address=None, derecho_address=None, resultado_address=None):
        """Agrega un cuadruplo al final y devuelve su numero (empieza en 1)."""
        self.cuadruplos.append(Cuadruplo(
            operador, izquierdo, derecho, resultado,
            izquierdo_address, derecho_address, resultado_address,
        ))
        return len(self.cuadruplos)

    def llenar(self, numero_cuadruplo, resultado):
        """Rellena un resultado pendiente usando el numero interno 1-based."""
        if numero_cuadruplo < 1 or numero_cuadruplo > len(self.cuadruplos):
            raise IndexError("Cuadruplo pendiente fuera de rango")
        cuadruplo = self.cuadruplos[numero_cuadruplo - 1]
        cuadruplo.resultado = resultado
        cuadruplo.resultado_address = resultado

    def siguiente(self):
        """Numero de instruccion que tendra el siguiente cuadruplo."""
        return len(self.cuadruplos) + 1

    def mostrar(self):
        """Devuelve el contenido de la fila como texto, un cuadruplo por linea."""
        lineas = []
        numero = 1
        for cuadruplo in self.cuadruplos:
            lineas.append(f"{numero:>3}  {cuadruplo}")
            numero = numero + 1
        return "\n".join(lineas)

    def mostrar_virtual(self):
        lineas = []
        numero = 1
        for cuadruplo in self.cuadruplos:
            lineas.append(f"{numero:>3}  {cuadruplo.mostrar_virtual()}")
            numero += 1
        return "\n".join(lineas)