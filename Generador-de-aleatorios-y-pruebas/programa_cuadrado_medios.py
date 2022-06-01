
from tkinter import *
from tkinter import messagebox
import random

class metodo_multiplicativo:

    def procedimiento_multiplicativo(self):
        semillas_generadas = []
        container = 0
        validador = False

        while not validador:
            main_seed = int(input("Ingrese la semilla: "))
            first_string_seed = str(main_seed)

            if len(first_string_seed) <=3:
                print("Ingrese una semilla válida para poder aplicar el método.")
            else:
                validador = True

        iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

        validador = False
        while not validador:
            activador = int(input("Ingrese si será autocompletado el programa: 1:Y / 2:N "))
            if activador == 1:
                autocompletado = True
                validador = True

            elif activador == 2:
                autocompletado = False
                validador = True
            
            else:
                print("Ingrese una opción válida y vuelva a intentarlo.")


        while container <= iteraciones:
                
            size = len(first_string_seed)

            if size % 2 == 0:
                seed_string = str(main_seed)
                
                    
                if len(seed_string) != size:
                    #messagebox.showerror("Error", "El valor introducido no puede ser usado como semilla.")
                    if autocompletado == False:
                        print("")
                        print("La semilla ha fallado en la iteracion " + str(container) +" y no puede producir más numeros.")
                        main_seed = int(input("Ingrese una nueva semilla para continuar con el proceso: "))
                        
                    else:
                        string_minima = "1"
                        string_maxima = "1"
                            
                        for i in range(size-1):
                            string_minima = string_minima + "0"

                        for i in range(size):
                            string_maxima = string_maxima + "0"
                            
                        rango_min = int(string_minima)
                        rango_max = int(string_maxima)

                        main_seed = random.randrange(rango_min, rango_max)
                        print(main_seed)
                    
                else:
                    new_seed = main_seed ** 2
                    new_seed_string = str(new_seed)
                    new_size = len(new_seed_string)

                    if new_size == (size * 2):
                        min = int((size / 2 ) - 1)
                        max = int(min + size)
                        final_seed = new_seed_string[min:max]
                        main_seed = int(final_seed)
                        semillas_generadas.append(final_seed)
                        container += 1

                    else:
                        diferent_len = (size * 2) - new_size
                            
                        for i in range(diferent_len):
                            new_seed_string = "0" + new_seed_string

                        min = int((size / 2 ) - 1)
                        max = int(min + size)
                        final_seed = new_seed_string[min:max]
                        main_seed = int(final_seed)
                        semillas_generadas.append(final_seed)
                        container += 1

            else:
                #messagebox.showerror("Error", "El valor introducido no puede ser usado como semilla.")
                if len(semillas_generadas) == 0:
                    print("")
                    print("El valor introducido no puede ser usado como semillaaa.")
                    main_seed = int(input("Ingrese una semilla válida para continuar con el proceso: "))

                else:
                    if autocompletado == False:
                        print("")
                        print("La semilla ha fallado en la iteracion " + str(container) +" y no puede producir más numeros.")
                        main_seed = int(input("Ingrese una nueva semilla para continuar con el proceso: "))
                        
                    else:
                        string_minima = "1"
                        string_maxima = "1"
                            
                        for i in range(size-1):
                            string_minima = string_minima + "0"

                        for i in range(size):
                            string_maxima = string_maxima + "0"
                            
                        rango_min = int(string_minima)
                        rango_max = int(string_maxima)

                        main_seed = random.randrange(rango_min, rango_max)
                        print(main_seed)
        print("")
        print("Proceso de generacion terminado")
        print(semillas_generadas)

mul = metodo_multiplicativo()
mul.procedimiento_multiplicativo()