from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.lineales.pila_stack import Infija_a_Posfija

class Dg_inf_pos(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/infija_posfija.ui", self)
        
        self.btn_conv.clicked.connect(self.convertir)
        
    def convertir(self):
        expresion = self.ent_dato.text().strip()
        if expresion:
            convertidor = Infija_a_Posfija()
            resultado = convertidor.convercion(expresion)
            self.lbl_resultado.setText(f"Posfija: {resultado}")
        else:
            self.lbl_resultado.setText("Ingrese una expresión válida")