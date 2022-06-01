
import random

class metodo_mixto:

    def procedimiento_mixto(self, semilla, iteraciones):
        compactador = True
        while compactador:
            lista_a = []
            lista_c = []
            cont = 0
            flag = False

            while not flag:
                a = random.randrange(1,1000)
                if a % 3 != 0 and a % 5 != 0 and a-1 % 4 == 0:
                    lista_a.append(a)
                    cont += 1

                if cont == 10:
                    flag = True

            flag = False
            cont = 0
            while not flag:
                c = random.randrange(1,1000)
                if c % 8 == 5:
                    lista_c.append(c)
                    cont += 1
                if cont == 10:
                    flag = True

            lista_a.sort()
            lista_c.sort()

            lista_mayores = [lista_a[0], lista_c[0]]

            finish = False
            potencia = 1
            while not finish:
                m = 2 ** potencia

                if m > lista_mayores[0] and m > lista_mayores[1] and m > semilla:
                    lista_mayores.append(m)
                    finish = True
                else:
                    potencia = potencia + 2
            break

        a = lista_mayores[0]
        c = lista_mayores[1]
        m = lista_mayores[2]
        print(a, c, m)

        randoms = []

        for i in range(iteraciones):
            precalculo = ((a*semilla) + c)
            aleatorio = int(precalculo) % m
            semilla = aleatorio
            randoms.append(aleatorio)
        
        return(randoms)

'''m_mixto = metodo_mixto()
m_mixto.procedimiento_mixto(1238,1238)              
'''