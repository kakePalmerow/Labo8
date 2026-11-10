"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""

def reservar_puesto(puestos, coordenada):
    # TODO: implementa esta funcion.
    """
    reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
        esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
    """
    
    #Verificar si la coordenada es valida
    fila, columna = coordenada
    
    cantidad_filas = len(puestos)
    cantidad_columnas = len(puestos[0])
    
    #Las coordenadas validas son aquellas posiciones validas, es decir, aquellas que sean menores a la cantidad de filas que hay disponibles
    # y menores que la cantidad de columnas que hay disponibles
    if 0<=fila<cantidad_filas and 0<=columna<cantidad_columnas:
        #Verificar si el puesto está disponible
        if puestos[fila][columna] == 0:
            puestos[fila][columna] = 1 #Se reserva el puesto
            return True
    
    return False


def liberar_puesto(puestos, coordenada):
    """
        2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
        esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
    """
    
    #Verificar si la coordenada es valida
    fila, columna = coordenada
        
    cantidad_filas = len(puestos)
    cantidad_columnas = len(puestos[0])
        
    #Las coordenadas validas son aquellas posiciones validas, es decir, aquellas que sean menores a la cantidad de filas que hay disponibles
    # y menores que la cantidad de columnas que hay disponibles
    if 0<=fila<cantidad_filas and 0<=columna<cantidad_columnas:
        #Verificar si el puesto está ocupado
        if puestos[fila][columna] == 1:
            puestos[fila][columna] = 0 #Se libera el puesto
            return True
    
    return False
    

if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    # TODO: agrega al menos un caso propio.
    
    """
    COMPROBACIONES CON PRINT
    Realiza en orden, sobre el mismo tablero:
    - Reservar (0, 1): True.
    - Reservar otra vez (0, 1): False.
    - Liberar (1, 2): True.
    - Liberar otra vez (1, 2): False.
    - Reservar (5, 0): False.
    - Reservar (-1, 0): False.
    Muestra el tablero final y agrega una comprobacion propia.
    """
    
    print(f"Puestos Iniciales: {puestos}")
    print(f"Reservar {(0,1)}: {reservar_puesto(puestos, (0,1))}")
    print(f"Reservar {(0,1)}: {reservar_puesto(puestos, (0,1))}")
    coordenada = (1,2)
    print(f"Liberar {coordenada}: {liberar_puesto(puestos, coordenada)}")
    print(f"Liberar {coordenada}: {liberar_puesto(puestos, coordenada)}")
    coordenada = (5,0)
    print(f"Reservar {coordenada}: {reservar_puesto(puestos, coordenada)}")
    coordenada = (-1,0)
    print(f"Reservar {coordenada}: {reservar_puesto(puestos, coordenada)}")
    print(f"Puestos Finales: {puestos}")
    
    
    

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
