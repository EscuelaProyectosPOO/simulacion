from pathlib import Path
import os
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from interfaces.codigo.Manejo_archivos import Manejo_archivos
from interfaces.codigo.seccion_abastecimiento import funciones_abastecimiento
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
        self.funcionesAbastecimiento = funciones_abastecimiento()

        self.opciones()

        
        #conectar botones
        self.btnmas.clicked.connect(lambda :self.agregar_filas(self.tabla))
        self.btnmenos.clicked.connect(lambda :self.eliminar_filas(self.tabla))
        self.btnmas2.clicked.connect(lambda :self.agregar_filas(self.tabla2))
        self.btnmenos2.clicked.connect(lambda :self.eliminar_filas(self.tabla2))
        self.tablas_opcion.activated.connect(self.opciones)#cambia la tabla deacuerdo a la opcion seleccionada
        self.Guardar.clicked.connect(self.guardar_datos)
        self.btndatos.clicked.connect(self.Guardar_file)
        self.btncargar.clicked.connect(self.open_file)
        self.btniniciar.clicked.connect(self.iniciar_simulacion)

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

        elif(self.tablas_opcion.currentIndex() == 4):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de llegada etiquetas y sellos en días', 'Probabilidad'])
            self.tabla2.setColumnCount(2)
            self.tabla2.setHorizontalHeaderLabels (['Costo de envio de etiquetas y sellos en días', 'Probabilidad'])

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

        matriz, numero_filas = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla,self.tabla.columnCount()+1)
        matriz2, numero_filas2 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla2,self.tabla2.columnCount()+1)
        
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

       

        
        nombre_tabla = self.tabla.horizontalHeaderItem(0).text() 
        nombre_tabla2 = self.tabla2.horizontalHeaderItem(0).text() 

    
        # informacion de la tabla
        matriz1, numero_columnas, numero_filas  = self.tomar_valores_tabla(self.tabla)
        matriz2, numero_columnas2, numero_filas2  = self.tomar_valores_tabla(self.tabla2)

        
        if(numero_filas > 0 and numero_filas2 > 0):

            m1, n1 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla,self.tabla.columnCount()+1)
            m2, n2 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", nombre_tabla2,self.tabla2.columnCount()+1)

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
        numero_filas = tabla.rowCount()
        numero_columnas = tabla.columnCount()+1
        nombre_tabla = tabla.horizontalHeaderItem(0).text() 
        probabilidad_total = 0

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

                probabilidad_total += matriz[i][1]

        except AttributeError as e:
            QMessageBox().critical(self, "Error", "Debe colocar datos numericos en la tabla "+ nombre_tabla, QMessageBox.Discard)
            numero_filas = 0

       
        if(probabilidad_total >= 0.98 and probabilidad_total <= 1):

            return matriz, numero_columnas, numero_filas

        else:
            QMessageBox().critical(self, "Error", "La suma de todas las probabilidades debe sumar 1 en la tabla " + nombre_tabla, QMessageBox.Discard)
            return matriz, numero_columnas, 0
            
    def open_file(self):
        # abre el archivo con datos de una simulacion anterior para cargarlos al nuevo
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","file","Txt (*.txt)")

        archivo = "base_datos/Datos_abastecimiento.txt"

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
        archivo = "base_datos/Datos_abastecimiento.txt"
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
            


    def closeEvent(self, event):

        self.ventana_principal.show()

    def has_numbers(self,inputString):
        # te devuelve si existe algun numero en el string
        return any(char.isdigit() for char in inputString)

    def iniciar_simulacion(self):
        # inicia los hilos con lps datos de las tablas

        iteraciones = self.iteraciones.text()

        if(iteraciones != "" and self.has_numbers(iteraciones)):

            matriz1, numeroFilas1 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Tiempo de llegada piñas en días',3)
            matriz2, numeroFilas2 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Costo de envio piñas',3)

            matriz3, numeroFilas3 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Tiempo de llegada botellas de vidrio en días',3)
            matriz4, numeroFilas4 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Costo de envio de botellas de vidrio en días',3)

            matriz5, numeroFilas5 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Tiempo de llegada botellas de plastico en días',3)
            matriz6, numeroFilas6 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Costo de envio de botellas de plastico en días',3)

            matriz7, numeroFilas7 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Tiempo de llegada tapones y corchos en días',3)
            matriz8, numeroFilas8 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Costo de envio de tapones y corchos en días',3)

            matriz9, numeroFilas9 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Tiempo de llegada etiquetas y sellos en días',3)
            matriz10, numeroFilas10 = self.manejo_archivos.leer("base_datos/Datos_abastecimiento.txt", 'Costo de envio de etiquetas y sellos en días',3)
                     
            lista_pinas = [matriz1,matriz2,numeroFilas1, numeroFilas2,3,3]
           
            lista_botellas =  [matriz3,matriz4,numeroFilas3, numeroFilas4,3,3]
           
            lista_plastico =  [matriz5,matriz6,numeroFilas5, numeroFilas6,3,3]
           
           
            lista_tapones =  [matriz7,matriz8,numeroFilas7, numeroFilas8,3,3]
            
            lista_sellos =  [matriz9,matriz10,numeroFilas9, numeroFilas10,3,3]

            if(numeroFilas1 >0 and numeroFilas2 > 0 and numeroFilas3 >0 and numeroFilas4 > 0 and numeroFilas5 > 0 and numeroFilas6 > 0 and numeroFilas7 > 0 and numeroFilas8 > 0 and numeroFilas9 >0 and numeroFilas10 > 0):
                try:
                
                    nombre_archivo = self.funcionesAbastecimiento.iniciar_hilos(lista_pinas,lista_botellas,lista_tapones,lista_plastico,lista_sellos,int(iteraciones))

                    ruta = str(os.path.join(Path.home(), "Downloads"))  + "/" + nombre_archivo

                    if(os.path.exists(ruta)):
                        QMessageBox.information(self, "Felicidades", "El reporte se ha generados exitosamente", QMessageBox.Discard)

                    else:
                        QMessageBox().critical(self, "Error", "No se pudo generar archivo", QMessageBox.Discard)

                except Exception as e:

                    QMessageBox().critical(self, "Error", "No se pudo generar archivo", QMessageBox.Discard)

            else:
                QMessageBox().critical(self, "Error", "Debes llenar todas las tablas para iniciar la simulación", QMessageBox.Discard)
            
        else:

            QMessageBox().critical(self, "Error", "Debe colocar un numero de semanas", QMessageBox.Discard)
        

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicsacion
    app = QApplication(sys.argv)
    ventana = Ventana_datos_abastecimiento()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()