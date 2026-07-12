import sys
from PyQt5.QtWidgets import QApplication
from loads.ld_menu_principal import VentanaPrincipal

#Esto se utilizo para correrlo en la terminal
"""from menus.menu2 import Menu"""
   
"""def main():
   menu =Menu()
   menu.ejecutar()"""
   
#Este main se encarga de mostrar el sistema del banco

"""from PyQt5 import QtWidgets
from loads.ld_banco import DgBanco
def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = DgBanco()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#Este main se encarga de mostrar la ventana principal con los proyectos de estructura lineal

def main():
   app = QApplication(sys.argv)
   menu = VentanaPrincipal()
   menu.show()
   sys.exit(app.exec_())


if __name__ == "__main__":
    main()
