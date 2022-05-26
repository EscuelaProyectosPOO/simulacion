from matplotlib.pyplot import pink
import numpy as np
import os

class Manejo_archivos():

    def crear_archivo(self,nombre_archivo):
        #crea el archivo con el nomre y la ruta dados
        with open(nombre_archivo,"w") as file:
            file.close()


    def escribrir(self,nombre_archivo, nombre_tabla, matriz, numero_filas,numero_columnas):
        # escribe los datos de la tabla, usando como identifiacador el nombre de la tabla

        identificador = nombre_tabla + "," + str(numero_columnas)
        linea = self.convertir_datos(matriz, numero_filas, numero_columnas)

        with open(nombre_archivo,"a") as file:
            file.write(identificador)
            file.write(linea)

    def eliminar(self,nombre_archivo,nombre_tabla, numero_columnas):
        # elimina los datos de esa tabla en especifico en el documento

        with open(nombre_archivo,"r") as file:
            lineas = file.readlines()

        lineas_nuevas = self.informacion_nueva(lineas, nombre_tabla, numero_columnas)

        if(self.eliminar_archivo(nombre_archivo)):

            with open(nombre_archivo,"w") as file:

                for i in lineas_nuevas:

                    file.write(i)

    def leer(self, nombre_archivo ,nombre_tabla, numero_columnas):
        # lee los datos de la tabla correspondiente y los regresa en forma de matriz 
        with open(nombre_archivo,"r") as file:
            lineas = file.readlines()

        informacion_tabla = self.informacion_vieja(lineas,nombre_tabla,numero_columnas)
        
        if(len(informacion_tabla) == 0 or len(informacion_tabla) == 1 ):

            return 0, False

        else:

            matriz, numero_filas = self.convertir_datos_matriz(informacion_tabla,numero_columnas)

            return matriz, numero_filas

       


    def informacion_nueva(self, lineas,nombre_tabla, numero_columnas):
        # elimina la informacion de la tabla y deja la informacion que ocupamos en las lista
        contador = 0
        lista_nueva = []

        while(contador < len(lineas)):
            
            linea = lineas[contador]
            datos_linea = linea.split(",")

            if nombre_tabla in datos_linea :
                
                lista_nueva = lineas[:contador] + lineas[(contador +numero_columnas+1) :]

                break

            contador +=1
            

        return lista_nueva


    def informacion_vieja(self, lineas,nombre_tabla, numero_columnas):
        # obtiene los datos de la tabla elegida y los retorna
        contador = 0
        lista_nueva = []

        while(contador < len(lineas)):
            
            linea = lineas[contador]
            datos_linea = linea.split(",")

            if nombre_tabla in datos_linea :
                
                lista_nueva = lineas[contador:(contador +numero_columnas+1)] 
                break

            contador +=1
        

        return lista_nueva



    def eliminar_archivo(self, nombre_archivo):
        #elimina el documento entero
        if(os.path.exists(nombre_archivo)):
            os.remove(nombre_archivo)

            return True

        else:

            return False
            



    def convertir_datos(self, matriz, numero_filas, numero_columnas):
        # convierte los datos de la matriz en lineas para insertar en el documento
        
        linea = "\n"
        
        for i in range(numero_columnas):
            separador = ","
            for j in range(numero_filas):

                if(j == numero_filas-1):
                    separador = ""

                linea += str(matriz[j][i])+ separador

            linea += "\n"


        return linea

    def convertir_datos_matriz(self, lineas, numero_columnas):
        # te da la informacion de la tabla y las convierte en una matriz con datos numericos en forma de string para que se pongan los datos
        numero_filas = len(lineas[1].split(","))
        lineas = lineas[1:]

        matriz = np.zeros((numero_filas, numero_columnas))

        for i in range(0,numero_columnas):

            linea = lineas[i].replace(",", " ")
            datos = linea.split(" ")

            for j in range(numero_filas):

                
               
                matriz[j][i] = float(datos[j])

        return matriz, numero_filas

            








if(__name__== "__main__"):
    m = Manejo_archivos()
   
    matriz = np.zeros((3,3))

    matriz[0][0] = 2
    matriz[0][1] = 0.3

    matriz[1][0] = 5
    matriz[1][1] = 0.5

    matriz[2][0] = 8
    matriz[2][1] = 0.2

    #print(matriz)
    #m.crear_archivo("base_datos/topos.txt")
    #m.escribrir("base_datos/topos.txt","Produccion2",matriz,3,3)
    #m.eliminar("base_datos/topos.txt", "Ventas_pinas2",3)
    m.leer("base_datos/topos.txt", "Produccion2",3)
   
