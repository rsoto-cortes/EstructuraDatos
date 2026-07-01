from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from loads.ld_lista_enlazada import dg_lis_enl_sim
from loads.ld_pila_stack import Dg_Stack
from loads.ld_enfija_posfija import Dg_inf_pos

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Menu_principal.ui",self)
        
        self.actionLista_Enlazada.triggered.connect(self.abrirlista_simple)
        self.actionPila_o_Stack.triggered.connect(self.abrir_pila)
        self.actionInfija_a_Posfija.triggered.connect(self.abrir_inf_posf)
        self.actionSalir.triggered.connect(self.close)
        
        
    def abrirlista_simple(self):
        dialogo = dg_lis_enl_sim()
        dialogo.exec_()
       
       
    def abrir_pila(self):
        dialogo = Dg_Stack()
        dialogo.exec_()
        
    def abrir_inf_posf(self):
        dialogo=Dg_inf_pos()
        dialogo.exec_()