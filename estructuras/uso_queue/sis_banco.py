from estructuras.uso_queue.queue import Queue
import datetime

class Cliente:
    def __init__(self, turno):
        self.turno = turno
        self.hora_ingreso = datetime.datetime.now()
        self.hora_atendido = None
        self.tiempo_atencion = None

    def atender(self):
        self.hora_atendido = datetime.datetime.now()
        self.tiempo_atencion = (self.hora_atendido - self.hora_ingreso).seconds
        return self.tiempo_atencion


class Banco:
    def __init__(self):
        self.cola = Queue()
        self.clientes_atendidos = 0
        self.tiempo_total = 0
        self.recepcion_abierta = True

    def ingresar_cliente(self, turno):
        if not self.recepcion_abierta:
            return
        cliente = Cliente(turno)
        self.cola.enqueue(cliente)


    def atender_cliente(self):
        if self.cola.is_empty():

            return
        cliente = self.cola.first.data
        self.cola.dequeue()
        tiempo = cliente.atender()
        self.clientes_atendidos += 1
        self.tiempo_total += tiempo


    def cerrar_recepcion(self):
        self.recepcion_abierta = False

    def resumen(self):
        if self.clientes_atendidos > 0:
            promedio = self.tiempo_total / self.clientes_atendidos
        else:
            promedio = 0
        print(f"Clientes atendidos: {self.clientes_atendidos}")
        print(f"Tiempo promedio de atención: {promedio:.2f} segundos")
