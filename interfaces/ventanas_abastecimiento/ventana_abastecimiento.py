
import os
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from interfaces.codigo.Manejo_archivos import Manejo_archivos
import numpy as np

class Ventana_datos_abastecimiento(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

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
        # instancias de clases necesarias
        self.manejo_archivos = Manejo_archivos()

        self.opciones()
        
        #conectar botones
        self.btnmas.clicked.connect(lambda :self.agregar_filas(self.tabla))
        self.btnmenos.clicked.connect(lambda :self.eliminar_filas(self.tabla))
        self.btnmas2.clicked.connect(lambda :self.agregar_filas(self.tabla2))
        self.btnmenos2.clicked.connect(lambda :self.eliminar_filas(self.tabla2))
        self.tablas_opcion.activated.connect(self.opciones)#cambia la tabla deacuerdo a la opcion seleccionada
        self.Guardar.clicked.connect(self.guardar_datos)

    def opciones(self):
        # en base a la opcion escogida se desata una accion
        self.limpiar_tabla(self.tabla)
        self.limpiar_tabla(self.tabla2)
        
        if(self.tablas_opcion.currentIndex() == 0):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada piñas en días', 'Probabilidad'])
            
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio piñas', 'Probabilidad'])
            
            self.tabla.resizeColumnsToContents()
            self.tabla2.resizeColumnsToContents()
            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        
        elif(self.tablas_opcion.currentIndex() == 1):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada botellas de vidrio en días', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de botellas de vidrio en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()


        elif(self.tablas_opcion.currentIndex() == 2):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada botellas de plastico en días', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de botellas de plastico en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        elif(self.tablas_opcion.currentIndex() == 3):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada tapones y corchos en días', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de tapones y corchos en días', 'Probabilidad'])

            #para que las columnas se repartan el espacio de la tabla y la llenen
            header1 = self.tabla.horizontalHeader()       
            header2 = self.tabla2.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

    def colocar_datos_tablas(self):
        # si hay datos en la ase de datos de la tabla seleccionada los trae de regreso
        nombre_tabla = self.tabla.horizontalHeaderItem(0).text() 
        nombre_tabla2 = self.tabla2.horizontalHeaderItem(0).text() 

        matriz, numero_filas = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla,self.tabla.columnCount())
        matriz2, numero_filas2 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla2,self.tabla2.columnCount())

        if(numero_filas != False):
            self.agregar_datos_tabla(self.tabla,numero_filas,matriz)

        if(numero_filas2 != False):
            self.agregar_datos_tabla(self.tabla2,numero_filas2,matriz2)


    def agregar_datos_tabla(self, tabla, numero_filas, matriz):
        # rellena las columnas con los datos dados
        tabla.setRowCount(numero_filas)
        for i in range(numero_filas):
            tabla.setItem(i,0, QtWidgets.QTableWidgetItem(str(matriz[i][0])))
            tabla.setItem(i,1, QtWidgets.QTableWidgetItem(str(matriz[i][1])))
            


    def guardar_datos(self):

        # informacion de la tabla
        matriz1, numero_columnas, numero_filas  = self.tomar_valores_tabla(self.tabla)
        matriz2, numero_columnas2, numero_filas2  = self.tomar_valores_tabla(self.tabla2)

        
        nombre_tabla = self.tabla.horizontalHeaderItem(0).text() 
        nombre_tabla2 = self.tabla2.horizontalHeaderItem(0).text() 

        filas1 = self.tabla.rowCount()
        filas2 = self.tabla2.rowCount()

        if(filas1 == 0 or filas2 == 0):

            QMessageBox.warning(self, "Advertencia", "Debe colocar datos en ambas tablas", QMessageBox.Discard)
        else:
            m1, n1 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla,self.tabla.columnCount())
            m2, n2 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla2,self.tabla2.columnCount())

            if(n1 != False):
                self.manejo_archivos.eliminar("base_datos/Datos_abastecimiento.txt",nombre_tabla,numero_columnas)

            if(n2 != False):
                self.manejo_archivos.eliminar("base_datos/Datos_abastecimiento.txt",nombre_tabla2,numero_columnas2)

            self.manejo_archivos.escribrir("base_datos/Datos_abastecimiento.txt",nombre_tabla,matriz1,numero_filas,numero_columnas)
            self.manejo_archivos.escribrir("base_datos/Datos_abastecimiento.txt",nombre_tabla2,matriz2,numero_filas2,numero_columnas2)

            QMessageBox.information(self, "Guardar", "Los datos se han guardado exitosamente", QMessageBox.Discard)
        
    def limpiar_tabla(self, tabla):
        # elimina todos los datos que se enucntren el la tabla
        for i in range(tabla.rowCount()):

            self.eliminar_filas(tabla)

    def agregar_filas(self, nombre_tabla):

        posicion_fila = nombre_tabla.rowCount()
        nombre_tabla.insertRow(posicion_fila)

    def eliminar_filas(self, nombre_tabla):

        posicion_fila = nombre_tabla.rowCount()
        nombre_tabla.removeRow(posicion_fila-1)


    def tomar_valores_tabla(self, tabla):

        matriz = np.zeros((tabla.rowCount(),tabla.columnCount()))
        
        for i in range(tabla.rowCount()):

            for j in range(tabla.columnCount()):

                valor_celda = tabla.item(i, j)
                matriz[i][j] = float(valor_celda.text())


        return matriz, tabla.columnCount(),tabla.rowCount()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # escribir ruta donnde empezara a buscar
        ruta = os.getcwd().replace("\simulacion","")
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()",  ruta,"Txt (*.txt)", options=options)
        if fileName:
            print(fileName)

    def closeEvent(self, event):

        self.ventana_principal.show()
        

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    app = QApplication(sys.argv)
    ventana = Ventana_datos_abastecimiento()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()