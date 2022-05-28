from threading import *
import numpy as np

#Importación de los archivos necesarios
from Abastecimiento import Abastecimiento

class funciones_abastecimiento(Abastecimiento):
    #Creacion del hilo para los suministros de piñas
    def pinas(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_pinas, tiempo_maximo_pinas, tiempo_minimo_pinas =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_pinas, costo_maximo_pinas, costo_minimo_pinas = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

    def botellas_vidrio(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_bv, tiempo_maximo_bv, tiempo_minimo_bv =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_bv, costo_maximo_bv, costo_minimo_bv= self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

    def tapones_corchos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_corchos, tiempo_maximo_corchos, tiempo_minimo_corchos =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_corchos, costo_maximo_corchos, costo_minimo_corchos = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

    def botellas_pet(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_bp, tiempo_maximo_bp, tiempo_minimo_bp =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_bp, costo_maximo_bp, costo_minimo_bp = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

    def etiquetas_sellos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_sellos, tiempo_maximo_sellos, tiempo_minimo_sellos =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_sellos, costo_maximo_sellos, costo_minimo_sellos = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

    def iniciar_hilos(self):
        numerofilas, numerocolumnas = 3,3
    
        matriz = np.zeros((numerofilas,numerocolumnas))

        matriz[0][0] = 2
        matriz[0][1] = 0.3

        matriz[1][0] = 5
        matriz[1][1] = 0.5

        matriz[2][0] = 8
        matriz[2][1] = 0.2

        #Creacion de los hilos para las funciones anteriormente creadas

        hilo_pinas = Thread(target=self.pinas, name="Hilo_pinas",args=(matriz,numerofilas,numerocolumnas,10))

        hilo_botellas_vidrio = Thread(target=self.botellas_vidrio,name="Hilo_botellas_vidiro",args=(matriz,numerofilas,numerocolumnas,10))

        hilo_tapones_corcho = Thread(target=self.tapones_corchos,name="Hilo_tapones",args=(matriz,numerofilas,numerocolumnas,10))

        hilo_botellas_pet = Thread(target=self.botellas_pet,name="Hilo_botellas_pet",args=(matriz,numerofilas,numerocolumnas,10))

        hilo_etiquetas = Thread(target=self.etiquetas_sellos,name="Hilo_etiquetas",args=(matriz,numerofilas,numerocolumnas,10))

        #Inicialización de los hilos
        hilo_pinas.start()
        hilo_botellas_vidrio.start()
        hilo_tapones_corcho.start()
        hilo_botellas_pet.start()
        hilo_etiquetas.start()