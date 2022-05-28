import random
import numpy as np

class Abastecimiento():

    def proceso_tiempo(self, matriz, numero_filas,numero_columnas,numero_iteraciones):
        # este se encarga de calcular el tiempo 

        contador = 0
        envio_maximo = 0
        envio_minimo = None
        promedio_tiempo = 0 

        matriz = self.probabilidad_acumulada(matriz,numero_filas,numero_columnas)

        while(contador < numero_iteraciones):

            numero_aleatorio  = random.random()

            valor, numero_fila = self.sacar_valor(matriz,numero_filas,numero_columnas,numero_aleatorio)


            if(envio_minimo == None):

                envio_minimo = valor

            elif(envio_maximo < valor):

                envio_maximo = valor

            if(envio_minimo > valor):

                envio_minimo = valor

            promedio_tiempo += valor



            contador += 1

        promedio_tiempo = promedio_tiempo/numero_iteraciones

        #print("Tiempo promeio:", promedio_tiempo, ",Envio maximo:", envio_maximo, "Envio minimo:", envio_minimo)
        
        return promedio_tiempo, envio_maximo, envio_minimo

    def proceso_costo(self, matriz, numero_filas,numero_columnas,numero_iteraciones):

        # este se encarga de calcular el costo

        contador = 0
        envio_maximo = 0
        envio_minimo = None
        promedio_costo = 0    

        matriz = self.probabilidad_acumulada(matriz,numero_filas,numero_columnas)
        #print(matriz)
        while(contador < numero_iteraciones):

            numero_aleatorio  = random.random()
            #print(numero_aleatorio)
            # el valor es el dato que le corresponde al numero aleatorio, esto lo sabemos gracias a los rangos
            # el numero de fila, es la fila en la que se encuentra el el dato
            valor, numero_fila = self.sacar_valor(matriz,numero_filas,numero_columnas,numero_aleatorio)

            #print(valor,numero_fila)

            if(envio_minimo == None):

                envio_minimo = valor


            elif(envio_minimo > valor):

                envio_minimo = valor
                #print(envio_minimo, ":", valor,numero_fila, ":", numero_aleatorio)

            if(envio_maximo < valor):

                envio_maximo = valor


            promedio_costo += valor

            contador += 1
            

        promedio_costo = promedio_costo/numero_iteraciones

        #print("Costo promedio:", promedio_costo, ",Costo maximo:", envio_maximo, "Costo minimo:", envio_minimo)

        return promedio_costo, envio_maximo, envio_minimo
    
    def probabilidad_acumulada(self,matriz,numero_filas,numero_columnas):
        #saca la probabilidad acumulada y la coloca en la matriz

        probabilidad_acumulado = 0

        for i in range(0,numero_filas):

            probabilidad_acumulado += matriz[i][numero_columnas-2]

            matriz[i][numero_columnas-1] = probabilidad_acumulado


        return matriz

    def sacar_valor(self, matriz, numerofilas, numero_columnas, numero_aleatorio):
        # saca el valor que le corresponde a ese numero aleatorio, comparadon dinamicamente los rangos

        suelo = 0
        numero = 0
        numero_fila = 0

        if(numero_aleatorio == 0):

            numero = matriz[0][0]

        else:

            for i in range(numerofilas):

                
                tope = matriz[i][numero_columnas-1]

                sentencia  = numero_aleatorio > suelo and numero_aleatorio <= tope

                if(sentencia):

                    numero = matriz[i][0]
                    numero_fila = i
                    break

                suelo = tope 
                    
        return numero, numero_fila

if(__name__ == "__main__"):

    matriz = np.zeros((3,3))

    matriz[0][0] = 2
    matriz[0][1] = 0.3

    matriz[1][0] = 5
    matriz[1][1] = 0.5

    matriz[2][0] = 8
    matriz[2][1] = 0.2
    
    #m = Abastecimiento()
    #matriz_acumulada = m.probabilidad_acumulada(matriz,3,3)
    #print(matriz_acumulada)
    #print(m.sacar_valor(matriz_acumulada,3,3,0.801))
    #print(m.probabilidad_acumulada(matriz,3,3))
    #m.proceso_costo(matriz,3,3,100000)
    #m.proceso_tiempo(matriz,3,3,100000)
    
    


            
            


        