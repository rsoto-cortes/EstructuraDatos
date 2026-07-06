from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
        
    # Insertar un elemento en la pila
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    # Eliminar un elemento
    #Retornar el valor eliminado
    def pop(self):
        if self.top is None:
            return None
        valor = self.top.data
        self.top = self.top.next
        return valor
    
    #Retornar el valor del nodo en el tope
    def top_of_stack(self):
        if self.top != None:
            return self.top.data

    
    
    # Muestra el contenido de la pila    
    def print_stack(self):
        temp = self.top
        valores = []
        while temp is not None:
            valores.append(str(temp.data))
            temp = temp.next
        return "Top-> " + "->".join(valores)


# -------------------------------
# Conversor de infija a posfija
# -------------------------------
class Infija_a_Posfija:
    def __init__(self):
        self.stack = Stack()
        self.output = []

    def obtener_precedente(self, op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        if op == '$':  # potencia
            return 3
        return 0

    def definir_operador(self, c):
        return c in ['+', '-', '*', '/', '$']

    def convercion(self, expression: str) -> str:
        self.output = []  # limpiar salida en cada conversión
        for token in expression:
            if token.isalnum():  # operando
                self.output.append(token)
            elif token == '(':
                self.stack.push(token)
            elif token == ')':
                while not self.stack.is_empty() and self.stack.top_of_stack() != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  # eliminar '('
            elif self.definir_operador(token):
                while (not self.stack.is_empty() and 
                       self.obtener_precedente(self.stack.top_of_stack()) >= self.obtener_precedente(token)):
                    self.output.append(self.stack.pop())
                self.stack.push(token)

        while not self.stack.is_empty():
            self.output.append(self.stack.pop())

        return "".join(self.output)
    
class Evaluar_Expresion:
    def __init__(self):
        self.stack = Stack()
        self.convertidor = Infija_a_Posfija()  # reutilizamos tu clase

    def aplicar_operacion(self, op, a, b):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        if op == '$': return a ** b  # potencia

    def evaluar(self, expresion_infija: str) -> float:
        # Paso 1: convertir a posfija con tu clase
        posfija = self.convertidor.convercion(expresion_infija)

        # Paso 2: recorrer la posfija y usar la pila
        for token in posfija:
            if token.isdigit():
                self.stack.push(int(token))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                resultado = self.aplicar_operacion(token, a, b)
                self.stack.push(resultado)

        return self.stack.pop()
