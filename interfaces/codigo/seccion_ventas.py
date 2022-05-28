from threading import *
import numpy as np
from sympy import false

#Importacion del las clases necesarias para la venta mediante herencia
from Ventas import Ventas

class funciones_ventas(Ventas): 
    def llegada_clientes(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        #Funcion que contabiliza el tiempo de llegada de los clientes
        tiempo_promedio_llegada, tiempo_maximo_llegada, tiempo_minimo_llegada = self.proceso_tiempo(matriz,numero_filas,numero_columnas,numero_iteraciones)

    def estancia_clientes(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        #Funcion que contabiliza el tiempo de estancia de los clientes
        tiempo_promedio_estancia, tiempo_maximo_estancia, tiempo_minimo_estancia = self.proceso_tiempo(matriz,numero_filas,numero_columnas,numero_iteraciones)

    def venta_botellas(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        
        matriz_contador, ganancias = self.proceso_alcohol(matriz,numero_filas,numero_columnas,numero_iteraciones)

    def iniciar_hilos(self):
        #Valores iniciales para los parametros de los hilos
        numero_filas_llegada = self.numero_filas_llegada
        numero_columnas_llegada = self.numero_columnas_llegada
        numero_iteraciones_llegada = self.numero_iteraciones_llegada

        numero_filas_estancia = self.numero_filas_estancia
        numero_columnas_estancia = self.numero_columnas_estancia
        numero_iteraciones_estancia = self.numero_iteraciones_estancia

        numero_filas_venta = self.numero_filas_venta
        numero_columnas_venta = self.numero_columnas_venta
        numero_iteraciones_venta = self.numero_iteraciones_venta
        
        matriz_llegada = np.zeros((self.numero_filas,self.numero_columnas))
        matriz_estancia = np.zeros((self.numero_filas,self.numero_columnas))
        matriz_botellas = np.zeros((self.numero_filas,self.numero_columnas))
        
        hilo_llegada = Thread(target=self.llegada_clientes,name="Hilo_llegada_clientes",args=(matriz_llegada,numero_filas_llegada,numero_columnas_llegada,numero_iteraciones_llegada))

        hilo_estancia = Thread(target=self.estancia_clientes,name="Hilo_estancia_clientes",args=(matriz_estancia,numero_filas_estancia,numero_columnas_estancia,numero_iteraciones_estancia))

        hilo_venta = Thread(target=self.venta_botellas,name="Hilo_venta_botellas",args=(matriz_botellas,numero_filas_venta,numero_columnas_venta,numero_iteraciones_venta))

        #Inicializar los hilos
        hilo_llegada.start()
        hilo_estancia.start()
        hilo_venta.start()

        