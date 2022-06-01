from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Generador_de_aleatorios_y_pruebas.programa_komolgorov import pruebas_komolgorov

class gui_Komolgorov_smirnoff:

    def gui_komolgorov(self):
        gui = Tk()
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = gui.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = gui.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        gui.geometry(posicion)
        gui.title('Simulacion - Komolgorov-Smirnoff')
        gui.config(bg = '#88bea1')
        gui.resizable(0,0)
        gui.iconbitmap("Generador_de_aleatorios_y_pruebas/logo.ico")

        labeltitiulo = Label(gui, text = "Komolgorov - Smirnoff", bg = "#c0c1c3", font = "Times", width = "25", height= "2")
        labeltitiulo.place(relx=0.175, rely=0.125)

        label_archivo = Label(gui, text = "Nombre del archivo:", bg = "#cdced0", font = "Times", width = "26", height= "1")
        label_archivo.place(relx=0.176, rely=0.35)

        entry_archivo = StringVar()
        entry_archivo = Entry(gui, width = "28", font = "Times", textvariable=entry_archivo,justify="center")
        entry_archivo.place(relx=0.169, rely=0.45)

        label_alpha = Label(gui, text = "Alpha:", bg = "#cdced0", font = "Times", width = "26", height= "1")
        label_alpha.place(relx=0.175, rely=0.55)

        entry_alpha = StringVar()
        entry_alpha = Entry(gui, width = "28", font = "Times", textvariable=entry_alpha,justify="center")
        entry_alpha.place(relx=0.179, rely=0.65)


        def acciones():

            archivo = entry_archivo.get()
            alpha = float(entry_alpha.get())
                
            if archivo == "":
                messagebox.showerror("Error", "Debe ingresar el nombre del archivo")
            if alpha == "":
                messagebox.showerror("Error", "Debe ingresar el valor de alpha")
            else:
                archivo = entry_archivo.get()
                alpha = entry_alpha.get()
                alpha = float(alpha)

            archivo_completo = archivo + ".txt"

            try:
                archivo = open(archivo_completo, "r")
                lineas = archivo.readlines()
                archivo.close()

                aleatorios = []
                for linea in lineas:
                    linea = linea.strip()
                    aleatorios.append(float(linea))

                pf = pruebas_komolgorov()
                pf.procedimiento_komolgorov(aleatorios, alpha)

            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo no existe")

        bunidad = Button(gui, text = "Seleccionar", bg = '#cbc9bb', command = acciones, font = "Times")
        bunidad.place(relx=0.275, rely=0.8)
        bunidad.config(activebackground="#94A9B9", width="16", height="1")
        
        gui.mainloop()