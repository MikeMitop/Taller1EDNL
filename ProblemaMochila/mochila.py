def mochila_01(capacidad_maxima, lista_pesos, lista_valores):
   
    if len(lista_pesos) != len(lista_valores):
        raise ValueError("Las listas de pesos y valores deben tener la misma longitud")

    num_objetos = len(lista_pesos)
    # tabla_resultados[i][j] = valor máximo posible usando los primeros i objetos
    # con una capacidad de mochila _
    tabla_resultados = [[0] * (capacidad_maxima + 1) for _ in range(num_objetos + 1)]

    # Llenar la tabla de resultados usando programación dinámica 
    for i in range(1, num_objetos + 1):
        objeto_actual = i - 1  # Índice real del objeto en las listas originales
        for capacidad_actual in range(1, capacidad_maxima + 1):
            if lista_pesos[objeto_actual] > capacidad_actual:
                # El objeto no cabe en la capacidad actual, mantenemos el valor anterior
                tabla_resultados[i][capacidad_actual] = tabla_resultados[i-1][capacidad_actual]
            else:
                # Decidir si es mejor incluir o no el objeto actual
                valor_incluyendo = lista_valores[objeto_actual] + tabla_resultados[i-1][capacidad_actual - lista_pesos[objeto_actual]]
                valor_excluyendo = tabla_resultados[i-1][capacidad_actual]
                tabla_resultados[i][capacidad_actual] = max(valor_incluyendo, valor_excluyendo)

    # Reconstruir la solución para encontrar qué objetos fueron seleccionados
    objetos_seleccionados = []
    capacidad_restante = capacidad_maxima
    
    # Recorrer la tabla desde el final para identificar los objetos incluidos
    for i in range(num_objetos, 0, -1):
        objeto_actual = i - 1  # Índice real del objeto
        # Si el valor cambió respecto a la fila anterior, este objeto fue incluido
        if tabla_resultados[i][capacidad_restante] != tabla_resultados[i-1][capacidad_restante]:
            objetos_seleccionados.append(objeto_actual)
            capacidad_restante -= lista_pesos[objeto_actual]
            
    objetos_seleccionados.reverse()  # Para mostrarlos en orden creciente

    return tabla_resultados[num_objetos][capacidad_maxima], objetos_seleccionados


if __name__ == "__main__":
    lista_pesos = [10, 20, 30]
    lista_valores = [60, 100, 120]
    capacidad_maxima = 50

    valor_maximo, objetos = mochila_01(capacidad_maxima, lista_pesos, lista_valores)

    print("EJEMPLO BÁSICO DEL PROBLEMA DE LA MOCHILA 0/1")
    print("=" * 50)
    print("Objetos disponibles:")
    print(f"{'Índice':<8} {'Peso':<8} {'Valor':<8} {'Ratio V/P':<10}")
    print("-" * 40)
    for i, (p, v) in enumerate(zip(lista_pesos, lista_valores)):
        print(f"{i:<8} {p:<8} {v:<8} {v/p:<10.2f}")

    print("\nResultado óptimo:")
    print(f"Capacidad máxima de la mochila: {capacidad_maxima}")
    print(f"Valor máximo obtenible: {valor_maximo}")
    peso_total = sum(lista_pesos[i] for i in objetos)
    print(f"Peso total utilizado: {peso_total}/{capacidad_maxima}")
    print("Objetos seleccionados (índices):", objetos)
