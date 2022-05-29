from threading import *
import numpy as np

#Importación de los archivos necesarios
from Abastecimiento import Abastecimiento
import creaPDF

class funciones_abastecimiento(Abastecimiento):
    #Creacion del hilo para los suministros de piñas
    def pinas(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_pinas, tiempo_maximo_pinas, tiempo_minimo_pinas =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_pinas, costo_maximo_pinas, costo_minimo_pinas = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_pinas, tiempo_maximo_pinas, tiempo_minimo_pinas, costo_promedio_pinas, costo_maximo_pinas, costo_minimo_pinas

    def botellas_vidrio(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_bv, tiempo_maximo_bv, tiempo_minimo_bv =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_bv, costo_maximo_bv, costo_minimo_bv= self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)
        
        return tiempo_promedio_bv, tiempo_maximo_bv, tiempo_minimo_bv, costo_promedio_bv, costo_maximo_bv, costo_minimo_bv

    def tapones_corchos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        
        tiempo_promedio_corchos, tiempo_maximo_corchos, tiempo_minimo_corchos =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_corchos, costo_maximo_corchos, costo_minimo_corchos = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_corchos, tiempo_maximo_corchos, tiempo_minimo_corchos, costo_promedio_corchos, costo_maximo_corchos, costo_minimo_corchos

    def botellas_pet(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_bp, tiempo_maximo_bp, tiempo_minimo_bp =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_bp, costo_maximo_bp, costo_minimo_bp = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_bp, tiempo_maximo_bp, tiempo_minimo_bp, costo_promedio_bp, costo_maximo_bp, costo_minimo_bp

    def etiquetas_sellos(self,matriz,numero_filas,numero_columnas,numero_iteraciones):
        tiempo_promedio_sellos, tiempo_maximo_sellos, tiempo_minimo_sellos =  self.proceso_tiempo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        costo_promedio_sellos, costo_maximo_sellos, costo_minimo_sellos = self.proceso_costo(matriz, numero_filas,numero_columnas,numero_iteraciones)

        return tiempo_promedio_sellos, tiempo_maximo_sellos, tiempo_minimo_sellos, costo_promedio_sellos, costo_maximo_sellos, costo_minimo_sellos

    def iniciar_hilos(self, lista_pinas, lista_bv, lista_corchos, lista_bp, lista_sellos, numero_iteraciones):
        #Se hará la asignación de los parametros para los hilos
        #Datos para la ejecucion del proceso de las piñas
        matriz_pinas = lista_pinas[0]
        numero_filas_pinas = lista_pinas[1]
        numero_columnas_pinas = lista_pinas[2]
        
        #Datos para la ejecucion de las botellas de vidrio
        matriz_bv = lista_bv[0]
        numero_filas_bv = lista_bv[1]
        numero_columnas_bv = lista_bv[2]

        #Datos para la ejecucion de los tapones corchos
        matriz_corchos = lista_corchos[0]
        numero_filas_corchos = lista_corchos[1]
        numero_columnas_corchos = lista_corchos[2]
        
        #Datos para la ejecucion de las botellas de pet
        matriz_bp = lista_bp[0]
        numero_filas_bp = lista_bp[1]
        numero_columnas_bp = lista_bp[2]

        #Datos para la ejecucion de las etiquetas de sellos
        matriz_sellos = lista_sellos[0]
        numero_filas_sellos = lista_sellos[1]
        numero_columnas_sellos = lista_sellos[2]
        
        #Creacion de los hilos para las funciones anteriormente creadas

        hilo_pinas = Thread(target=self.pinas, name="Hilo_pinas",args=(matriz_pinas,numero_filas_pinas,numero_columnas_pinas,numero_iteraciones))

        hilo_botellas_vidrio = Thread(target=self.botellas_vidrio,name="Hilo_botellas_vidiro",args=(matriz_bp,numero_filas_bp,numero_columnas_bp,numero_iteraciones))

        hilo_tapones_corcho = Thread(target=self.tapones_corchos,name="Hilo_tapones",args=(matriz_corchos,numero_filas_corchos,numero_columnas_corchos,numero_iteraciones))

        hilo_botellas_pet = Thread(target=self.botellas_pet,name="Hilo_botellas_pet",args=(matriz_bp,numero_filas_bp,numero_columnas_bp,numero_iteraciones))

        hilo_etiquetas = Thread(target=self.etiquetas_sellos,name="Hilo_etiquetas",args=(matriz_sellos,numero_filas_sellos,numero_columnas_sellos,numero_iteraciones))

        #Inicialización de los hilos
        pina_prom, pina_max, pina_min, pina_costo_prom, pina_costo_max, pina_costo_min = hilo_pinas.start()
        bv_min, bv_max, bv_prom, bv_costo_min, bv_costo_max, bv_costo_prom = hilo_botellas_vidrio.start()
        corcho_min, corcho_max, corcho_prom, corcho_costo_min, corcho_costo_max, corcho_costo_prom = hilo_tapones_corcho.start()
        bp_min, bp_max, bp_prom, bp_costo_min, bp_costo_max, bp_costo_prom = hilo_botellas_pet.start()
        sello_min, sello_max, sello_prom, sello_costo_min, sello_costo_max, sello_costo_prom = hilo_etiquetas.start()
        
    
        #Creacion del diccionario para almacenar los resultados
        
        diccionario = {"pina_min": pina_min,
                       "pina_max": pina_max,
                       "pina_prom": pina_prom,
                       "costo_min_pina": pina_costo_min,
                       "costo_max_pina": pina_costo_max,
                       "costo_prom_pina": pina_costo_prom,
                       "bv_min": bv_min,
                       "bv_max": bv_max,
                       "bv_prom": bv_prom,
                       "costo_min_bv": bv_costo_min,
                       "costo_max_bv": bv_costo_max,
                       "costo_prom_bv": bv_costo_prom,
                       "tc_min": corcho_min,
                       "tc_max": corcho_max,
                       "tc_prom": corcho_prom,
                       "costo_min_tc": corcho_costo_min,
                       "costo_max_tc": corcho_costo_max,
                       "costo_prom_tc": corcho_costo_prom,
                       "bp_min": bp_min,
                       "bp_max": bp_max,
                       "bp_prom": bp_prom,
                       "costo_min_bp": bp_costo_min,
                       "costo_max_bp": bp_costo_max,
                       "costo_prom_bp": bp_costo_prom,
                       "ec_min": sello_min,
                       "ec_max": sello_max,
                       "ec_prom": sello_prom,
                       "costo_min_ec": sello_costo_min,
                       "costo_max_ec": sello_costo_max,
                       "costo_prom_ec": sello_costo_prom}
        
