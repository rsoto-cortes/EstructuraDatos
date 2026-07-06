from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.lineales.pila_stack import Stack
from estructuras.lineales.nodo import Node

class Dg_Stack(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Pila_stack.ui", self)
        
        self.da = None
        self.ag = Stack()
        
        self.btn_agr.clicked.connect(self.agre)
        self.btn_elim.clicked.connect(self.elimi)
        self.btn_imp.clicked.connect(self.prin)
        self.btn_mos.clicked.connect(self.to)   
        
        
    def agre(self):
        self.da = self.ent_dato.text().strip()
        if self.da:
            self.ag.push(self.da)
            self.ent_dato.clear()
        else:
            self.lbl_resultado.setText("Ingrese un valor")
        
    def elimi(self):
        eliminado = self.ag.pop()
        if eliminado is None:
            self.lbl_resultado.setText("Pila vacía")
        else:
            self.lbl_resultado.setText(f"Se eliminó: {eliminado}")
        
    def prin(self):
        self.lbl_resultado.setText(self.ag.print_stack())

    def to(self):
        self.lbl_resultado.setText(f"Top-> {self.ag.top_of_stack()}")
        
        
