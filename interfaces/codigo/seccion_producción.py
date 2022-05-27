from threading import *
import numpy as np

#Importacion de los archivos necesarios
from Abastecimiento import Abastecimiento

class funciones_producción(Abastecimiento):
    # Hilo que se encarga de la coccion en el honro
    def metodo_hornos(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio, tiempo_minimo, tiempo_maximo = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        #Obtencion de los registros de nominas
        costo_promedio, costo_minimo, costo_maximo, costo_total = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo realizo la iteracion")
    # Hilo que se encarga de controlar la molida 
    def metodo_molinos(self,matriz, numero_filas,numero_columnas,numero_iteraciones):
        pass
    
    # Hilo que se encarga de controlar la fermentacion
    def metodo_fermentacion(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        pass
    
    # Hilo que se encarga de controlar la graduacion del mezcal
    def metodo_graduacion(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        pass
    
    # Hilo que se encarga del reposo del mezcal
    def metodo_reposo(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        pass

    # Hilo que se encarga de controlar el embotellamiento
    def metodo_embotellado(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        pass

    #Funcion que inicializa los hilos
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
        hilo_horno = Thread(target=self.metodo_hornos, name="Hilo_Hornos", args=(matriz,numerofilas,numerocolumnas,10))

        #hilo_molino = Thread(target=self.metodo_molinos, name="Hilo_Molinos", args=())

        #hilo_fermentacion = Thread(target=self.metodo_fermentacion, name="Hilo_Fermentacion", args=())

        #hilo_graduacion = Thread(target=self.metodo_graduacion, name="Hilo_Graduacion", args=())
        
        #hilo_reposo = Thread(target=self.metodo_reposo, name="Hilo_Reposo", args=())

        #hilo_embotellado = Thread(target=self.metodo_embotellado, name="Hilo_Embotellado", args=())

        #Inicializacion de todos los procesos de la simulacion
        hilo_horno.start()
        #hilo_molino.start()
        #hilo_fermentacion.start()
        #hilo_graduacion.start()
        #hilo_reposo.start()
        #hilo_embotellado.start()

if __name__ == "__main__":
    funciones_producción().iniciar_hilos()