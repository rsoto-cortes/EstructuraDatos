from estructuras.uso_queue.queue import Queue

class Menu(object):
    def __init__(self):
        self.cola=Queue()
        self.opcion=0
        
    def mostrar_menu(self):
        print("Menu Queue")
        print("1-Agregar")
        print("2-Eliminar")
        print("3-Primer dato")
        print("4-Ultimo dato")
        print("5-imprimir Queue")
        print("6-Salir")
    
    def opciones(self):
        self.opcion= int(input("Seleccione una opcion: "))
        
        match self.opcion:
            case 1:
                num=int(input("Inserte el dato a agregar: "))
                self.cola.enqueue(num)
            case 2 :
                self.cola.dequeue()
                
            case 3 :
                print("El primer dato es: ")
                print (self.cola.firstQueue())
            case 4 :
                print("El ultimo dato es: ")
                print(self.cola.lastQueue())
            
            case 5:
                print("La lista completa es: ")
                self.cola.printQueue()
            
            case 6 :
                print("Saliendo..")
                
            case _:
                print("Opcion no encontrada")
                
    def ejecutar(self):
        while self.opcion != 6:
            self.mostrar_menu()
            self.opciones()