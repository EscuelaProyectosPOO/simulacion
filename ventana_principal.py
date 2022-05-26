import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import ctypes
from interfaces.ventanas_produccion.ventana_datos_produccion import Ventana_datos_produccion
from interfaces.ventanas_abastecimiento import ventana_abastecimiento
from interfaces.ventana_ventas.ventana_datos_ventas import Ventana_datos_ventas
class Ventana_principal(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("pantalla_principal.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)
        self.btnproduccion.clicked.connect(self.produccion)
        self.btnabastecimiento.clicked.connect(self.abastecimiento)
        self.btnventa.clicked.connect(self.ventas)

    
    def produccion(self):
        
        self.hide()
        self.ex = Ventana_datos_produccion(self)
        self.ex.show()

    def abastecimiento(self):

        self.hide()
        self.ex = ventana_abastecimiento.Ventana_datos_abastecimiento(self)
        self.ex.show()

    def ventas(self):

        self.hide()
        self.ex = Ventana_datos_ventas(self)
        self.ex.show()

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()