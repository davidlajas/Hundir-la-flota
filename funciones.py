import numpy as np
import random

#Creación de tablero
def tablero(tamaño):
    return np.full((tamaño,tamaño),"#") #Hacemos un tablero de tamaño por tamaño


#Creación de flota
def crear_barco(eslora, tablero):
    eslora_base = 0 #definimos eslora base para ir igualando
    hori_vert = np.random.randint(0,1) #con esta variable se decide si va vertical u horizontalmente
    fila = np.random.randint(0,10-eslora) # se decide una fila al azar - la eslora para que no se salga del tabero
    columna = np.random.randint(0,10-eslora) # se decide una columna al azar - la eslora para que no se salga del tabero
    tablero[fila,columna] = "O"
    while eslora_base != eslora: #con este bucle seguirá añadiendo eslora hasta que se iguale al que hemos indicado en la lista
        if hori_vert == 0: #horizontal
            tablero[fila+eslora_base,columna] = "O"
            eslora_base = eslora_base +1 #cada vez que se ejecuta el bucle se añade uno al contador de la eslora base
            
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
    