from tkinter import *
from tkinter import ttk

from GUI_metodo_multiplicativo import gui_metodo_multiplicativo
from GUI_metodo_mixto import gui_metodo_mixto
from GUI_prueba_frecuencias import gui_prueba_frecuencias
from GUI_komolgorov import gui_Komolgorov_smirnoff

class main_gui:
    def gui_principal(self):
        mainwindow = Tk()
        
        ancho_ventana = 425
        alto_ventana = 400
        x_ventana = mainwindow.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = mainwindow.winfo_screenheight()// 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        mainwindow.geometry(posicion)

        mainwindow.title('Simulacion - Programa integrador')
        mainwindow.config(bg = '#88bea1')
        mainwindow.resizable(0,0)
        mainwindow.iconbitmap("logo.ico")

        
        labeltitiulo = Label(mainwindow, text = "SIMULACION", bg = "#c0c1c3", font = "Times", width = "25", height= "2")
        labeltitiulo.place(relx=0.175, rely=0.125)

        options = [
            "Metodo multiplicativo",
            "Metodo mixto",
            "Prueba de frecuencias",
            "Komolgorov - Smirnov",
        ]
        cmb = ttk.Combobox(mainwindow, width=21, values=options, state="readonly", font = "Times", height="1", justify = "center")
        cmb.place(relx=0.215,rely=0.475)
        cmb.current(0)

        def acciones():
            if cmb.get() == "Metodo multiplicativo":
                m_m = gui_metodo_multiplicativo()
                m_m.gui_multiplicativo()

            if cmb.get() == "Metodo mixto":
                m_mix = gui_metodo_mixto()
                m_mix.gui_mixto()

            if cmb.get() == "Prueba de frecuencias":
                f = gui_prueba_frecuencias()
                f.gui_frecuencias()

            if cmb.get() == "Komolgorov - Smirnov":
                k = gui_Komolgorov_smirnoff()
                k.gui_komolgorov()
    
        bunidad = Button(mainwindow, text = "Seleccionar", bg = '#cbc9bb', command = acciones, font = "Times")
        bunidad.place(relx=0.275, rely=0.8)
        bunidad.config(activebackground="#94A9B9", width="16", height="1")
        mainwindow.mainloop()

gui = main_gui()
gui.gui_principal()