import sys
from PyQt5.QtWidgets import QApplication
from loads.ld_menu_principal import VentanaPrincipal


def main():
   app = QApplication(sys.argv)
   menu = VentanaPrincipal()
   menu.show()
   sys.exit(app.exec_())


if __name__ == "__main__":
   main()