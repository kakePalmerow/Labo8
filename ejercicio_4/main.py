"""
Reporte de ocupacion

DATOS
puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

IMPLEMENTA
1. resumir_filas(puestos): devuelve una lista de tuplas
   (numero_de_fila, ocupados, disponibles). Puedes utilizar sum().
2. transformar_estados(puestos, transformar): aplica la funcion recibida a cada
   estado mediante una comprension anidada. Devuelve una tabla nueva sin
   modificar el tablero original.
Llama a transformar_estados con una lambda que transforme 0 en "Disponible"
y 1 en "Ocupado".

COMPROBACIONES CON PRINT
- Resumen esperado: [(0, 2, 2), (1, 1, 3), (2, 3, 1)].
- Muestra la tabla de textos y el tablero original despues de transformarlo.
- Agrega un tablero propio con una unica fila y comprueba sus resultados.

ANALISIS EN COMENTARIOS
- Es correcto decir que una comprension evita recorrer los puestos? Explica.
- Cuantos estados se transforman en el ejemplo inicial?

COMMIT SUGERIDO
Completa ejercicio 4: reportes y transformacion de estados
"""

def resumir_filas(puestos):
    #Retorna lista de tuplas, donde la tupla tiene la forma
    #(numero_de_fila, ocupados, disponibles)
    #ocupados = Es la suma de cuantos elementos de la fila tienen 1
    #disponibles = Es la diferencia del total de puestos en una fila - ocupados
    return [
        (i, sum(fila), len(fila) - sum(fila))
            for i, fila in enumerate(puestos)
    ]
    


def transformar_estados(puestos, transformar):
    '''
        aplica la funcion recibida a cada
        estado mediante una comprension anidada. Devuelve una tabla nueva sin
        modificar el tablero original.
        Llama a transformar_estados con una lambda que transforme 0 en "Disponible"
        y 1 en "Ocupado".
    '''

    #Aplicar funcion recibida al elemento de cada puesto
    tabla_nueva = [[transformar(elemento) for elemento in fila] for fila  in puestos]
    
    return tabla_nueva

if __name__ == "__main__":
    puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    # TODO: agrega al menos un caso propio.
    
    #- Resumen esperado: [(0, 2, 2), (1, 1, 3), (2, 3, 1)].
    print(f"Resumen de puestos {("fila", "ocupados", "disponibles")}: {resumir_filas(puestos)}")
    # Muestra la tabla de textos y el tablero original despues de transformarlo.
    puestos_transformados=transformar_estados(puestos, lambda x: "Disponible" if x == 0 else "Ocupado")
    
    print(f"Resumen de puestos en texto: {puestos_transformados}")
    print(f"Puestos original: {puestos}\n")
    
    
    # Agrega un tablero propio con una unica fila y comprueba sus resultados.
    puestos_nuevo = [[0, 0, 0, 0,1], [0, 1, 1, 1,1], [1,0, 1, 1, 0]]
    
    print(f"Resumen de puestos {("fila", "ocupados", "disponibles")}:  {resumir_filas(puestos_nuevo)}")
    # Muestra la tabla de textos y el tablero original despues de transformarlo.
    puestos_transformados=transformar_estados(puestos_nuevo, lambda x: "Disponible" if x == 0 else "Ocupado")
        
    print(f"Resumen de puestos en texto: {puestos_transformados}")
    print(f"Puestos original: {puestos_nuevo}")