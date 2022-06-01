from threading import *
import numpy as np
from datetime import *

#Importación de los archivos necesarios
from interfaces.codigo.Abastecimiento import Abastecimiento
from interfaces.codigo import creaPDF

class funciones_abastecimiento(Abastecimiento):
    #Creacion del hilo para los suministros de piñas
    def pinas(self,lista_pinas,numero_iteraciones):

        matriz_tiempo = lista_pinas[0]
        matriz_costos = lista_pinas[1]
        numero_filas_tiempo = lista_pinas[2]
        numero_filas_costos = lista_pinas[3]
        numero_columnas_tiempo = lista_pinas[4]
        numero_columnas_costos = lista_pinas[5]
        
        tiempo_promedio_pinas, tiempo_maximo_pinas, tiempo_minimo_pinas =  self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        costo_promedio_pinas, costo_maximo_pinas, costo_minimo_pinas = self.proceso_costo(matriz_costos, numero_filas_costos,numero_columnas_costos,numero_iteraciones)

        return tiempo_promedio_pinas, tiempo_maximo_pinas, tiempo_minimo_pinas, costo_promedio_pinas, costo_maximo_pinas, costo_minimo_pinas

    def botellas_vidrio(self,lista_vidrio,numero_iteraciones):
        matriz_tiempo = lista_vidrio[0]
        matriz_costos = lista_vidrio[1]
        numero_filas_tiempo = lista_vidrio[2]
        numero_filas_costos = lista_vidrio[3]
        numero_columnas_tiempo = lista_vidrio[4]
        numero_columnas_costos = lista_vidrio[5]
                
        tiempo_promedio_bv, tiempo_maximo_bv, tiempo_minimo_bv =  self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        costo_promedio_bv, costo_maximo_bv, costo_minimo_bv= self.proceso_costo(matriz_costos, numero_filas_costos,numero_columnas_costos,numero_iteraciones)
        
        return tiempo_promedio_bv, tiempo_maximo_bv, tiempo_minimo_bv, costo_promedio_bv, costo_maximo_bv, costo_minimo_bv

    def tapones_corchos(self,lista_tapones,numero_iteraciones):
        matriz_tiempo = lista_tapones[0]
        matriz_costos = lista_tapones[1]
        numero_filas_tiempo = lista_tapones[2]
        numero_filas_costos = lista_tapones[3]
        numero_columnas_tiempo = lista_tapones[4]
        numero_columnas_costos = lista_tapones[5]
        
        tiempo_promedio_corchos, tiempo_maximo_corchos, tiempo_minimo_corchos =  self.proceso_tiempo(matriz_tiempo,numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        costo_promedio_corchos, costo_maximo_corchos, costo_minimo_corchos = self.proceso_costo(matriz_costos, numero_filas_costos,numero_columnas_costos,numero_iteraciones)

        return tiempo_promedio_corchos, tiempo_maximo_corchos, tiempo_minimo_corchos, costo_promedio_corchos, costo_maximo_corchos, costo_minimo_corchos

    def botellas_pet(self,lista_pet,numero_iteraciones):
        matriz_tiempo = lista_pet[0]
        matriz_costos = lista_pet[1]
        numero_filas_tiempo = lista_pet[2]
        numero_filas_costos = lista_pet[3]
        numero_columnas_tiempo = lista_pet[4]
        numero_columnas_costos = lista_pet[5]     

        tiempo_promedio_bp, tiempo_maximo_bp, tiempo_minimo_bp =  self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        costo_promedio_bp, costo_maximo_bp, costo_minimo_bp = self.proceso_costo(matriz_costos, numero_filas_costos,numero_columnas_costos,numero_iteraciones)

        return tiempo_promedio_bp, tiempo_maximo_bp, tiempo_minimo_bp, costo_promedio_bp, costo_maximo_bp, costo_minimo_bp

    def etiquetas_sellos(self,lista_sellos,numero_iteraciones):
        matriz_tiempo = lista_sellos[0]
        matriz_costos = lista_sellos[1]
        numero_filas_tiempo = lista_sellos[2]
        numero_filas_costos = lista_sellos[3]
        numero_columnas_tiempo = lista_sellos[4]
        numero_columnas_costos = lista_sellos[5]

        tiempo_promedio_sellos, tiempo_maximo_sellos, tiempo_minimo_sellos =  self.proceso_tiempo(matriz_tiempo, numero_filas_tiempo,numero_columnas_tiempo,numero_iteraciones)

        costo_promedio_sellos, costo_maximo_sellos, costo_minimo_sellos = self.proceso_costo(matriz_costos, numero_filas_costos,numero_columnas_costos,numero_iteraciones)

        return tiempo_promedio_sellos, tiempo_maximo_sellos, tiempo_minimo_sellos, costo_promedio_sellos, costo_maximo_sellos, costo_minimo_sellos

    def iniciar_hilos(self, lista_pinas, lista_bv, lista_corchos, lista_bp, lista_sellos, numero_iteraciones):
                #Inicialización de los hilos
        pina_prom, pina_max, pina_min, pina_costo_prom, pina_costo_max, pina_costo_min = self.pinas(lista_pinas, numero_iteraciones)
        bv_prom, bv_max, bv_min, bv_costo_prom, bv_costo_max, bv_costo_min  = self.botellas_vidrio(lista_bv, numero_iteraciones)
        corcho_prom, corcho_max, corcho_min,corcho_costo_prom,corcho_costo_max, corcho_costo_min  = self.tapones_corchos(lista_corchos, numero_iteraciones)
        bp_prom, bp_max,bp_min, bp_costo_prom, bp_costo_max, bp_costo_min  = self.botellas_pet(lista_bp, numero_iteraciones)
        sello_prom, sello_max, sello_min, sello_costo_prom, sello_costo_max, sello_costo_min  = self.etiquetas_sellos(lista_sellos, numero_iteraciones)
        
    
        #Creacion del diccionario para almacenar los resultados
        
        diccionario = {"pina_min": pina_min,
                       "pina_max": pina_max,
                       "pina_prom": pina_prom,
                       "cost_min_pina": pina_costo_min,
                       "costo_max_pina": pina_costo_max,
                       "costo_prom_pina": pina_costo_prom,
                       "bv_min": bv_min,
                       "bv_max": bv_max,
                       "bv_prom": bv_prom,
                       "cost_min_bv": bv_costo_min,
                       "costo_max_bv": bv_costo_max,
                       "costo_prom_bv": bv_costo_prom,
                       "tc_min": corcho_min,
                       "tc_max": corcho_max,
                       "tc_prom": corcho_prom,
                       "cost_min_tc": corcho_costo_min,
                       "costo_max_tc": corcho_costo_max,
                       "costo_prom_tc": corcho_costo_prom,
                       "bp_min": bp_min,
                       "bp_max": bp_max,
                       "bp_prom": bp_prom,
                       "cost_min_bp": bp_costo_min,
                       "costo_max_bp": bp_costo_max,
                       "costo_prom_bp": bp_costo_prom,
                       "ec_min": sello_min,
                       "ec_max": sello_max,
                       "ec_prom": sello_prom,
                       "cost_min_ec": sello_costo_min,
                       "costo_max_ec": sello_costo_max,
                       "costo_prom_ec": sello_costo_prom}
        
        #Creación del pdf
        anio = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        hora = datetime.now().hour
        minuto = datetime.now().minute
        segundo = datetime.now().second
        nombre_pdf = "Reporte_abastecimiento-"+str(anio)+"-"+str(mes)+"-"+str(dia)+"_"+str(hora)+"-"+str(minuto)+"-"+str(segundo)+".pdf"
    
        #creaPDF.crear_pdf("C:/Users/ALEXG/Documents/Ingeniería en Sistemas Computacionales/Semestre 4/Simulacion/Proyecto simulacion/simulacion/template_abastecimiento.html",diccionario,nombre_pdf)
        creaPDF.crear_pdf("C:/Users/tetil/OneDrive/Documents/simulacion/templates/template_abastecimiento.html",diccionario,nombre_pdf)
        return nombre_pdf
        
if __name__ == "__main__":
    matriz = [[2,0.3],[5,0.5],[8,0.2]]
    numero_filas = 3
    numero_columnas = 2

    lista_pinas = [matriz, numero_filas, numero_columnas]
    lista_bv = [matriz, numero_filas, numero_columnas]
    lista_corchos = [matriz, numero_filas, numero_columnas]
    lista_bp = [matriz, numero_filas, numero_columnas]
    lista_sellos = [matriz, numero_filas, numero_columnas]
    numeros_iteraciones = 10

    objeto = funciones_abastecimiento()
    objeto.iniciar_hilos(lista_pinas, lista_bv, lista_corchos, lista_bp, lista_sellos, numeros_iteraciones)