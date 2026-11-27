"""
Pila (stack): estructura LIFO, el ultimo en entrar es el primero en salir.

Se usa en el generador de cuadruplos para operandos, operadores, saltos
pendientes y llamadas a funcion.
"""


class Pila:
    """Pila simple sobre una lista de Python (el tope es el final de la lista)."""

    def __init__(self):
        self.elementos = []

    def meter(self, elemento):
        """Coloca un elemento en el tope de la pila (push)."""
        self.elementos.append(elemento)

    def sacar(self):
        """
        Quita y devuelve el elemento del tope (pop).

        Raises:
            IndexError: si la pila esta vacia.
        """
        if self.esta_vacia():
            raise IndexError("No se puede sacar de una pila vacia")
        return self.elementos.pop()

    def tope(self):
        """
        Devuelve el elemento del tope sin quitarlo (peek).

        Raises:
            IndexError: si la pila esta vacia.
        """
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.elementos[-1]

    def esta_vacia(self):
        """True si la pila no tiene elementos."""
        return len(self.elementos) == 0

    def tamano(self):
        """Numero de elementos en la pila."""
        return len(self.elementos)
