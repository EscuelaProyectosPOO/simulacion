
from tkinter import messagebox

class pruebas_komolgorov:
    def procedimiento_komolgorov(self, aleatorios, alpha):
        valores = []
        for i in range(len(aleatorios)):
            size = int(len(aleatorios))
            division = float((i + 1) / size)
            resta = division - aleatorios[i]
            valores.append(abs(resta))
        
        #Llena una lista con todos los valores de alpha con valor a 0.05
        valores_alpha = [[1,3.84],
                         [2,5.99],
                         [3,7.81],
                         [4,9.49],
                         [5,11.07],
                         [6,12.59],
                         [7,14.07],
                         [8,15.51],
                         [9,16.92],
                         [10,18.31],
                         [11,19.68],
                         [12,21.03],
                         [13,22.36],
                         [14,23.68],
                         [15,25.00],
                         [16,26.31],
                         [17,27.59],
                         [18,28.87],
                         [19,30.14],
                         [20,31.41],
                         [25,37.65],
                         [30,43.77],
                         [40,55.76],
                         [50,67.50],
                         [60,79.08],
                         [70,90.53],
                         [80,101.88],
                         [90,113.14],
                         [100,124.34]],


        valores.sort()
        minimo = valores[0]
        
        if minimo <= alpha:
            messagebox.showinfo("Resultado", "La sentencia H0 se acepta. Los numeros están en el intervalo de confianza")
        else:
            messagebox.showerror("Resultado", "La sentencia H0 se rechaza. Los numeros no están en el intervalo de confianza")