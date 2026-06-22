from estructuras.lineales.lista_enlazada_simple import LinkedList
class Menu(object):
    def __init__(self):
        self.lista = LinkedList()
        self.opcion = 0
    
    def mostrar_menu(self): 
        print("Menu de Lista Enlazada")
        print("1-Insertar al inicio")
        print("2-Insertar al final")
        print("3-Buscar")
        print("4-Imprimir")
        print("5-Eliminar el primer numero")
        print("6-Eliminar el ultimo numero")
        print("7-Salir")
        
    def opciones(self):
        self.opcion = int(input("Seleccione una opcion: "))
    
        match self.opcion :
            case 1:
                num=int(input("Inserte el dato a agregar:"))
                self.lista.insert_at_beginning(num)
            
            case 2:
                num=int(input("Inserte el dato a agregar:"))
                self.lista.insert_at_end(num)
                
            case 3:
                num=int(input("Ingrese el dato a buscar:"))
                encontrado=self.lista.search(num)
                if encontrado:
                    print(f"Elemento {num} encontrado en la lista")
                else:
                    print(f"Elementp {num} no encontrado en la lista")
                
            case 4:
                print("La lista completa es:")
                self.lista.print_list()
            
            case 5:
                self.lista.delet_at_beginning()
                
            case 6:
                self.lista.delet_at_end()
            
            
            case 7:
                print("Saliendo...")
                
            case _:
                print("Opción no válida. Intenta de nuevo.")
    
    def ejecutar(self):
        while self.opcion != 7:
            self.mostrar_menu()
            self.opciones()