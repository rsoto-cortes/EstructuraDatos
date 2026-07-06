from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.lineales.pila_stack import Infija_a_Posfija
from estructuras.lineales.pila_stack import Evaluar_Expresion

class Dg_inf_pos(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/infija_posfija.ui", self)
        
        self.btn_conv.clicked.connect(self.convertir)
        self.btn_eval.clicked.connect(self.evaluar)
        
    def convertir(self):
        expresion = self.ent_dato.text().strip()
        if expresion:
            convertidor = Infija_a_Posfija()
            resultado = convertidor.convercion(expresion)
            self.lbl_resultado.setText(resultado)
        else:
            self.lbl_resultado.setText("Ingrese una expresión válida")
            
    def evaluar(self):
        expresion = self.ent_dato.text().strip()
        if expresion:
            evaluador = Evaluar_Expresion()
            resultado = evaluador.evaluar(expresion)
            self.lbl_res_ev.setText(str(resultado))
        else:
            self.lbl_res_ev.setText("Ingrese una expresión válida")
        