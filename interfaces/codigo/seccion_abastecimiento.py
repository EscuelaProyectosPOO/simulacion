from threading import *
import numpy as np

#Importación de los archivos necesarios
from Abastecimiento import Abastecimiento

class funciones_abastecimiento(Abastecimiento):
    #Creacion del hilo para los suministros de piñas
    def pinas(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        pass

    def botellas_vidrio(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        pass

    def tapones_corchos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        pass

    def botellas_pet(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        pass

    def etiquetas_sellos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        pass

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