# Hundir-la-flota - Python

## Descripción
Este repositorio contiene una implementación del clásico juego **Hundir la flota** en Python.  
El juego enfrenta a un jugador contra la CPU en un tablero de 10x10. Ambos colocan barcos de manera aleatoria y disparan por turnos hasta que uno de los dos logra hundir todos los barcos del oponente.

El juego incluye:
- Tableros de 10x10 para el jugador y la CPU.
- Colocación automática de barcos según la lista de esloras definida.
- Turnos alternos entre jugador y CPU.
- Registro de disparos y actualización de aciertos.
- Mensajes claros que indican si un disparo es "Tocado", "Agua" o inválido.


## Cómo jugar
1. Ejecuta el script principal:
   ```bash
   python main.py
2. Introduce las coordenadas de fila y columna para disparar. Deben ser números del 1 al 10.

3. El juego indica si el disparo fue un acierto sobre un barco ("Tocado") o un fallo ("Agua").

4. La CPU realiza sus disparos automáticamente después del turno del jugador.

5. La partida termina cuando uno de los dos jugadores hunde todos los barcos del oponente.

6. Al final de la partida se muestra un resumen con los tableros del jugador y de la CPU, incluyendo barcos y disparos realizados.