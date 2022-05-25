
import os
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from pathlib import Path

class Ventana_datos_abastecimiento(QDialog):

    def __init__(self):

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("interfaces/ventanas_abastecimiento/Ingreso_datos_abastecimiento.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.opciones()
        
        #conectar botones
        self.btnmas.clicked.connect(lambda :self.agregar_filas(self.tabla))
        self.btnmenos.clicked.connect(lambda :self.eliminar_filas(self.tabla))
        self.btnmas2.clicked.connect(lambda :self.agregar_filas(self.tabla2))
        self.btnmenos2.clicked.connect(lambda :self.eliminar_filas(self.tabla2))
        self.tablas_opcion.activated.connect(self.opciones)#cambia la tabla deacuerdo a la opcion seleccionada
        self.Guardar.clicked.connect(self.openFileNameDialog)

    def opciones(self):
        # en base a la opcion escogida se desata una accion
        
        if(self.tablas_opcion.currentIndex() == 0):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada piñas\n en días ', 'Probabilidad'])
            
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio piñas', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        
        elif(self.tablas_opcion.currentIndex() == 1):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada botellas\n de vidrio, en días ', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de botellas\n de vidrio, en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        elif(self.tablas_opcion.currentIndex() == 2):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada botellas\n de plastico, en días ', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de botellas\n de plastico, en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        elif(self.tablas_opcion.currentIndex() == 3):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada tapones y\n corchos, en días ', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de tapones y\n corchos, en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)



    def agregar_filas(self, nombre_tabla):

        posicion_fila = nombre_tabla.rowCount()
        nombre_tabla.insertRow(posicion_fila)

    def eliminar_filas(self, nombre_tabla):

        posicion_fila = nombre_tabla.rowCount()
        nombre_tabla.removeRow(posicion_fila-1)


    def tomar_valores_tabla(self, matriz):
        
        for i in range(self.tabla.rowCount()):

            for j in range(self.tabla.columnCount()):

                valor_celda = self.tabla.item(i, j)
                matriz[i][j] = float(valor_celda.text())


        return matriz

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # escribir ruta donnde empezara a buscar
        ruta = os.getcwd().replace("\simulacion","")
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()",  ruta,"Txt (*.txt)", options=options)
        if fileName:
            print(fileName)


if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    app = QApplication(sys.argv)
    ventana = Ventana_datos_abastecimiento()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()