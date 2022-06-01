
from tkinter import messagebox

class prueba_frecuencias:
    def procedimiento_frecuencias(self,aleatorio,alpha,secciones):
        aleatorios = aleatorio
        separacion = secciones

        tamano = len(str(aleatorios[0]))
        longitud = "1"
        for i in range(tamano):
            longitud = longitud + "0"
        
        inter = int(longitud) / separacion      

        frecuencia = []
        for i in range(separacion):
            frecuencia.append(list())

        rangomin = 0
        rangomax = int(inter)
        for i in range(separacion):

            for j in range(len(aleatorios)):
                if aleatorios[j] >= rangomin and aleatorios[j] <= rangomax:
                    frecuencia[i].append(aleatorios[j])

            rangomin = rangomin + int(inter)
            rangomax = rangomax + int(inter)
        
        fe = float(len(aleatorios)/separacion)
        
        frecuencias_observadas = []
        for i in range(separacion):
            frecuencias_observadas.append(list())
        
        
        for i in range(separacion):
            size_temp = len(frecuencia[i])
            frecuencias_observadas[i].append(size_temp)
        
        
        x0 = 0
        for i in range(separacion):
            fo = float(frecuencias_observadas[i][0])
            x0 = x0 + (((fo - fe)**2.0)/fe)
        
        print(x0)

        if x0 < alpha:
            messagebox.showinfo("Resultado","La secuencia de datos ha sido acepatada.")
        else:
            messagebox.showerror("Resultado","La secuencia de datos ha sido rechazada.")
