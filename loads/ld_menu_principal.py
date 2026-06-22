from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from loads.ld_lista_enlazada import dg_lis_enl_sim

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Menu_principal.ui",self)
        
        self.actionLista_Enlazada.triggered.connect(self.abrirlista_simple)
        
        
        
    def abrirlista_simple(self):
        dialogo = dg_lis_enl_sim()
        dialogo.exec_()
        