from estructuras.uso_queue.queue import Queue


class TrabajoImpresion:


    def __init__(self, usuario, documento, paginas):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas

    def __str__(self):
        return f" {self.usuario} - {self.documento} ({self.paginas} pág.)"
    


class GestorImpresion:
    def __init__(self):
        self.cola = Queue()

    def agregar_trabajo(self, usuario, documento, paginas):
        if not usuario or not documento or paginas < 1:
            return None, "Error: datos inválidos."
        trabajo = TrabajoImpresion(usuario, documento, paginas)
        self.cola.enqueue(trabajo)
        return trabajo, "Trabajo agregado correctamente."

    def procesar_siguiente(self):
        if self.cola.is_empty():
            return None, "Error: la cola está vacía."
        trabajo = self.cola.firstQueue()
        self.cola.dequeue()
        return trabajo, f"Trabajo procesado: {trabajo}"

    def consultar_frente(self):
        if self.cola.is_empty():
            return None, "La cola está vacía."
        return self.cola.firstQueue(), "Trabajo en frente consultado."

    def trabajos_pendientes(self):
        temp = self.cola.first
        lista = []
        while temp is not None:
            lista.append(temp.data)
            temp = temp.next
        return lista

    def total_pendientes(self):
        return len(self.trabajos_pendientes())

