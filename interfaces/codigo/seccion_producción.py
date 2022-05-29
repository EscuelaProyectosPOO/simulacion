from threading import *
import numpy as np

#Importacion de los archivos necesarios
from Abastecimiento import Abastecimiento
import creaPDF

class funciones_produccion(Abastecimiento):
    # Hilo que se encarga de la coccion en el honro
    def metodo_hornos(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_horno, tiempo_maximo_horno, tiempo_minimo_horno = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        #Obtencion de los registros de los costos de operación
        costo_promedio_horno, costo_maximo_horno, costo_minimo_horno = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_horno, tiempo_maximo_horno, tiempo_minimo_horno, costo_promedio_horno, costo_maximo_horno, costo_minimo_horno

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
        #Se hará la asignación de los parametros para los hilos

        #Datos para la asignación de los hornos
        matriz_horno = []
        numero_filas_horno = 0
        numero_columnas_horno = 0
        numero_iteraciones_horno = 0

        #Datos para la asignación de los molinos
        matriz_molino_1 = []
        numero_filas_molino_1 = 0
        numero_columnas_molino_1 = 0
        numero_iteraciones_molino_1 = 0

        matriz_molino_2 = []
        numero_filas_molino_2 = 0
        numero_columnas_molino_2 = 0
        numero_iteraciones_molino_2 = 0

        matriz_molino_3 = []
        numero_filas_molino_3 = 0
        numero_columnas_molino_3 = 0
        numero_iteraciones_molino_3 = 0

        #Datos para la asignación de la fermentacion
        matriz_fermentacion = []
        numero_filas_fermentacion = 0
        numero_columnas_fermentacion = 0
        numero_iteraciones_fermentacion = 0

        #Datos para la asignación de la graduacion
        matriz_graduacion = []
        numero_filas_graduacion = 0
        numero_columnas_graduacion = 0
        numero_iteraciones_graduacion = 0

        #Datos para la asignación del reposo
        matriz_reposo = []
        numero_filas_reposo = 0
        numero_columnas_reposo = 0
        numero_iteraciones_reposo = 0

        #Datos para la asignación del embotellado
        matriz_embotellado_1 = []
        numero_filas_embotellado_1 = 0
        numero_columnas_embotellado_1 = 0
        numero_iteraciones_embotellado_1 = 0

        matriz_embotellado_2 = []
        numero_filas_embotellado_2 = 0
        numero_columnas_embotellado_2 = 0
        numero_iteraciones_embotellado_2 = 0

        matriz_embotellado_3 = []
        numero_filas_embotellado_3 = 0
        numero_columnas_embotellado_3 = 0
        numero_iteraciones_embotellado_3 = 0


        #Creacion de los hilos para las funciones anteriormente creadas
        hilo_horno = Thread(target=self.metodo_hornos, name="Hilo_Hornos", args=(matriz_horno, numero_filas_horno,numero_columnas_horno,numero_iteraciones_horno))

        hilo_molino_1 = Thread(target=self.metodo_molinos, name="Hilo_Molinos", args=(matriz_molino_1, numero_filas_molino_1,numero_columnas_molino_1,numero_iteraciones_molino_1))

        hilo_molino_2 = Thread(target=self.metodo_molinos, name="Hilo_Molinos", args=(matriz_molino_2, numero_filas_molino_2,numero_columnas_molino_2,numero_iteraciones_molino_2))

        hilo_molino_3 = Thread(target=self.metodo_molinos, name="Hilo_Molinos", args=(matriz_molino_3, numero_filas_molino_3,numero_columnas_molino_3,numero_iteraciones_molino_3))

        hilo_fermentacion = Thread(target=self.metodo_fermentacion, name="Hilo_Fermentacion", args=(matriz_fermentacion, numero_filas_fermentacion,numero_columnas_fermentacion,numero_iteraciones_fermentacion))

        hilo_graduacion = Thread(target=self.metodo_graduacion, name="Hilo_Graduacion", args=(matriz_graduacion, numero_filas_graduacion,numero_columnas_graduacion,numero_iteraciones_graduacion))
        
        hilo_reposo = Thread(target=self.metodo_reposo, name="Hilo_Reposo", args=(matriz_reposo, numero_filas_reposo,numero_columnas_reposo,numero_iteraciones_reposo))

        hilo_embotellado_1 = Thread(target=self.metodo_embotellado, name="Hilo_Embotellado", args=(matriz_embotellado_1, numero_filas_embotellado_1,numero_columnas_embotellado_1,numero_iteraciones_embotellado_1))

        hilo_embotellado_2 = Thread(target=self.metodo_embotellado, name="Hilo_Embotellado", args=(matriz_embotellado_2, numero_filas_embotellado_2,numero_columnas_embotellado_2,numero_iteraciones_embotellado_2))

        hilo_embotellado_3 = Thread(target=self.metodo_embotellado, name="Hilo_Embotellado", args=(matriz_embotellado_3, numero_filas_embotellado_3,numero_columnas_embotellado_3,numero_iteraciones_embotellado_3))

        #Inicializacion de todos los procesos de la simulacion y retorno de los resultados
        horno_prom, horno_max, horno_min, cost_prom_horno, costo_max_horno, costo_min_horno  = hilo_horno.start()
        

        molino_prom_1, molino_max_1, molino_min_1, cost_prom_molino_1, costo_max_molino_1, costo_min_molino_1 = hilo_molino_1.start()
        
        molino_prom_2, molino_max_2, molino_min_2, cost_prom_molino_2, costo_max_molino_2, costo_min_molino_2 = hilo_molino_2.start()
        
        molino_prom_3, molino_max_3, molino_min_3, cost_prom_molino_3, costo_max_molino_3, costo_min_molino_3 = hilo_molino_3.start()
        

        fermentacion_prom, fermentacion_max, fermentacion_min, cost_prom_fermentacion, costo_max_fermentacion, costo_min_fermentacion = hilo_fermentacion.start()
        
        graduacion_prom, graduacion_max, graduacion_min, cost_prom_graduacion, costo_max_graduacion, costo_min_graduacion = hilo_graduacion.start()
        
        repo_prom, repo_max, repo_min, cost_prom_reposo, costo_max_reposo, costo_min_reposo = hilo_reposo.start()
        

        embotellado_prom_1, embotellado_max_1, embotellado_min_1, cost_prom_embotellado_1, costo_max_embotellado_1, costo_min_embotellado_1= hilo_embotellado_1.start()
        
        embotellado_prom_2, embotellado_max_2, embotellado_min_2, cost_prom_embotellado_2, costo_max_embotellado_2, costo_min_embotellado_2= hilo_embotellado_2.start()
        
        embotellado_prom_3, embotellado_max_3, embotellado_min_3, cost_prom_embotellado_3, costo_max_embotellado_3, costo_min_embotellado_3= hilo_embotellado_3.start()

        diccionario = {"horno_min":horno_min,
                    "horno_max":horno_max,
                    "horno_prom":horno_prom,
                    "cost_min_horno":costo_min_horno,
                    "cost_max_horno":costo_max_horno,
                    "cost_prom_horno":cost_prom_horno,
                    "molino_min_1":molino_min_1,
                    "molino_max_1":molino_max_1,
                    "molino_prom_1":molino_prom_1,
                    "cost_min_molino_1":costo_min_molino_1,
                    "cost_max_molino_1":costo_max_molino_1,
                    "cost_prom_molino_1":cost_prom_molino_1,
                    "molino_min_2":molino_min_2,
                    "molino_max_2":molino_max_2,
                    "molino_prom_2":molino_prom_2,
                    "cost_min_molino_2":costo_min_molino_2,
                    "cost_max_molino_2":costo_max_molino_2,
                    "cost_prom_molino_2":cost_prom_molino_2,
                    "molino_min_3":molino_min_3,
                    "molino_max_3":molino_max_3,
                    "molino_prom_3":molino_prom_3,
                    "cost_min_molino_3":costo_min_molino_3,
                    "cost_max_molino_3":costo_max_molino_3,
                    "cost_prom_molino_3":cost_prom_molino_3,
                    "fermentacion_min":fermentacion_min,
                    "fermentacion_max":fermentacion_max,
                    "fermentacion_prom":fermentacion_prom,
                    "cost_min_fermentacion":costo_min_fermentacion,
                    "cost_max_fermentacion":costo_max_fermentacion,
                    "cost_prom_fermentacion":cost_prom_fermentacion,
                    "graduacion_min":graduacion_min,
                    "graduacion_max":graduacion_max,
                    "graduacion_prom":graduacion_prom,
                    "cost_min_graduacion":costo_min_graduacion,
                    "cost_max_graduacion":costo_max_graduacion,
                    "cost_prom_graduacion":cost_prom_graduacion,
                    "repo_min":repo_min,
                    "repo_max":repo_max,
                    "repo_prom":repo_prom,
                    "cost_min_reposo":costo_min_reposo,
                    "cost_max_reposo":costo_max_reposo,
                    "cost_prom_reposo":cost_prom_reposo,
                    "embotellado_min_1":embotellado_min_1,
                    "embotellado_max_1":embotellado_max_1,
                    "embotellado_prom_1":embotellado_prom_1,
                    "cost_min_embotellado_1":costo_min_embotellado_1,
                    "cost_max_embotellado_1":costo_max_embotellado_1,
                    "cost_prom_embotellado_1":cost_prom_embotellado_1,
                    "embotellado_min_2":embotellado_min_2,
                    "embotellado_max_2":embotellado_max_2,
                    "embotellado_prom_2":embotellado_prom_2,
                    "cost_min_embotellado_2":costo_min_embotellado_2,
                    "cost_max_embotellado_2":costo_max_embotellado_2,
                    "cost_prom_embotellado_2":cost_prom_embotellado_2,
                    "embotellado_min_3":embotellado_min_3,
                    "embotellado_max_3":embotellado_max_3,
                    "embotellado_prom_3":embotellado_prom_3,
                    "cost_min_embotellado_3":costo_min_embotellado_3,
                    "cost_max_embotellado_3":costo_max_embotellado_3,
                    "cost_prom_embotellado_3":cost_prom_embotellado_3
                    }

        creaPDF.crear_pdf("\templates",diccionario,"reporte_produccion.html")


if __name__ == "__main__":
    funciones_produccion().iniciar_hilos()