from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.uso_queue.queue import Queue

class Dg_queue(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/queue.ui",self)
        
        self.que = Queue()
        
        self.btn_deq.clicked.connect(self.dequ)
        self.btn_enq.clicked.connect(self.enqu)
        self.btn_firsq.clicked.connect(self.firstqu)
        self.btn_lasq.clicked.connect(self.lastqu)
        self.btn_prinq.clicked.connect(self.printq)
        
    def enqu(self):
        dato= self.ent_dato.text().strip()
        
        self.que.enqueue(dato)
        self.ent_dato.clear()
    
    
    def dequ(self):
        self.que.dequeue()
    
    
    def firstqu(self):
        valor= self.que.firstQueue()
        self.lbl_res.setText(f"El primer dato es: {valor}")
    
    def lastqu(self):
        valor = self.que.lastQueue()
        self.lbl_res.setText(f"El ultimo dato es: {valor}")
        
        
    def printq(self):
        self.lbl_res.setText(self.queue_lista())
    
    def queue_lista(self):
        temp = self.que.first
        if temp is None:
            return 'Queue vacío'
        parts = []
        while temp is not None:
            parts.append(str(temp.data))
            
            temp = temp.next
        return f"first-> {' -> '.join(parts)} <-last"