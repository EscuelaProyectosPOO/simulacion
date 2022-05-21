import re
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr

class Ventana_datos_ventas(QDialog):

    def __init__(self):

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("interfaces/ventana_vebntas/Ingreso_datos_ventas.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)
        self.opciones()

        #conectar botones
        self.btnmas.clicked.connect(self.agregar_filas)
        self.btnmenos.clicked.connect(self.eliminar_filas)
        self.tablas_opcion.activated.connect(self.opciones)

    def opciones(self):
        # en base a la opcion escogida se desata una accion
        
        if(self.tablas_opcion.currentIndex() == 0):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada \n en minutos', 'Probabilidad'])

            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        elif(self.tablas_opcion.currentIndex() == 1):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de estancia \n en minutos', 'Probabilidad'])

            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        elif(self.tablas_opcion.currentIndex() == 2):

            self.tabla.setColumnCount(3)
            self.tabla.setHorizontalHeaderLabels (['Tipo de alcohol \n  que se lleva', 'Costo botella', 'Probabilidad'])

            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def agregar_filas(self):

        posicion_fila = self.tabla.rowCount()
        self.tabla.insertRow(posicion_fila)

    def eliminar_filas(self):

        posicion_fila = self.tabla.rowCount()
        self.tabla.removeRow(posicion_fila-1)


    def tomar_valores_tabla(self, matriz):
        
        for i in range(self.tabla.rowCount()):

            for j in range(self.tabla.columnCount()):

                valor_celda = self.tabla.item(i, j)
                matriz[i][j] = float(valor_celda.text())


        return matriz


if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_datos_ventas()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()