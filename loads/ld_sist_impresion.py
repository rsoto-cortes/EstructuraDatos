import sys
from PyQt5.QtWidgets import QDialog,QTableWidgetItem
from PyQt5 import uic
from estructuras.uso_queue.sis_impresion import GestorImpresion

class DgImpresion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/sistema_impresion.ui", self)  # carga el archivo .ui

        # Instancia del gestor
        self.gestor = GestorImpresion()

        # Configurar tabla
        self.tablaCola.setColumnCount(3)
        self.tablaCola.setHorizontalHeaderLabels(
            ["Usuario", "Documento", "Páginas"]
        )

        # Conectar botones
        self.btnAgregar.clicked.connect(self.agregar_trabajo)
        self.btnImprimir.clicked.connect(self.procesar_trabajo)
        self.btnConsultar.clicked.connect(self.consultar_frente)

    def agregar_trabajo(self):
        usuario = self.txtUsuario.text().strip()
        documento = self.txtDocumento.text().strip()
        paginas = self.spinPaginas.value()

        trabajo, mensaje = self.gestor.agregar_trabajo(usuario, documento, paginas)
        self.txtMensajes.append(mensaje)

        if trabajo:
            self.actualizar_tabla()
        
        self.txtUsuario.clear()
        self.txtDocumento.clear()
        self.spinPaginas.clear()

    def procesar_trabajo(self):
        trabajo, mensaje = self.gestor.procesar_siguiente()
        self.txtMensajes.append(mensaje)
        self.actualizar_tabla()

    def consultar_frente(self):
        trabajo, mensaje = self.gestor.consultar_frente()
        if trabajo:
            self.txtMensajes.append(f"Frente: {trabajo}")
        else:
            self.txtMensajes.append(mensaje)

    def actualizar_tabla(self):
        trabajos = self.gestor.trabajos_pendientes()
        self.tablaCola.setRowCount(len(trabajos))

        for i, t in enumerate(trabajos):
            self.tablaCola.setItem(i, 0, QTableWidgetItem(t.usuario))
            self.tablaCola.setItem(i, 1, QTableWidgetItem(t.documento))
            self.tablaCola.setItem(i, 2, QTableWidgetItem(str(t.paginas)))

        self.lblTotal.setText(f"Total pendientes: {len(trabajos)}")
