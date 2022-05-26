import numpy as np
import random
from Abastecimiento import Abastecimiento

class Ventas(Abastecimiento):

    # esta clase sirve para contabilizar y saber el tiempo de llegada del cliente, su estancia, y el tipo de alcohol que se llevara

    def proceso_alcohol(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        # saber que tipo 

        contador = 0
        numero_fila = 0
        
        matriz = self.probabilidad_acumulada(matriz,numero_filas,numero_columnas)
        matriz_contador = self.crear_matriz_botellas(matriz,numero_filas)


        while(contador < numero_iteraciones):

            numero_aleatorio = random.random()

            valor, numero_fila = self.sacar_valor(matriz,numero_filas,numero_columnas,numero_aleatorio)

            matriz_contador[numero_fila][2] += 1
            matriz_contador[numero_fila][3] += matriz[numero_fila][1]

            contador += 1

        ganancias_totales = self.extraer_ganancias_totales(matriz_contador,numero_filas)
        print(matriz_contador, ganancias_totales)

        

    def crear_matriz_botellas(self, matriz, numero_filas):
        # crea una nueva matriz que se ultilizara para el conteo de las botellas

        matriz_nueva = np.zeros((numero_filas,4))

        for i in range(numero_filas):

            for j in range(2):

                matriz_nueva[i][j] = matriz[i][j]


        return matriz_nueva

    def extraer_ganancias_totales(self, matriz, numero_filas):
       # extrae las ganancias totales de la venta de botellas

        ganancias_totales = 0
        for i in range(numero_filas):

            ganancias_totales += matriz[i][3]


        return ganancias_totales






if(__name__ == "__main__"):

    matriz = np.zeros((3,4))

    matriz[0][0] = 2.5
    matriz[0][1] = 6000
    matriz[0][2] = 0.3

    matriz[1][0] = 5
    matriz[1][1] = 70000
    matriz[1][2] = 0.5

    matriz[2][0] = 1.2
    matriz[2][1] = 69000 
    matriz[2][2] = 0.2


    m = Ventas()
    #print(m.crear_matriz_botellas(matriz,3))
    #print(m.probabilidad_acumulada(matriz,3,4))
    #m.crear_matriz_botellas(matriz,3)
    m.proceso_alcohol(matriz,3,4,10)

    
    
