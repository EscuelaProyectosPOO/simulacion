from tkinter import simpledialog
from tkinter import messagebox
import random

class metodo_multiplicativo:
    def procedimiento_multiplicativo(slef,semilla,iteraciones,autoc):

        
        main_seed = semilla
        main_string_seed  = str(main_seed)
        main_seed_size = len(main_string_seed)

        iteraciones = iteraciones

        auto = autoc
        
        e = 10**(main_seed_size/2)
        
        diferencia = random.randrange(1,11)
        carga = random.randrange(1,3)

        if carga == 1:
            a = int(e + diferencia)
        else:
            a = int(e - diferencia)

        randoms = []
        for i in range(iteraciones):
            eval_seed = main_seed * a
            finish_string_seed = str(eval_seed)
            long = (main_seed_size) * -1
            last_size = len(finish_string_seed)

            if last_size != (2 * main_seed_size):
               
                dif = 2 * main_seed_size - last_size  
                
                for j in range(dif):
                    finish_string_seed = "0" + finish_string_seed
                
                last_seed = int(finish_string_seed[long:])
                last_size = len(str(last_seed))

                if last_size == main_seed_size:
                    main_seed = int(last_seed)
                    randoms.append(main_seed)
                
                else:
                    if auto == True:
                        min = "1"
                        max = "1"

                        for k in range(main_seed_size -1):
                            min = min + "0"
                        
                        for k in range(main_seed_size):
                            max = max + "0"

                        main_seed = random.randrange(int(min), int(max))
                        randoms.append(main_seed)

                    else:
                        messagebox.showerror("Error","La semilla ha fallado en la iteracion " + str(i) +".")

                        ciclo = True
                        while ciclo:
                            semilla_temporal = simpledialog.askinteger("Aviso","Ingrese una nueva semilla para continuar con el proceso:")

                            if semilla_temporal is not None:
                                size_semilla_temporal = len(str(semilla_temporal))

                                if size_semilla_temporal % 3 == 0:
                                    main_seed = semilla_temporal
                                    break
                                else:
                                    messagebox.showerror("Error", "La semilla no es válida.")
                            else:
                                messagebox.showerror("Error", "La semilla no puede quedar vacía.")

            else:
                last_seed = int(finish_string_seed[long:])
                last_size = len(str(last_seed))

                if last_size == main_seed_size:
                    main_seed = int(last_seed)
                    randoms.append(main_seed)

                else:
                    if auto == True:
                        min = "1"
                        max = "1"

                        for k in range(main_seed_size -1):
                            min = min + "0"
                        
                        for k in range(main_seed_size):
                            max = max + "0"

                        main_seed = random.randrange(int(min), int(max))
                        randoms.append(main_seed)

                    else:
                        messagebox.showerror("Error","La semilla ha fallado en la iteracion " + str(i) +".")

                        ciclo = True
                        while ciclo:
                            semilla_temporal = simpledialog.askinteger("Aviso","Ingrese una nueva semilla para continuar con el proceso:")

                            if semilla_temporal is not None:
                                size_semilla_temporal = len(str(semilla_temporal))

                                if size_semilla_temporal % 3 == 0:
                                    main_seed = semilla_temporal
                                    break
                                else:
                                    messagebox.showerror("Error", "La semilla no es válida.")
                            else:
                                messagebox.showerror("Error", "La semilla no puede quedar vacía.")

        #print(randoms)
        return randoms                   
