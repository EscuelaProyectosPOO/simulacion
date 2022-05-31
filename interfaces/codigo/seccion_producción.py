from threading import *
import numpy as np
from datetime import *

#Importacion de los archivos necesarios
from interfaces.codigo.Abastecimiento import Abastecimiento
from interfaces.codigo import creaPDF
class funciones_produccion(Abastecimiento):
    # Hilo que se encarga de la coccion en el honro
    def metodo_hornos(self, lista_datos_hornos, numero_iteraciones):
        matriz_tiempo = lista_datos_hornos[0]
        numero_filas_tiempo = lista_datos_hornos[2]
        numero_columnas_tiempo = lista_datos_hornos[3]
        
        #Obtencion de los registros de los tiempos de operación
        tiempo_promedio_horno, tiempo_maximo_horno, tiempo_minimo_horno = self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        return tiempo_promedio_horno, tiempo_maximo_horno, tiempo_minimo_horno

    # Hilo que se encarga de controlar la molida 
    def metodo_molinos(self,lista_datos_molinos,numero_iteraciones):
        matriz_tiempo = lista_datos_molinos[0]
        matriz_costo = lista_datos_molinos[1]
        numero_filas_tiempo = lista_datos_molinos[2]
        numero_filas_costo = lista_datos_molinos[3]
        numero_columnas_tiempo = lista_datos_molinos[4]
        numero_columnas_costo = lista_datos_molinos[5]
        
        tiempo_promedio_molino, tiempo_maximo_molino, tiempo_minimo_molino = self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        #Obtencion de los registros de nominas
        costo_promedio_molino, costo_maximo_molino, costo_minimo_molino  = self.proceso_costo(matriz_costo, numero_filas_costo,numero_columnas_costo,numero_iteraciones)

        return tiempo_promedio_molino, tiempo_maximo_molino, tiempo_minimo_molino, costo_promedio_molino, costo_maximo_molino, costo_minimo_molino
    
    # Hilo que se encarga de controlar la fermentacion
    def metodo_fermentacion(self,matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_fermentacion, tiempo_maximo_fermentacion, tiempo_minimo_fermentacion = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_fermentacion, tiempo_maximo_fermentacion, tiempo_minimo_fermentacion

    # Hilo que se encarga de controlar la graduacion del mezcal
    def metodo_graduacion(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_graduacion, tiempo_maximo_graduacion, tiempo_minimo_graduacion = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_graduacion, tiempo_maximo_graduacion, tiempo_minimo_graduacion

    # Hilo que se encarga del reposo del mezcal
    def metodo_reposo(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_reposo, tiempo_maximo_reposo, tiempo_minimo_reposo = self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_reposo, tiempo_maximo_reposo, tiempo_minimo_reposo

    # Hilo que se encarga de controlar el embotellamiento
    def metodo_embotellado(self, lista_embotellado,numero_iteraciones):
        matriz_tiempo = lista_embotellado[0]
        matriz_costo = lista_embotellado[1]
        numero_filas_tiempo = lista_embotellado[2]
        numero_filas_costo = lista_embotellado[3]
        numero_columnas_tiempo = lista_embotellado[4]
        numero_columnas_costo = lista_embotellado[5]


        tiempo_promedio_embotellado, tiempo_maximo_embotellado, tiempo_minimo_embotellado = self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        #Obtencion de los registros de los costos de operación
        costo_promedio_embotellado, costo_maximo_embotellado, costo_minimo_embotellado = self.proceso_costo(matriz_costo, numero_filas_costo,numero_columnas_costo,numero_iteraciones)

        return tiempo_promedio_embotellado, tiempo_maximo_embotellado, tiempo_minimo_embotellado, costo_promedio_embotellado, costo_maximo_embotellado, costo_minimo_embotellado

    #Funcion que inicializa los hilos
    def iniciar_hilos(self, lista_horno, lista_molino_1, lista_molino_2, lista_molino_3, lista_fermentacion, lista_graduacion, lista_reposo, lista_embotellado_1, lista_embotellado_2, lista_embotellado_3, numero_iteraciones, nomina_empleado, costo_uso_horno):
                
        #Datos para la asignación de la fermentacion
        matriz_fermentacion = lista_fermentacion[0]
        numero_filas_fermentacion = lista_fermentacion[1]
        numero_columnas_fermentacion = lista_fermentacion[2]

        #Datos para la asignación de la graduacion
        matriz_graduacion = lista_graduacion[0]
        numero_filas_graduacion = lista_graduacion[1]
        numero_columnas_graduacion = lista_graduacion[2]

        #Datos para la asignación del reposo
        matriz_reposo = lista_reposo[0]
        numero_filas_reposo = lista_reposo[1]
        numero_columnas_reposo = lista_reposo[2]
        numero_iteraciones_reposo = numero_iteraciones


        #Inicializacion de todos los procesos de la simulacion y retorno de los resultados
        horno_prom, horno_max, horno_min = self.metodo_hornos(lista_horno, numero_iteraciones)
        
        molino_prom_1, molino_max_1, molino_min_1, cost_prom_molino_1, costo_max_molino_1, costo_min_molino_1 = self.metodo_molinos(lista_molino_1, numero_iteraciones)
        
        molino_prom_2, molino_max_2, molino_min_2, cost_prom_molino_2, costo_max_molino_2, costo_min_molino_2 = self.metodo_molinos(lista_molino_2, numero_iteraciones)
        
        molino_prom_3, molino_max_3, molino_min_3, cost_prom_molino_3, costo_max_molino_3, costo_min_molino_3 = self.metodo_molinos(lista_molino_3, numero_iteraciones)

        fermentacion_prom, fermentacion_max, fermentacion_min = self.metodo_fermentacion(matriz_fermentacion, numero_filas_fermentacion, numero_columnas_fermentacion, numero_iteraciones)
        
        graduacion_prom, graduacion_max, graduacion_min = self.metodo_graduacion(matriz_graduacion, numero_filas_graduacion, numero_columnas_graduacion, numero_iteraciones)
        
        repo_prom, repo_max, repo_min = self.metodo_reposo(matriz_reposo, numero_filas_reposo, numero_columnas_reposo, numero_iteraciones_reposo)

        embotellado_prom_1, embotellado_max_1, embotellado_min_1, cost_prom_embotellado_1, costo_max_embotellado_1, costo_min_embotellado_1= self.metodo_embotellado(lista_embotellado_1, numero_iteraciones)
        
        embotellado_prom_2, embotellado_max_2, embotellado_min_2, cost_prom_embotellado_2, costo_max_embotellado_2, costo_min_embotellado_2= self.metodo_embotellado(lista_embotellado_2, numero_iteraciones)
        
        embotellado_prom_3, embotellado_max_3, embotellado_min_3, cost_prom_embotellado_3, costo_max_embotellado_3, costo_min_embotellado_3= self.metodo_embotellado(lista_embotellado_3, numero_iteraciones)

        #Calculamos las nominas de los procesos
        nomina_prom_molino_1 = molino_prom_1 * nomina_empleado * 3
        nomina_prom_molino_2 = molino_prom_2 * nomina_empleado * 4
        nomina_prom_molino_3 = molino_prom_3 * nomina_empleado * 5

        nomina_min_molino_1 = molino_min_1 * nomina_empleado * 3
        nomina_min_molino_2 = molino_min_2 * nomina_empleado * 4
        nomina_min_molino_3 = molino_min_3 * nomina_empleado * 5

        nomina_max_molino_1 = molino_max_1 * nomina_empleado * 3
        nomina_max_molino_2 = molino_max_2 * nomina_empleado * 4
        nomina_max_molino_3 = molino_max_3 * nomina_empleado * 5

        nomina_prom_envasado_1 = embotellado_prom_1 * nomina_empleado * 3
        nomina_prom_envasado_2 = embotellado_prom_2 * nomina_empleado * 4
        nomina_prom_envasado_3 = embotellado_prom_3 * nomina_empleado * 5
        
        nomina_min_envasado_1 = embotellado_min_1 * nomina_empleado * 3
        nomina_min_envasado_2 = embotellado_min_2 * nomina_empleado * 4
        nomina_min_envasado_3 = embotellado_min_3 * nomina_empleado * 5

        nomina_max_envasado_1 = embotellado_max_1 * nomina_empleado * 3
        nomina_max_envasado_2 = embotellado_max_2 * nomina_empleado * 4
        nomina_max_envasado_3 = embotellado_max_3 * nomina_empleado * 5

        #Se calcularán los costos del uso del horno
        costo_min_horno = horno_min * costo_uso_horno
        costo_max_horno = horno_max * costo_uso_horno
        costo_prom_horno = horno_prom * costo_uso_horno
        
        #Creación del diccionario que contendrá los valores para la generación de un pdf
        diccionario = {"horno_min":horno_min,
                    "horno_max":horno_max,
                    "horno_prom":horno_prom,
                    "cost_min_horno":costo_min_horno,
                    "costo_max_horno":costo_max_horno,
                    "costo_prom_horno":costo_prom_horno,

                    "molino_min_1":molino_min_1,
                    "molino_max_1":molino_max_1,
                    "molino_prom_1":molino_prom_1,
                    "cost_min_molino_1":costo_min_molino_1,
                    "costo_max_molino_1":costo_max_molino_1,
                    "costo_prom_molino_1":cost_prom_molino_1,
                    "pago_min_molinos_1":nomina_min_molino_1,
                    "pago_max_molinos_1":nomina_max_molino_1,
                    "pago_prom_molinos_1":nomina_prom_molino_1,

                    "molino_min_2":molino_min_2,
                    "molino_max_2":molino_max_2,
                    "molino_prom_2":molino_prom_2,
                    "cost_min_molino_2":costo_min_molino_2,
                    "costo_max_molino_2":costo_max_molino_2,
                    "costo_prom_molino_2":cost_prom_molino_2,
                    "pago_min_molinos_2":nomina_min_molino_2,
                    "pago_max_molinos_2":nomina_max_molino_2,
                    "pago_prom_molinos_2":nomina_prom_molino_2,


                    "molino_min_3":molino_min_3,
                    "molino_max_3":molino_max_3,
                    "molino_prom_3":molino_prom_3,
                    "cost_min_molino_3":costo_min_molino_3,
                    "costo_max_molino_3":costo_max_molino_3,
                    "costo_prom_molino_3":cost_prom_molino_3,
                    "pago_min_molinos_3":nomina_min_molino_3,
                    "pago_max_molinos_3":nomina_max_molino_3,
                    "pago_prom_molinos_3":nomina_prom_molino_3,
                    
                    "ferm_min":fermentacion_min,
                    "ferm_max":fermentacion_max,
                    "ferm_prom":fermentacion_prom,

                    "grad_min":graduacion_min,
                    "grad_max":graduacion_max,
                    "grad_prom":graduacion_prom,

                    "rep_min":repo_min,
                    "rep_max":repo_max,
                    "rep_prom":repo_prom,

                    "alm_min_1":embotellado_min_1,
                    "alm_max_1":embotellado_max_1,
                    "alm_prom_1":embotellado_prom_1,
                    "cost_min_alm_1":costo_min_embotellado_1,
                    "costo_max_alm_1":costo_max_embotellado_1,
                    "costo_prom_alm_1":cost_prom_embotellado_1,
                    "pago_min_alm_1":nomina_min_envasado_1,
                    "pago_max_alm_1":nomina_max_envasado_1,
                    "pago_prom_alm_1":nomina_prom_envasado_1,

                    "alm_min_2":embotellado_min_2,
                    "alm_max_2":embotellado_max_2,
                    "alm_prom_2":embotellado_prom_2,
                    "cost_min_alm_2":costo_min_embotellado_2,
                    "costo_max_alm_2":costo_max_embotellado_2,
                    "costo_prom_alm_2":cost_prom_embotellado_2,
                    "pago_min_alm_2":nomina_min_envasado_2,
                    "pago_max_alm_2":nomina_max_envasado_2,
                    "pago_prom_alm_2":nomina_prom_envasado_2,


                    "alm_min_3":embotellado_min_3,
                    "alm_max_3":embotellado_max_3,
                    "alm_prom_3":embotellado_prom_3,
                    "cost_min_alm_3":costo_min_embotellado_3,
                    "costo_max_alm_3":costo_max_embotellado_3,
                    "costo_prom_alm_3":cost_prom_embotellado_3,
                    "pago_min_alm_3":nomina_min_envasado_3,
                    "pago_max_alm_3":nomina_max_envasado_3,
                    "pago_prom_alm_3":nomina_prom_envasado_3,
                    }
        
        print("Despues del diccionario")

        #Creación del pdf
        anio = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        hora = datetime.now().hour
        minuto = datetime.now().minute
        segundo = datetime.now().second
        nombre_pdf = "Reporte_produccion-"+str(anio)+"-"+str(mes)+"-"+str(dia)+"_"+str(hora)+"-"+str(minuto)+"-"+str(segundo)+".pdf"

        print(nombre_pdf)

        print("Antes del pdf")

        #creaPDF.crear_pdf("C:/Users/ALEXG/Documents/Ingeniería en Sistemas Computacionales/Semestre 4/Simulacion/Proyecto simulacion/simulacion/templates/template_produccion.html",diccionario,nombre_pdf)
        creaPDF.crear_pdf("C:/Users/tetil/OneDrive/Documents/simulacion/templates/template_abastecimiento.html",diccionario,nombre_pdf)
        return nombre_pdf


if __name__ == "__main__":
    matriz = [[2,0.3],[5,0.5],[8,0.2]]
    numero_filas = 3
    numero_columnas = 2
    lista_horno = [matriz,numero_filas,numero_columnas]
    lista_molino_1 = [matriz,numero_filas,numero_columnas]
    lista_molino_2 = [matriz,numero_filas,numero_columnas]
    lista_molino_3 = [matriz,numero_filas,numero_columnas]
    lista_fermentacion = [matriz,numero_filas,numero_columnas]
    lista_graduacion = [matriz,numero_filas,numero_columnas]
    lista_reposo = [matriz,numero_filas,numero_columnas]
    lista_embotellado_1 = [matriz,numero_filas,numero_columnas]
    lista_embotellado_2 = [matriz,numero_filas,numero_columnas]
    lista_embotellado_3 = [matriz,numero_filas,numero_columnas]
    numero_iteraciones = 10
    nomina = 100

    funciones_produccion().iniciar_hilos(lista_horno,lista_molino_1,lista_molino_2,lista_molino_3,lista_fermentacion,lista_graduacion,lista_reposo,lista_embotellado_1,lista_embotellado_2,lista_embotellado_3,numero_iteraciones, nomina)