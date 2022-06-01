from pathlib import Path
import os
import sys
import  numpy as np
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication,  QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes #getSystemMetr
from interfaces.codigo.Manejo_archivos import Manejo_archivos
from interfaces.ventanas_produccion.ventana_datos_personal import Ventana_datos_personal
from interfaces.codigo.seccion_producción import funciones_produccion

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
        self.funcionesProduccion = funciones_produccion()
        self.opciones()

        
       #conectar botones
        self.btnmas.clicked.connect(lambda :self.agregar_filas(self.tabla))
        self.btnmenos.clicked.connect(lambda :self.eliminar_filas(self.tabla))
        self.tablas_opcion.activated.connect(self.opciones)
        self.Guardar.clicked.connect(self.guardar_datos)
        self.btndatos.clicked.connect(self.Guardar_file)
        self.btncargar.clicked.connect(self.open_file)
        self.llenar.clicked.connect(self.llamar_tablas)
        self.btniniciar.clicked.connect(self.iniciar_simulacion)

        

    def opciones(self):
        # en base a la opcion escogida se desata una accion
        
        self.limpiar_tabla(self.tabla)
        self.llenar.hide()
        self.Guardar.show()

        if(self.tablas_opcion.currentIndex() == 0):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de cocción en horas', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.colocar_datos_tablas()

        elif(self.tablas_opcion.currentIndex() == 1):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Costo de molino en horas', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            self.llenar.show()
            self.Guardar.hide()
            

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
            self.tabla.setHorizontalHeaderLabels (['Costo de embotellado y almacenaje', 'Probabilidad'])
            header1 = self.tabla.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            self.llenar.show()
            self.Guardar.hide()
        

        elif(self.tablas_opcion.currentIndex() == 5):

            self.tabla.setColumnCount(2)
            self.tabla.setHorizontalHeaderLabels (['Tiempo de reposo en años', 'Probabilidad'])
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
        numero_tablas = 3
        trabajadores  = 3
        nombre_opcion = self.tablas_opcion.currentText()

        if(nombre_opcion == "Tiempo de molino" or nombre_opcion == "Embotellado y almacenaje"):
            for i in range(numero_tablas):
                
                #como uso un dialow puedo usar un exce_ para oque me retorne un valor cuando se cierre la ventana
                self.hide()
                self.ex = Ventana_datos_personal(self,nombre_opcion,trabajadores)
                valor = self.ex.exec_()
                

                trabajadores += 1

    def iniciar_simulacion(self):
        # inicia los hilos con lps datos de las tablas

        iteraciones = self.iteraciones.text()
        nomina = self.nomina.text()
        costo_horno = self.costo_horno.text()
        costo_embotellado = self.costoembotellado.text()
        costo_molino = self.costo_molino.text()

        if(iteraciones != "" and self.has_numbers(iteraciones) and nomina != "" and self.has_numbers(nomina) and costo_horno != "" and self.has_numbers(costo_horno) and costo_embotellado != "" and self.has_numbers(costo_embotellado)):

            matriz1, numeroFilas1 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", 'Tiempo de cocción en horas',3)

            matriz_trabajadoresMolino_3, numeroFilas_trabajadoresMolino3 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Tiempo de molino Tiempo de 3 trabajadores en horas",3)
            matriz_trabajadoresMolino_4, numeroFilas_trabajadoresMolino4 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Tiempo de molino Tiempo de 4 trabajadores en horas",3)
            matriz_trabajadoresMolino_5, numeroFilas_trabajadoresMolino5 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Tiempo de molino Tiempo de 5 trabajadores en horas",3)

            matriz3, numeroFilas3 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", 'Tiempo de fermentación en días',3)
            matriz4, numeroFilas4 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", 'Tiempo de graduación del mezcal en minutos',3)

            matriz_trabajadoresEmbotellado_3, numeroFilas_trabajadoresEmbotellado3 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Embotellado y almacenaje Tiempo de 3 trabajadores en horas",3)
            matriz_trabajadoresEmbotellado_4, numeroFilas_trabajadoresEmbotellado4 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Embotellado y almacenaje Tiempo de 4 trabajadores en horas",3)
            matriz_trabajadoresEmbotellado_5, numeroFilas_trabajadoresEmbotellado5 = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", "Embotellado y almacenaje Tiempo de 5 trabajadores en horas",3)

        
            lista_coccion = [matriz1,numeroFilas1,3]

            trabajadoresMolino_3 = [matriz_trabajadoresMolino_3, numeroFilas_trabajadoresMolino3,3]
            trabajadoresMolino_4 = [matriz_trabajadoresMolino_4, numeroFilas_trabajadoresMolino4,3]
            trabajadoresMolino_5 = [matriz_trabajadoresMolino_5, numeroFilas_trabajadoresMolino5,3]

            lista_fermentacion = [matriz3,numeroFilas3,3]
            lista_graduacion = [matriz4,numeroFilas4,3]

            trabajadoresEmbotellado_3 = [matriz_trabajadoresEmbotellado_3, numeroFilas_trabajadoresEmbotellado3,3]
            trabajadoresEmbotellado_4 = [matriz_trabajadoresEmbotellado_4, numeroFilas_trabajadoresEmbotellado4,3]
            trabajadoresEmbotellado_5 = [matriz_trabajadoresEmbotellado_5, numeroFilas_trabajadoresEmbotellado5,3]

            matriz_reposo, numeroFilas_reposo = self.manejo_archivos.leer("base_datos/Datos_produccion.txt", 'Tiempo de reposo en años',3)
            lista_reposo = [matriz_reposo,numeroFilas_reposo,3]
           
            
            

            try:
                nombre_archivo = self.funcionesProduccion.iniciar_hilos(lista_coccion,trabajadoresMolino_3,trabajadoresMolino_4, trabajadoresMolino_5, lista_fermentacion,lista_graduacion,
                                                                    lista_reposo,trabajadoresEmbotellado_3, trabajadoresEmbotellado_4, trabajadoresEmbotellado_5,int(iteraciones), float(nomina),
                                                                    float(costo_horno),float(costo_molino),float(costo_embotellado))
          

                ruta = str(os.path.join(Path.home(), "Downloads"))  + "/" + nombre_archivo

                if(os.path.exists(ruta)):
                    QMessageBox.information(self, "Felicidades", "El reporte se ha generados exitosamente", QMessageBox.Discard)

                else:
                    QMessageBox().critical(self, "Error", "No se pudo generar archivo", QMessageBox.Discard)

            except Exception as e:

                QMessageBox().critical(self, "Error", "No se pudo generar archivo", QMessageBox.Discard)
                print(e)



        else:

            QMessageBox().critical(self, "Error", "Debe colocar un numero de semanas y el costos de nomina", QMessageBox.Discard)

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