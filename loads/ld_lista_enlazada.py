from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from estructuras.lineales.lista_enlazada_simple import LinkedList


class dg_lis_enl_sim(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Lista_enlazada.ui", self)

        self.lista = LinkedList()

        self.btn_ag_i.clicked.connect(self.agregar_i)
        self.btn_ag_f.clicked.connect(self.agregar_f)
        self.btn_imp.clicked.connect(self.imprimir)
        self.btn_el_i.clicked.connect(self.elim_i)
        self.btn_el_f.clicked.connect(self.elim_f)
        self.btn_bus.clicked.connect(self.buscar)

    def agregar_i(self):
        valor = self.ent_num.text().strip()
        
        self.lista.insert_at_beginning(valor)
        self.ent_num.clear()

    def agregar_f(self):
        valor = self.ent_num.text().strip()

        self.lista.insert_at_end(valor)
        self.ent_num.clear()
    
    def imprimir(self):
        self.lbl_res.setText(self._lista_str())

    def elim_i(self):
        self.lista.delet_at_beginning()

    def elim_f(self):
        self.lista.delet_at_end()

    def buscar(self):
        valor = self.ent_num.text().strip()

        encontrado = self.lista.search(valor)
        self.lbl_res.setText('Encontrado' if encontrado else 'No encontrado')

    def _lista_str(self):
        temp = self.lista.head
        if temp is None:
            return 'Lista vacía'
        parts = []
        while temp is not None:
            parts.append(str(temp.data))
            
            temp = temp.next
        return f"head-> {' -> '.join(parts)} <-tail none"