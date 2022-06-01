
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Generador_de_aleatorios_y_pruebas.programa_multiplicativo import metodo_multiplicativo
from Generador_de_aleatorios_y_pruebas.GUI_mostrar_resultados import gui_resultados

class gui_metodo_multiplicativo:

    def gui_multiplicativo(self):
        gui = Toplevel()

        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)

        gui.title('Simulacion - Metodo multiplicativo')
        gui.config(bg = '#88bea1')
        gui.resizable(0,0)
        gui.iconbitmap("Generador_de_aleatorios_y_pruebas/logo.ico")

        labeltitiulo = Label(gui, text = "Metodo multiplicativo", bg = "#cdced0", font = "Times", width = "25", height= "2")
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
                if size_seed % 2 != 0:
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
            
            autoc = self.autoc
                    
            m_m = metodo_multiplicativo()
            aleatorios = m_m.procedimiento_multiplicativo(semilla,iteraciones,autoc)
            
            m_r = gui_resultados()
            m_r.gui_mostrar(aleatorios)
        

        def completado():
            s = select.get()
            if s == 1:
                self.autoc = True
            else:
                self.autoc = False
          
        select = IntVar()
        radio_autocompletado = Radiobutton(gui,text="Autoregenerado",value=1,bg="#cdced0",width=15,variable=select,command=completado)
        radio_autocompletado.place(relx=0.175, rely=0.645)

        radio_usuario = Radiobutton(gui,text="Sin regenerar",value=2,bg="#cdced0", width=15,variable=select,command=completado)
        radio_usuario.place(relx=0.52, rely=0.645)

        boton_validar = Button(gui,text="Aceptar", command=validaciones, font="Times",bg="#cbc9bb")
        boton_validar.place(relx=0.275, rely=0.8)
        boton_validar.config(activebackground="#94A9B9", width="16", height="1")
        gui.mainloop()


'''t = gui_metodo_multiplicativo()
t.gui_multiplicativo()
'''