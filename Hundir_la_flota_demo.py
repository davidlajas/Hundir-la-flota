import numpy as np

import random

from funciones import *


colocacion = False 

while colocacion == False: #Si es False sigue el bucle hasta que coloca correctamente los barcos

    tablero_jugador = tablero(10)

    tablero_jugador_oculto = tablero_jugador.copy()

    tablero_CPU = tablero(10)

    tablero_CPU_oculto = tablero_CPU.copy()

    #Introducimos una lista en la que el número indica el la cantidad de esloras.
    lista_barcos = [2] 

    #Creamos de forma aleatoria las posiciones donde colocamos los barcos
    for eslora in lista_barcos:
        crear_barco(eslora,tablero_jugador_oculto)

    #Número de esloras totales por cada tablero oculto
    sum_esl =0
    for eslora in lista_barcos:
        sum_esl = sum_esl + eslora

    #Casillas ocupadas por "O" en jugador
    count_O_jug_oculto = np.sum(tablero_jugador_oculto == "O")

    #Creamos de forma aleatoria las posiciones donde colocamos los barcos
    for eslora in lista_barcos:
        crear_barco(eslora,tablero_CPU_oculto)

    #casillas ocupadas por "O" en CPU
    count_O_CPU_oculto = np.sum(tablero_CPU_oculto == "O")

    #Igualamos las esloras de cada tablero oculto al número de esloras que debería

    if count_O_CPU_oculto != sum_esl or count_O_jug_oculto != sum_esl:
        colocacion = False
    else: # Si coinciden las 3 variables se rompe el bucle y comienza la partida
        colocacion = True
        break

print(tablero_CPU_oculto) #solo aparece en la demo para probar
print("Flotas colocadas... ¡que comience la partida!")

#Número de aciertos de la CPU. Para definir variables. Va a ser 0 porque no ha habido aciertos.
count_O_jug = np.sum(tablero_jugador == "O")

#Número de aciertos del jugador. Para definir variables. Va a ser 0 porque no ha habido aciertos.
count_O_CPU = np.sum(tablero_CPU == "O")

#El 0 indica que es mi turno, el 1 que es el de la CPU
turno = 0

#Comenzamos el bucle y hasta que el número de aciertos de uno de los dos no sea igual al número de esloras no termina
while count_O_CPU != count_O_CPU_oculto and count_O_jug != count_O_jug_oculto:

    if turno == 0:
        print("Turno del jugador")
        print(tablero_CPU) #Al principio de cada turno indicamos cómo va el tablero con los barcos del enemigo
        try: #Intentamos que si no es un número del 1 al 10 dé error
            fila = int(input("Introduce la fila. Elige un número del 1 al 10: "))-1
            if fila > 9 or fila < 0 or not isinstance(fila,int):
                print("No entra dentro de los parámetros ofrecidos")
                fila = "Error"
        except: fila = "Error"

        try: #Intentamos que si no es un número del 1 al 10 dé error
            columna = int(input("Introduce la columna. Elige un número del 1 al 10: "))-1
            if columna > 9 or columna < 0 or not isinstance(columna,int):
                print("No entra dentro de los parámetros ofrecidos")
                columna = "Error"
                turno = 0
        except: columna = "Error"
        
        try: #Dispara el jugador
            disparar(fila,columna,tablero_CPU,tablero_CPU_oculto)
            resultado = disparar(fila,columna,tablero_CPU,tablero_CPU_oculto)
        except: resultado = "Error"
        
        if resultado == "Error":
            print(resultado)
            turno = 0 #Si da error se deja intentar de nuevo
        elif resultado == "Tocado":
            print(resultado)
            count_O_CPU = np.sum(tablero_CPU == "O") #Actualizamos los aciertos
            turno = 0
        elif resultado == "Agua": #Si no se acierta se pasa de turno
            print(resultado)
            turno = 1
        try:
            print(f"Disparo en: {fila+1},{columna+1}") #Indica dónde se ha disparado
        except: print("Alguno de los datos indicados no entra dentro de los parámetros ofrecidos. Inténtalo de nuevo")
        del fila #Borramos las variables para que no haya errores
        del columna #Borramos las variables para que no haya errores

    else: #Cuando turno es igual a 1
        print("Turno de la CPU")
        print(tablero_jugador)
        fila = random.randint(0,9) #Números aleatorio
        columna = random.randint(0,9)#Números aleatorio
        disparar(fila,columna,tablero_jugador,tablero_jugador_oculto)
        resultado = disparar(fila,columna,tablero_jugador,tablero_jugador_oculto)
        if resultado == "Tocado":
            print(resultado)
            count_O_jug = np.sum(tablero_jugador == "O") #Actualizamos los aciertos
            turno = 1
        else: print(resultado) 
        turno = 0
        print(f"Disparo en: {fila+1},{columna+1}")


if count_O_jug == sum_esl: #Si los aciertos son en el tablero del jugador gana la CPU
        print("Has perdido, gana la CPU")
else:
        print("¡Enhorabuena, has ganado!")

#Imprimimos un resumen de la partida
print("Resumen de la partida")    
print("-"*20)
print("Tablero de barcos de la CPU")
print("-"*20)
print(tablero_CPU_oculto)
print("-"*20)
print("Tablero disparos CPU")
print("-"*20)
print(tablero_jugador)
print("-"*20)
print("Tablero de barcos del jugador")
print("-"*20)