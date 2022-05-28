from threading import *
import numpy as np
from sympy import false

#Importacion del las clases necesarias para la venta mediante herencia
from Ventas import Ventas

class funciones_ventas(Ventas): 
    def llegada_clientes(self):
        

    def estancia_clientes(self):
        pass

    def venta_botellas(self):
        
        matriz_contador, ganancias = self.proceso_alcohol(matriz)

    def iniciar_hilos(self):
        
        hilo_llegada = Thread(target=self.llegada_clientes,name="Hilo_llegada_clientes",args=())

        hilo_estancia = Thread(target=self.estancia_clientes,name="Hilo_estancia_clientes",args=())

        hilo_venta = Thread(target=self.venta_botellas,name="Hilo_venta_botellas",args=())

        #Inicializar los hilos
        hilo_llegada.start()
        hilo_estancia.start()
        hilo_venta.start()

        