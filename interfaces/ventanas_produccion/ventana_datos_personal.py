import numpy as np
import os
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from interfaces.codigo.Manejo_archivos import Manejo_archivos


class Ventana_datos_personal(QDialog):

    def __init__(self, ventana_principal, nombre_opcion, numero_trabajadores):

        self.ventana_principal = ventana_principal
        self.nombre_opcion = nombre_opcion
        self.numero_trabajadores = numero_trabajadores



        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("interfaces/ventanas_produccion/ingreso_datos_personal.ui", self)

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

        self.titulo.setText(nombre_opcion + f" para {self.numero_trabajadores} numero de trabajadores")
        self.titulo.adjustSize()
        
       #conectar botones
        self.btnmas.clicked.connect(lambda :self.agregar_filas(self.tabla))
        self.btnmenos.clicked.connect(lambda :self.eliminar_filas(self.tabla))
        self.Guardar.clicked.connect(self.guardar_datos)

    def opciones(self):
        # en base a la opcion escogida se desata una accion
     

        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels ([f'Tiempo de {self.numero_trabajadores} trabajadores' , 'Probabilidad'])

        header1 = self.tabla.horizontalHeader()
        header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.colocar_datos_tablas()

    def colocar_datos_tablas(self):
        # si hay datos en la ase de datos de la tabla seleccionada los trae de regreso
        nombre_tabla = self.nombre_opcion + " " + self.tabla.horizontalHeaderItem(0).text()

        matriz, numero_filas = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", nombre_tabla,self.tabla.columnCount()+1)

        if(numero_filas != False):
            self.agregar_datos_tabla(self.tabla,numero_filas,matriz)


    def agregar_datos_tabla(self, tabla, numero_filas, matriz):
        # rellena las columnas con los datos dados
        tabla.setRowCount(numero_filas)
        
        for i in range(numero_filas):

            for j in range(tabla.columnCount()):

                tabla.setItem(i,j, QtWidgets.QTableWidgetItem(str(matriz[i][j])))
            


    def guardar_datos(self):

        # informacion de la tabla
        matriz1, numero_columnas, numero_filas  = self.tomar_valores_tabla(self.tabla)
        
        nombre_tabla = self.nombre_opcion + " " + self.tabla.horizontalHeaderItem(0).text()


        if(numero_filas == 0 ):

            QMessageBox.warning(self, "Advertencia", "Debe colocar datos en la tabla", QMessageBox.Discard)
        else:
            m1, n1 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", nombre_tabla,self.tabla.columnCount()+1)

            if(n1 != False):
                self.manejo_archivos.eliminar("base_datos/Datos_produccion.txt",nombre_tabla,numero_columnas)

            self.manejo_archivos.escribrir("base_datos/Datos_produccion.txt",nombre_tabla,matriz1,numero_filas,numero_columnas)

            QMessageBox.information(self, "Guardar", "Los datos se han guardado exitosamente", QMessageBox.Discard)

            self.close()
        

        
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

        numero_filas = tabla.rowCount()
        numero_columnas = tabla.columnCount()+1

        matriz = [ [0]*numero_columnas for _ in range(numero_filas)]
        try:
            for i in range(numero_filas):

                for j in range(numero_columnas-1):

                    celda = tabla.item(i, j)
                    valor = celda.text().strip()

                    if(self.has_numbers(valor)):

                        matriz[i][j] = float(valor)
                    else:
                        raise  AttributeError

        except AttributeError as e:
            QMessageBox().critical(self, "Error", "Debe colocar datos numericos en la tabla ", QMessageBox.Discard)
            numero_filas = 0

        return matriz, numero_columnas, numero_filas




            
    def has_numbers(self,inputString):
        # te devuelve si existe algun numero en el string
        return any(char.isdigit() for char in inputString)




    def closeEvent(self, event):

        self.ventana_principal.show()