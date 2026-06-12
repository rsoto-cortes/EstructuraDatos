from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data):
        #paso1: crear un nuevo nodo con el dato
        new_node = Node(data)
        
        #paso2: verificar si la lista esta vacia
        if self.head is None and self.tail is None:
            #si la lista esta vacia, el nuevo nodo sera tanto la cabeza como la cola
            self.head = new_node
            self.tail = new_node
        else:
            #si la lista no esta vacia, el nuevo nodo se convierte en la nueva cabeza
            new_node.next = self.head
            # luego, actualizamos la cabeza para que apunte al nuevo nodo
            self.head = new_node
    
    def print_list(self):
        temp = self.head
        print("Head -> ", end="")
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next
        print("<- Tail")
        print("None")
        
        
        