"""
Reto: varios laboratorios

DATOS
laboratorios = {
    "A": [[1, 0, 0], [0, 1, 0]],
    "B": [[1, 1], [1, 1]],
    "C": [[0, 0, 0]]
}

IMPLEMENTA
1. resumir_laboratorios(laboratorios): devuelve un diccionario con cada nombre
   como clave y una tupla (total_de_puestos, ocupados, disponibles) como valor.
2. laboratorios_con_cupo(resumen, cantidad): devuelve un set con los nombres
   de los laboratorios con al menos cantidad puestos disponibles.
   Si cantidad <= 0, devuelve un set vacio.
No modifiques los datos recibidos. Puedes utilizar sum().

COMPROBACIONES CON PRINT
- Resumen esperado: {"A": (6, 2, 4), "B": (4, 4, 0), "C": (3, 0, 3)}.
- Para cantidad 3: {"A", "C"}.
- Para cantidad 4: {"A"}.
- Para cantidad 5: set vacio.
- Comprueba tambien cantidad 0.
- Agrega un laboratorio propio y repite las consultas.
El orden de los elementos de un set no importa.

ANALISIS EN COMENTARIOS
Usa P para el total de puestos y L para el numero de laboratorios.
Que elementos revisa cada funcion? Justifica sus complejidades por separado.

COMMIT SUGERIDO
Completa ejercicio 6: resumen de multiples laboratorios
"""

def resumir_laboratorios(laboratorios):
    # Laboratorios es un diccionario. Clave corresponde al nombre del laboratorio, valor es una lista de puestos
    
    """
    devuelve un diccionario con cada nombre
    como clave y una tupla (total_de_puestos, ocupados, disponibles) como valor.
    """
    resumen = {}            #Diccionario vacio
    #Recorrer diccionario y generar tupla
    for laboratorio, puestos in laboratorios.items():
        total = 0
        ocupados = 0
        
        for puesto in puestos: #Recorre cada fila de cada puesto en laboratorio
            total += len(puesto)
            ocupados += sum(puesto)
            
        #Se crea clave-valor diccionario
        #                    = (total_puestos, total_ocupados, total_disponibles)
        resumen[laboratorio] = (total, ocupados, total-ocupados)
        
    return resumen
        
        


def laboratorios_con_cupo(resumen, cantidad):
    """
        laboratorios_con_cupo(resumen, cantidad): devuelve un set con los nombres
        de los laboratorios con al menos cantidad puestos disponibles.
        Si cantidad <= 0, devuelve un set vacio.
    """
    if cantidad <= 0:
        return set()
    
    #La tupla totales tiene la forma (total_puestos, total_ocupados, total_disponibles)
    #La posicion 2 corresponde al total disponibles
    return {laboratorio for laboratorio, totales in resumen.items() if totales[2]>=cantidad}


if __name__ == "__main__":
    laboratorios = {
        "A": [[1, 0, 0], [0, 1, 0]],
        "B": [[1, 1], [1, 1]],
        "C": [[0, 0, 0]]
    }
    
    """
    - Resumen esperado: {"A": (6, 2, 4), "B": (4, 4, 0), "C": (3, 0, 3)}.
    - Para cantidad 3: {"A", "C"}.
    - Para cantidad 4: {"A"}.
    - Para cantidad 5: set vacio.
    - Comprueba tambien cantidad 0.
    - Agrega un laboratorio propio y repite las consultas.
    """
    
    resumen = resumir_laboratorios(laboratorios)
    
    print(f"Laboratorios: {laboratorios}")
    print(f"Resumen laboratorios: {resumen}")
    cantidad = 3
    laboratorios_cupos = laboratorios_con_cupo(resumen, cantidad)
    print(f"Los laboratorios con cupo para {cantidad}: {laboratorios_cupos}")
    
    
    cantidad = 4
    laboratorios_cupos = laboratorios_con_cupo(resumen, cantidad)
    print(f"Los laboratorios con cupo para {cantidad}: {laboratorios_cupos}")
    
    
    cantidad = 5
    laboratorios_cupos = laboratorios_con_cupo(resumen, cantidad)
    print(f"Los laboratorios con cupo para {cantidad}: {laboratorios_cupos}")
    
    cantidad = 0
    laboratorios_cupos = laboratorios_con_cupo(resumen, cantidad)
    print(f"Los laboratorios con cupo para {cantidad}: {laboratorios_cupos}")



# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
