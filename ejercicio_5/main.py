"""
Reto: reservas de grupos

DATOS
puestos = [[1, 0, 0], [0, 1, 0]]

IMPLEMENTA
reservar_grupo(puestos, coordenadas): recibe una lista de tuplas (fila, columna).
Supone que cada coordenada es una tupla de dos enteros y que el tablero es
rectangular, no vacio, con estados 0 o 1.
- Si la lista esta vacia, devuelve False.
- Si hay coordenadas repetidas, invalidas, negativas o puestos ocupados,
  devuelve False y NO modifica ninguna celda.
- Solo si todas las coordenadas son validas y disponibles, reserva todos los
  puestos (estado 1) y devuelve True.
Utiliza un set para detectar duplicados. Comprueba todas las condiciones
antes de modificar el tablero. No utilices input().

COMPROBACIONES CON PRINT
Usa una copia NUEVA del tablero inicial para CADA caso:
- [(0, 1), (1, 0)]: True.
- [(0, 1), (0, 1)]: False.
- [(0, 1), (0, 0)]: False.
- [(0, 1), (8, 0)]: False.
- []: False.
Muestra el tablero tras cada llamada. Agrega un caso propio.

ANALISIS EN COMENTARIOS
Por que no debes reservar cada puesto inmediatamente despues de comprobarlo,
antes de revisar el resto del grupo?

COMMIT SUGERIDO
Completa ejercicio 5: reserva de grupos sin cambios parciales
"""

def reservar_grupo(puestos, coordenadas):
    """
    reservar_grupo(puestos, coordenadas): recibe una lista de tuplas (fila, columna).
    Supone que cada coordenada es una tupla de dos enteros y que el tablero es
    rectangular, no vacio, con estados 0 o 1.
    - Si la lista esta vacia, devuelve False.
    - Si hay coordenadas repetidas, invalidas, negativas o puestos ocupados,
        devuelve False y NO modifica ninguna celda.
    - Solo si todas las coordenadas son validas y disponibles, reserva todos los
        puestos (estado 1) y devuelve True.
    Utiliza un set para detectar duplicados. Comprueba todas las condiciones
    antes de modificar el tablero. No utilices input().
    """
    #Verificar que lista de puestos o coordenadas esta vacia
    if not puestos or not coordenadas:
        return False
    
    #Verificar que coordenadas no esten repetidas
    if len(set(coordenadas))!=len(coordenadas):
        #Hay coordenadas distintas porque cantidad de set(coordenadas) != a cantidad de coordenadas
        return False
    
    #Coordenadas validas
    cantidad_filas = len(puestos)
    cantidad_columnas = len(puestos[0])
    
    #Verificar si coordenadas son validas> Como es una lista de tuplas
    for coordenada in coordenadas:
        fila, columna = coordenada
        #Si hay coordenadas repetidas, invalidas, negativas o puestos ocupados,
        #devuelve False y NO modifica ninguna celda.
        if 0<=fila<cantidad_filas and 0<=columna<cantidad_columnas:
            #Verificar si el puesto esta ocupado
            if puestos[fila][columna] == 1:
                return False
        else: 
            return False
        
    #Reservar una vez validado todo (otra forma de hacer for, como se sabe que coordenadas es una tupla)
    for fila, columna in coordenadas:
        puestos[fila][columna] = 1
    return True


if __name__ == "__main__":
    puestos = [[1, 0, 0], [0, 1, 0]]

    """
    COMPROBACIONES CON PRINT
    Usa una copia NUEVA del tablero inicial para CADA caso:
    - [(0, 1), (1, 0)]: True.
    - [(0, 1), (0, 1)]: False.
    - [(0, 1), (0, 0)]: False.
    - [(0, 1), (8, 0)]: False.
    - []: False.
    Muestra el tablero tras cada llamada. Agrega un caso propio.
    """
    print(f"Tablero original: {puestos}")
    coordenadas = [(0, 1), (1, 0)]
    print(f"Verificar si se puede reservar para el grupo de coordenadas {coordenadas}: {reservar_grupo(puestos, coordenadas)}")
    print(f"Tablero después de intento de reserva: {puestos}")
    
    coordenadas = [(0, 1), (0, 1)]
    print(f"Verificar si se puede reservar para el grupo de coordenadas {coordenadas}: {reservar_grupo(puestos, coordenadas)}")
    print(f"Tablero después de intento de reserva: {puestos}")
    
    
    coordenadas = [(0, 1), (0, 0)]
    print(f"Verificar si se puede reservar para el grupo de coordenadas {coordenadas}: {reservar_grupo(puestos, coordenadas)}")
    print(f"Tablero después de intento de reserva: {puestos}")
    
    
    coordenadas = [(0, 1), (8, 0)]
    print(f"Verificar si se puede reservar para el grupo de coordenadas {coordenadas}: {reservar_grupo(puestos, coordenadas)}")
    print(f"Tablero después de intento de reserva: {puestos}")
    
    
    coordenadas = []
    print(f"Verificar si se puede reservar para el grupo de coordenadas {coordenadas}: {reservar_grupo(puestos, coordenadas)}")
    print(f"Tablero después de intento de reserva: {puestos}")
# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
