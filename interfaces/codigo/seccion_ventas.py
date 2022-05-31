from threading import *
import numpy as np
from sympy import false
from datetime import *

#Importacion del las clases necesarias para la venta mediante herencia
from interfaces.codigo.Ventas import Ventas
from interfaces.codigo import creaPDF
class funciones_ventas(Ventas): 
    def llegada_clientes(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        #Funcion que contabiliza el tiempo de llegada de los clientes
        tiempo_promedio_llegada, tiempo_maximo_llegada, tiempo_minimo_llegada = self.proceso_tiempo(matriz,numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_llegada, tiempo_maximo_llegada, tiempo_minimo_llegada

    def estancia_clientes(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        #Funcion que contabiliza el tiempo de estancia de los clientes
        tiempo_promedio_estancia, tiempo_maximo_estancia, tiempo_minimo_estancia = self.proceso_tiempo(matriz,numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_estancia, tiempo_maximo_estancia, tiempo_minimo_estancia

    def venta_botellas(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        
        matriz_contador, ganancias = self.proceso_alcohol(matriz,numero_filas,numero_columnas,numero_iteraciones)

        return matriz_contador, ganancias

    def iniciar_hilos(self, lista_llegada, lista_estancia, lista_ventas, numero_iteraciones):
        #Valores iniciales para los parametros de los hilos
        matriz_llegada = lista_llegada[0]
        numero_filas_llegada = lista_llegada[1]
        numero_columnas_llegada = lista_llegada[2]

        matriz_estancia = lista_estancia[0]
        numero_filas_estancia = lista_estancia[1]
        numero_columnas_estancia = lista_estancia[2]

        matriz_ventas = lista_ventas[0]
        numero_filas_ventas = lista_ventas[1]
        numero_columnas_ventas = lista_ventas[2]

        #Inicializar los hilos
        hora_min_cliente, hora_max_cliente, hora_prom_cliente = self.llegada_clientes(matriz_llegada, numero_filas_llegada, numero_columnas_llegada, numero_iteraciones)
        est_min_cliente, est_max_cliente, est_prom_cliente = self.estancia_clientes(matriz_estancia, numero_filas_estancia, numero_columnas_estancia, numero_iteraciones)
        matriz_botellas, ganancias = self.venta_botellas(matriz_ventas, numero_filas_ventas, numero_columnas_ventas, numero_iteraciones)      

        for i in matriz_botellas:
            print(i)
        
        lista_nombres = []
        for i in range(len(matriz_botellas)):
            lista_nombres.append(matriz_botellas[i][0])
        
        lista_precios = []
        for i in range(len(matriz_botellas)):
            lista_precios.append(matriz_botellas[i][1])
        
        lista_cantidad = []
        for i in range(len(matriz_botellas)):
            lista_cantidad.append(matriz_botellas[i][2])
        
        lista_ganancias = []
        for i in range(len(matriz_botellas)):
            lista_ganancias.append(matriz_botellas[i][3])
        
        #Encuentra el valor más grande en la lista de ganancias, su posicion y con el index obten el nombre de la lista_nombres e imprime las variables
        max_ganancia = max(lista_ganancias)
        pos_max_ganancia = lista_ganancias.index(max_ganancia)
        nombre_max_ganancia = lista_nombres[pos_max_ganancia]
        cantidad_botellas_max = lista_cantidad[pos_max_ganancia]
        
        #Encuentra el valor más pequeño en la lista de ganancias, su posicion y con el index obten el nombre de la lista_nombres e imprime las variables
        min_ganancia = min(lista_ganancias)
        pos_min_ganancia = lista_ganancias.index(min_ganancia)
        nombre_min_ganancia = lista_nombres[pos_min_ganancia]
        cantidad_botellas_min = lista_cantidad[pos_min_ganancia]

        #Obtener las ganacias promedio
        ganancia_promedio = sum(lista_ganancias)/len(lista_ganancias)



        #Crear el diccionario que contendrá todos los valores para la template
        diccionario = {"hora_min_ciente":hora_min_cliente,
                        "hora_max_ciente":hora_max_cliente,
                        "hora_prom_cliente":hora_prom_cliente,
                        "est_min_ciente":est_min_cliente,
                        "est_max_ciente":est_max_cliente,
                        "est_prom_cliente":est_prom_cliente,
                        "min_bot":nombre_min_ganancia,
                        "max_bot":nombre_max_ganancia,
                        "min_cant_bot":cantidad_botellas_min,
                        "max_cant_bot":cantidad_botellas_max,
                        "gan_prom":ganancia_promedio,
                        "gan_min":min_ganancia,
                        "gan_max":max_ganancia,
                        "gan_total":ganancias
    }
        
        #Crear el pdf con los valores del diccionario
        anio = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        hora = datetime.now().hour
        minuto = datetime.now().minute
        segundo = datetime.now().second
        nombre_pdf = "Reporte_ventas-"+str(anio)+"-"+str(mes)+"-"+str(dia)+"_"+str(hora)+"-"+str(minuto)+"-"+str(segundo)+".pdf"
        creaPDF.crear_pdf("C:/Users/tetil/OneDrive/Documents/simulacion/templates/template_ventas.html",diccionario,nombre_pdf)
        #creaPDF.crear_pdf("/template_producción.html",diccionario,nombre_pdf)

if __name__ == "__main__":
    matriz = [[2,0.3],[5,0.5],[8,0.2]]
    numero_filas = 3
    numero_columnas = 2
    numero_iteraciones = 10

    lista_llegada = [matriz,numero_filas,numero_columnas,numero_iteraciones]
    lista_estancia = [matriz,numero_filas,numero_columnas,numero_iteraciones]
    lista_ventas = [matriz,numero_filas,numero_columnas,numero_iteraciones]
    objeto = funciones_ventas()
    objeto.iniciar_hilos(lista_llegada, lista_estancia, lista_ventas, numero_iteraciones)