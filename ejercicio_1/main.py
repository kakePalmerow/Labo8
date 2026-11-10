"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    #Comprensión de diccionarios
    """
        puestos: Es una variable con estructura lista de listas
        En este caso, se puede analizar de dos formas
        
        A partir de la posición de los elementos en la lista de listas
        A partir de la posición de los elementos y los elementos en listas de listas
        
        
        En clases anteriores, hemos usado dos formas del ciclo for. Por ejemplo:
        
        posiciones      0        1        2
        productos = ["mango", "pera", "manzana"]
        len(productos) -> Retorna 3 en este ejemplo
        
        
        for i in range(len(productos)): Para obtener los indices de las posiciones de la lista
                                        En este ejemplo i toma los valores 0, 1 y 2
        
        for producto in productos:      Para obtener los elementos de la lista
                                        En este ejemplo producto toma los valores "mango", "pera" y "manzana"
                                        
        Hay una nueva forma, que funciona con enumerate
        for i, producto in enumerate(productos):    Para obtener tanto los indices de las posiciones de la lista, 
                                                    como los elementos de la misma.
                                                    En este ejemplo tenemos
                                                    
                                        Iteración | Valor i | Valor producto
                                            1          0         "mango"
                                            2          1         "pera"
                                            3          2         "manzana"

    """
    #Comprensión de diccionarios a partir de las posiciones en la lista de listas puestos
    # i posición de la fila
    # j posición en la columna
    # puestos[i][j]: Elemento en la fila i, columna j
    #                         Expresión   |          Recorrido de lista de listas      
    mapa_posicion = {(i, j): puestos[i][j] for i in range(len(puestos)) for j in range(len(puestos[i]))}    
    
    
    #Comprensión de diccionarios a partir de las posiciones en la lista de listas puestos
    #                            Expresión   |          Recorrido de lista de listas        
    mapa_enumerate = {(fila, columna): estado for fila, fila_elemento in enumerate(puestos) for columna, estado in enumerate(fila_elemento)}
    
    #Ambos retornan la misma forma, lo que cambia es el planteamiento de comprensión de diccionarios
    #print(f"Mapa posicion {mapa_posicion} - Mapa enumerate {mapa_enumerate}") 
    
    return mapa_posicion


def obtener_disponibles(puestos):
    """
    Enunciado pide
    
    obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
                                    Utiliza una comprension de conjuntos.
    """
    
    
    # Estructura de comprension
    #             Expresión     |          Recorrido de lista de listas                               |      Condición                                         
    resultado = {(fila, columna) for fila in range(len(puestos)) for columna in range(len(puestos[0])) if puestos[fila][columna] == 0}
    
    return resultado


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    
    
    # TODO: agrega al menos un caso propio.
    
    # Muestra el mapa completo y los disponibles.
    mapa = crear_mapa(puestos)
    puestos_disponibles = obtener_disponibles(puestos)
    
    print(f"Mapa disponible: {mapa} \nPuestos disponibles: {puestos_disponibles}")
    
    #Consulta el estado de (1, 2) en el mapa: debe ser 1.
    coordenada = (1,2)
    print(f"Estado de coordenada {coordenada}: {mapa[coordenada]}")
    
    #Agrega y comprueba otro tablero propio.
    nuevos_puestos = [[1, 1, 0, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0]]
    
    mapa = crear_mapa(nuevos_puestos)
    puestos_disponibles = obtener_disponibles(nuevos_puestos)
        
    print(f"Nuevo mapa disponible: {mapa} \nPuestos disponibles: {puestos_disponibles}")
        
    #Consulta el estado de (1, 2) en el mapa: debe ser 1.
    coordenada = (3,2)
    print(f"Estado de coordenada {coordenada}: {mapa[coordenada]}")
    
    
    

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
