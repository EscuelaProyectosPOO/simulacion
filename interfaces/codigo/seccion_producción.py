from threading import *
import numpy as np

#Importacion de los archivos necesarios
from Abastecimiento import Abastecimiento

class funciones_producción(Abastecimiento):
    # Hilo que se encarga de la coccion en el honro
    def metodo_hornos(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_horno, tiempo_maximo_horno, tiempo_minimo_horno = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        #Obtencion de los registros de los costos de operación
        costo_promedio_horno, costo_maximo_horno, costo_minimo_horno = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo hornos realizo la iteracion")

    # Hilo que se encarga de controlar la molida 
    def metodo_molinos(self,matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_molino, tiempo_maximo_molino, tiempo_minimo_molino = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        #Obtencion de los registros de nominas
        costo_promedio_molino, costo_maximo_molino, costo_minimo_molino  = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo molinos realizo la iteracion")
    
    # Hilo que se encarga de controlar la fermentacion
    def metodo_fermentacion(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_fermentacion, tiempo_maximo_fermentacion, tiempo_minimo_fermentacion = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo fermentacion realizo la iteracion")

    # Hilo que se encarga de controlar la graduacion del mezcal
    def metodo_graduacion(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_graduacion, tiempo_maximo_graduacion, tiempo_minimo_graduacion = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo graduacion realizo la iteracion")

    # Hilo que se encarga del reposo del mezcal
    def metodo_reposo(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_reposo, tiempo_maximo_reposo, tiempo_minimo_reposo = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo reposo realizo la iteracion")

    # Hilo que se encarga de controlar el embotellamiento
    def metodo_embotellado(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_embotellado, tiempo_maximo_embotellado, tiempo_minimo_embotellado = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        #Obtencion de los registros de los costos de operación
        costo_promedio_embotellado, costo_maximo_embotellado, costo_minimo_embotellado = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        print("El hilo embotellado realizo la iteracion")

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

        hilo_molino = Thread(target=self.metodo_molinos, name="Hilo_Molinos", args=(matriz,numerofilas,numerocolumnas,10))

        hilo_fermentacion = Thread(target=self.metodo_fermentacion, name="Hilo_Fermentacion", args=(matriz,numerofilas,numerocolumnas,10))

        hilo_graduacion = Thread(target=self.metodo_graduacion, name="Hilo_Graduacion", args=(matriz,numerofilas,numerocolumnas,10))
        
        hilo_reposo = Thread(target=self.metodo_reposo, name="Hilo_Reposo", args=(matriz,numerofilas,numerocolumnas,10))

        hilo_embotellado = Thread(target=self.metodo_embotellado, name="Hilo_Embotellado", args=(matriz,numerofilas,numerocolumnas,10))

        #Inicializacion de todos los procesos de la simulacion
        hilo_horno.start()
        hilo_molino.start()
        hilo_fermentacion.start()
        hilo_graduacion.start()
        hilo_reposo.start()
        hilo_embotellado.start()

if __name__ == "__main__":
    funciones_producción().iniciar_hilos()