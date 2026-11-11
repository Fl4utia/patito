class Stack:
    """
    Un stack.
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        Agrega un elemento a la parte superior de la pila.
        """
        self.stack.append(element)

    def pop(self):
        """
        Elimina y devuelve el elemento en la parte superior de la pila.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise Exception("Cannot pop from empty stack.")

    def is_empty(self):
        """
        Comprueba si la pila está vacía.
        """
        return len(self.stack) == 0

    def tamano(self):
        """
        Devuelve el número de elementos en la pila.
        """
        return len(self.stack)

    def peek(self):
        """
        Que es el elemento de hasta arriba.
        """
        if not self.is_empty():
            return self.stack[-1]
        raise Exception("Cannot peek into empty stack.")