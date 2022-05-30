import os
import sys
import  numpy as np
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from interfaces.codigo.Manejo_archivos import Manejo_archivos
from interfaces.ventanas_produccion.ventana_datos_personal import Ventana_datos_personal

class Ventana_datos_produccion(QDialog):

    def __init__(self, ventana_principal):

        self.ventana_principal = ventana_principal

        QDialog.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("interfaces/ventanas_produccion/Ingreso_datos_produccion.ui", self)

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
        self.tablas_opcion.activated.connect(self.opciones)
        self.Guardar.clicked.connect(self.guardar_datos)
        self.btndatos.clicked.connect(self.Guardar_file)
        self.btncargar.clicked.connect(self.open_file)
        self.llenar.clicked.connect(self.llamar_tablas)

    def opciones(self):
        # en base a la opcion escogida se desata una accion
        
        self.limpiar_tabla(self.tabla)

        if(self.tablas_opcion.currentIndex() == 0):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de cocción en horas', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        elif(self.tablas_opcion.currentIndex() == 1):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo en horas', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        elif(self.tablas_opcion.currentIndex() == 2):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de fermentación en días', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        elif(self.tablas_opcion.currentIndex() == 3):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de graduación del mezcal en minutos', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        elif(self.tablas_opcion.currentIndex() == 4):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de embotellado y almacenaje en minutos', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()
        


   
    def colocar_datos_tablas(self):
        # si hay datos en la ase de datos de la tabla seleccionada los trae de regreso
        nombre_tabla = self.tabla.horizontalHeaderItem(0).text() 

        matriz, numero_filas = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", nombre_tabla,self.tabla.columnCount())

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
        
        nombre_tabla = self.tabla.horizontalHeaderItem(0).text() 


        if(numero_filas == 0 ):

            QMessageBox.warning(self, "Advertencia", "Debe colocar datos en la tabla", QMessageBox.Discard)
        else:
            m1, n1 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", nombre_tabla,self.tabla.columnCount()+1)

            if(n1 != False):
                self.manejo_archivos.eliminar("base_datos/Datos_produccion.txt",nombre_tabla,numero_columnas)

            self.manejo_archivos.escribrir("base_datos/Datos_produccion.txt",nombre_tabla,matriz1,numero_filas,numero_columnas)

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

        numero_filas = tabla.rowCount()
        numero_columnas = tabla.columnCount()+1
        nombre_tabla = tabla.horizontalHeaderItem(0).text() 

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

        except ValueError: 
            QMessageBox().critical(self, "Error", "Debe colocar datos numericos en la tabla ", QMessageBox.Discard)
            numero_filas = 0

        return matriz, numero_columnas, numero_filas


    def open_file(self):
        # abre el archivo con datos de una simulacion anterior para cargarlos al nuevo
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","file","Txt (*.txt)")

        archivo = "base_datos/Datos_produccion.txt"
        try:
            if(os.stat(fileName).st_size != 0 and fileName ):

                with open(fileName, "r") as file:
                    lineas = file.readlines()

                with open(archivo, "w") as file:
                    for i in lineas:
                        file.write(i)

                self.opciones()
                QMessageBox.information(self, "Felicidades", "han sido recuperados con exito", QMessageBox.Discard)

            else:

                QMessageBox.warning(self, "Ups!!!", "Actualemten no hay datos que se puedan guardar", QMessageBox.Discard)
        except FileNotFoundError as e:

            QMessageBox().critical(self, "Error", "no se pudo econtrar el archivo", QMessageBox.Discard)

    def Guardar_file(self):
        # guarda con el nombre que le dio el usuario el archivo con los datos dentro
        save_as = QFileDialog.getSaveFileName(self, "Save as...", '', "Txt (*.txt)")[0]
        archivo = "base_datos/Datos_produccion.txt"
        try:
            if(os.stat(archivo).st_size != 0 and save_as ):

                with open(archivo, "r") as file:
                    lineas = file.readlines()

                with open(save_as, "w") as file:
                    for i in lineas:
                        file.write(i)

                QMessageBox.information(self, "Guardar", "Los datos de esta simulacion se han guardado exitosamente", QMessageBox.Discard)

            else:

                QMessageBox.warning(self, "Ups!!!", "Actualemten no hay datos que se puedan guardar", QMessageBox.Discard)

        except FileNotFoundError as e:

            QMessageBox().critical(self, "Error", "no se pudo guardar el archivo", QMessageBox.Discard)
            
    def has_numbers(self,inputString):
        # te devuelve si existe algun numero en el string
        return any(char.isdigit() for char in inputString)


    def llamar_tablas(self):
        # llama a las tablas de personal para que se le inserten datos
        numero_tablas = int(self.numeroPersonal.text())
        trabajadores  = 3
        nombre_opcion = self.tablas_opcion.currentText()

        if(nombre_opcion == "Tiempo de molino" or nombre_opcion == "Embotellado y almacenaje"):
            for i in range(numero_tablas):
                
                #como uso un dialow puedo usar un exce_ para oque me retorne un valor cuando se cierre la ventana
                self.hide()
                self.ex = Ventana_datos_personal(self,nombre_opcion,trabajadores)
                valor = self.ex.exec_()
                

                trabajadores += 1

        

        

    def closeEvent(self, event):

        self.ventana_principal.show()
        
if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    #app = QApplication(sys.argv)
    #ventana = Ventana_datos_ventas()
    #ventana.show()
    #ejecutar la aplicacion
    #app.exec_()

    """
    para que la primeara columna se estire pero las demas se adapten al contenido
    de esta manera se llena el esoacio de la tabla
    header = self.table.horizontalHeader()       
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    """