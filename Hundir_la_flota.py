import numpy as np

import random

from funciones import *


colocacion = False 

while colocacion == False: 

    tablero_jugador = tablero(10)

    tablero_jugador_oculto = tablero_jugador.copy()

    tablero_CPU = tablero(10)

    tablero_CPU_oculto = tablero_CPU.copy()

    
    lista_barcos = [2] 

    
    for eslora in lista_barcos:
        crear_barco(eslora,tablero_jugador_oculto)

    
    sum_esl =0
    for eslora in lista_barcos:
        sum_esl = sum_esl + eslora

    
    count_O_jug_oculto = np.sum(tablero_jugador_oculto == "O")

    
    for eslora in lista_barcos:
        crear_barco(eslora,tablero_CPU_oculto)

    
    count_O_CPU_oculto = np.sum(tablero_CPU_oculto == "O")

    

    if count_O_CPU_oculto != sum_esl or count_O_jug_oculto != sum_esl:
        colocacion = False
    else: 
        colocacion = True
        break

print("Flotas colocadas... ¡que comience la partida!")


count_O_jug = np.sum(tablero_jugador == "O")


count_O_CPU = np.sum(tablero_CPU == "O")


turno = 0


while count_O_CPU != count_O_CPU_oculto and count_O_jug != count_O_jug_oculto:

    if turno == 0:
        print("Turno del jugador")
        print(tablero_CPU) 
        try: 
            fila = int(input("Introduce la fila. Elige un número del 1 al 10: "))-1
            if fila > 9 or fila < 0 or not isinstance(fila,int):
                print("No entra dentro de los parámetros ofrecidos")
                fila = "Error"
        except: fila = "Error"

        try: 
            columna = int(input("Introduce la columna. Elige un número del 1 al 10: "))-1
            if columna > 9 or columna < 0 or not isinstance(columna,int):
                print("No entra dentro de los parámetros ofrecidos")
                columna = "Error"
                turno = 0
        except: columna = "Error"
        
        try: 
            disparar(fila,columna,tablero_CPU,tablero_CPU_oculto)
            resultado = disparar(fila,columna,tablero_CPU,tablero_CPU_oculto)
        except: resultado = "Error"
        
        if resultado == "Error":
            print(resultado)
            turno = 0 
        elif resultado == "Tocado":
            print(resultado)
            count_O_CPU = np.sum(tablero_CPU == "O") 
            turno = 0
        elif resultado == "Agua": 
            print(resultado)
            turno = 1
        try:
            print(f"Disparo en: {fila+1},{columna+1}") 
        except: print("Alguno de los datos indicados no entra dentro de los parámetros ofrecidos. Inténtalo de nuevo")
        del fila 
        del columna 

    else: 
        print("Turno de la CPU")
        print(tablero_jugador)
        fila = random.randint(0,9) 
        columna = random.randint(0,9)
        disparar(fila,columna,tablero_jugador,tablero_jugador_oculto)
        resultado = disparar(fila,columna,tablero_jugador,tablero_jugador_oculto)
        if resultado == "Tocado":
            print(resultado)
            count_O_jug = np.sum(tablero_jugador == "O") 
            turno = 1
        else: print(resultado) 
        turno = 0
        print(f"Disparo en: {fila+1},{columna+1}")


if count_O_jug == sum_esl:
        print("Has perdido, gana la CPU")
else:
        print("¡Enhorabuena, has ganado!")

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