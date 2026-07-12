import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.uso_queue.sis_banco import Banco as BancoLogico


class DgBanco(QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ui", "sistema_banco.ui"))
        uic.loadUi(ui_path, self)

        self.banco = BancoLogico()

        self.btn_turno.clicked.connect(self.ingresar_turno)   
        self.btn_atender.clicked.connect(self.atender_cliente) 
        self.btn_cerrar.clicked.connect(self.cerrar_recepcion)
        self.textEdit.setReadOnly(True)

   
    def ingresar_turno(self):
        self.turno = self.ent_turno.text()
        if self.turno:
            turno = f"T{self.turno}"
            self.banco.ingresar_cliente(turno)
            cliente = self.banco.cola.last.data
            self.textEdit.append(f"{cliente.turno} → {cliente.hora_ingreso.strftime('%H:%M:%S')}")
            self.ent_turno.clear()

    def atender_cliente(self):
        if not self.banco.cola.is_empty():
            cliente = self.banco.cola.first.data
            self.banco.atender_cliente()
            self.remover_turno()
            self.lbl_atendido.setText(f"{cliente.turno} → {cliente.hora_atendido.strftime('%H:%M:%S')} → {cliente.tiempo_atencion} seg")
        else:
            self.lbl_atendido.setText("No hay clientes en espera.")
    

    def remover_turno(self):
        contenido = self.textEdit.toPlainText().splitlines()
        if contenido:
            contenido.pop(0)
            self.textEdit.setPlainText("\n".join(contenido))

    def cerrar_recepcion(self):
        self.banco.cerrar_recepcion()
        self.btn_turno.setEnabled(False)
        if not self.banco.cola.is_empty():
            self.lbl_cerrar.setText("Hay clientes por atender")
        else:
            self.lbl_cerrar.setText("Banco cerrado")

        
            self.lbl_no_clientes.setText(f"No clientes atendidos: {self.banco.clientes_atendidos}")
            if self.banco.clientes_atendidos > 0:
                promedio = self.banco.tiempo_total / self.banco.clientes_atendidos
            else:
                promedio = 0
            self.lbl_tiemp_prom.setText(f"Tiempo promedio: {promedio:.0f} seg")





