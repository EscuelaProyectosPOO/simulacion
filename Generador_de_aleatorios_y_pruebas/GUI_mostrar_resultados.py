from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

class gui_resultados:

    def gui_mostrar(self, aleatorios):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Simulacion - ventana de resultados')
        gui.config(bg = '#88bea1')
        gui.resizable(0,0)
        gui.iconbitmap("Generador_de_aleatorios_y_pruebas/logo.ico")

        labeltitiulo = Label(gui, text = "Resultados", bg = "#c0c1c3", font = "Times", width = "25", height= "2")
        labeltitiulo.place(relx=0.175, rely=0.125)
        
        frame_auxiliar = Frame(gui)
        frame_auxiliar.place(relx=0.25,rely=0.3)

        scroll = Scrollbar(frame_auxiliar,orient="vertical")
        scroll.pack(side=RIGHT,fill=Y)

        caja_resultados = Listbox(frame_auxiliar,yscrollcommand=scroll.set, justify="center", font="Times", height=8)
        caja_resultados.pack(side=LEFT)

        scroll.config(command=caja_resultados.yview)

        #print(aleatorios)

        size = len(aleatorios)
        for i in range(size):
            string_aleatorio = str(aleatorios[i])
            string_aleatorio = "0." + string_aleatorio
            float_aleatorio = float(string_aleatorio)
            aleatorios[i] = float_aleatorio

        size = len(aleatorios)
        for i in range(size):
            caja_resultados.insert(END,aleatorios[i])
        

        def guardar_aleatorios():
           
            archivo_abierto = open("base_datos/Numeros_aleatorios.txt","a")

            for i in range(len(aleatorios)):
    
                if i <= len(aleatorios)-1:
                    archivo_abierto.write(str(aleatorios[i]) + "\n")
                else:
                    archivo_abierto.write(str(aleatorios[i]))
                
            archivo_abierto.close()

            messagebox.showinfo("Exito", "El archivo ha sido creado correctamente.")

        boton_guardar = Button(gui, text="Guardar", command=guardar_aleatorios,font="Times",bg="#cbc9bb")
        boton_guardar.place(relx=0.275, rely=0.85)
        boton_guardar.config(activebackground="#94A9B9", width="16", height="1")

        gui.mainloop()
'''r = gui_resultados()
r.gui_mostrar()'''