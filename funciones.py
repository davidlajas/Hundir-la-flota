import numpy as np
import random

#Creación de tablero
def tablero(tamaño):
    return np.full((tamaño,tamaño),"#")


#Creación de flota
def crear_barco(eslora, tablero):
    eslora_base = 0
    hori_vert = np.random.randint(0,1)
    fila = np.random.randint(0,10-eslora)
    columna = np.random.randint(0,10-eslora)
    tablero[fila,columna] = "O"
    while eslora_base != eslora:
        if hori_vert == 0: #horizontal
            tablero[fila+eslora_base,columna] = "O"
            eslora_base = eslora_base +1
            
        else: #vertical
            tablero[fila,columna+eslora_base] = "O"
            eslora_base = eslora_base +1

#Disparar

def disparar(fila,columna,tablero,tablero_oculto):
    if tablero_oculto[fila,columna] == "O":
        tablero[fila,columna] = "O"
        return "Tocado"
    elif tablero_oculto[fila,columna] == "#" :
        tablero[fila,columna] = "A"
        return "Agua"
    else: 
        return "Error"