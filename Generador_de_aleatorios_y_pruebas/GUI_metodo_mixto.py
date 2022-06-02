from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Generador_de_aleatorios_y_pruebas.programa_mixto import metodo_mixto
from Generador_de_aleatorios_y_pruebas.GUI_mostrar_resultados import gui_resultados

class gui_metodo_mixto:

    def gui_mixto(self):
        gui = Tk()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        
        gui.title('Simulacion - Metodo mixto')
        gui.config(bg = '#88bea1')
        gui.resizable(0,0)
        gui.iconbitmap("Generador_de_aleatorios_y_pruebas/logo.ico")

        labeltitiulo = Label(gui, text = "Metodo mixto", bg = "#c0c1c3", font = "Times", width = "25", height= "2")
        labeltitiulo.place(relx=0.175, rely=0.125)

        label_semilla = Label(gui, text = "Semilla:", bg = "#cdced0", font = "Times", width = "7", height= "1")
        label_semilla.place(relx=0.175, rely=0.325)

        caja_semilla = StringVar()
        caja_semilla = ttk.Entry(gui,textvariable = caja_semilla,justify="center", width=18,font="Times")
        caja_semilla.place(relx=0.4, rely=0.327)

        label_iteraciones = Label(gui, text = "Iteraciones:", bg = "#cdced0", font = "Times", width = "8", height= "1")
        label_iteraciones.place(relx=0.175, rely=0.525)

        caja_iteraciones = StringVar()
        caja_iteraciones = ttk.Entry(gui,textvariable = caja_iteraciones,justify="center", width=17,font="Times")
        caja_iteraciones.place(relx=0.42, rely=0.527)


        def validaciones():
            try:
                size_seed = len(caja_semilla.get())
                if size_seed % 2 == 0:
                    semilla = int(caja_semilla.get())
                elif size_seed == 0:
                    messagebox.showerror("Error", "La semilla no puede estar vacía.")
                else:
                    caja_semilla.delete(0,END)
                    messagebox.showerror("Error", "La semilla dada de entrada es inválida.")
            except ValueError:
                caja_semilla.delete(0,END)
                messagebox.showerror("Error","La semilla contiene caractéres no válidos.")
            
            try:
                size_count = len(caja_iteraciones.get())
                if size_count == 0:
                    messagebox.showerror("Error","Las iteraciones no pueden estar vacías.")
                else:
                    iteraciones_temp = int(caja_iteraciones.get())
                    if iteraciones_temp <= 0:
                        caja_iteraciones.delete(0,END)
                        messagebox.showerror("Error", "El campo iteraciones no puede ser menor a 0.")
                    else:
                        iteraciones = int(caja_iteraciones.get())
                
            except ValueError:
                caja_iteraciones.delete(0,END)
                messagebox.showerror("Error","Las iteraciones contiene caractéres no válidos.")

            m_mix = metodo_mixto()
            aleatorios = m_mix.procedimiento_mixto(semilla,iteraciones)

            m_r = gui_resultados()
            m_r.gui_mostrar(aleatorios)


        boton_validar = Button(gui,text="Aceptar", command=validaciones, font="Times",bg="#cbc9bb")
        boton_validar.place(relx=0.275, rely=0.8)
        boton_validar.config(activebackground="#94A9B9", width="16", height="1")
        
        gui.mainloop()

'''m_mixto = gui_metodo_mixto()
m_mixto.gui_mixto()'''