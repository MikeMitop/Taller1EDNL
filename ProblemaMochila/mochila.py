#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementación del Problema de la Mochila usando Programación Dinámica

Este módulo contiene implementaciones para resolver el problema de la mochila
utilizando programación dinámica. Incluye tanto la versión 0/1 (cada objeto
puede ser seleccionado una vez o ninguna) como la versión ilimitada.

Autor: Manus AI
Fecha: 2025
"""

def mochila_01(capacidad, pesos, valores):
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica.
    
    En este problema, cada objeto puede ser seleccionado una vez o ninguna.
    El objetivo es maximizar el valor total sin exceder la capacidad de la mochila.
    
    Args:
        capacidad (int): Capacidad máxima de la mochila
        pesos (list): Lista de pesos de los objetos
        valores (list): Lista de valores de los objetos
    
    Returns:
        tuple: (valor_maximo, objetos_seleccionados)
            - valor_maximo (int): El valor máximo que se puede obtener
            - objetos_seleccionados (list): Lista de índices de objetos seleccionados
    
    Complejidad:
        Tiempo: O(n * W) donde n es el número de objetos y W la capacidad
        Espacio: O(n * W) para almacenar la tabla de programación dinámica
    """
    n = len(pesos)
    
    # Verificar que las listas tengan la misma longitud
    if len(pesos) != len(valores):
        raise ValueError("Las listas de pesos y valores deben tener la misma longitud")
    
    # Crear tabla para almacenar los resultados de subproblemas
    # dp[i][w] = valor máximo que se puede obtener con los primeros i objetos
    # y capacidad w
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla de manera ascendente
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            # Si el peso del objeto actual excede la capacidad actual
            if pesos[i-1] > w:
                # No podemos incluir este objeto
                dp[i][w] = dp[i-1][w]
            else:
                # Elegir el máximo entre incluir o no incluir el objeto actual
                incluir = valores[i-1] + dp[i-1][w - pesos[i-1]]
                no_incluir = dp[i-1][w]
                dp[i][w] = max(incluir, no_incluir)
    
    # Reconstruir la solución (qué objetos fueron seleccionados)
    objetos_seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        # Si el valor cambió, significa que incluimos este objeto
        if dp[i][w] != dp[i-1][w]:
            objetos_seleccionados.append(i-1)  # Índice del objeto (base 0)
            w -= pesos[i-1]  # Reducir la capacidad restante
    
    objetos_seleccionados.reverse()  # Ordenar por índice original
    
    return dp[n][capacidad], objetos_seleccionados


def mochila_ilimitada(capacidad, pesos, valores):
    """
    Resuelve el problema de la mochila ilimitada usando programación dinámica.
    
    En este problema, cada objeto puede ser seleccionado múltiples veces.
    
    Args:
        capacidad (int): Capacidad máxima de la mochila
        pesos (list): Lista de pesos de los objetos
        valores (list): Lista de valores de los objetos
    
    Returns:
        int: El valor máximo que se puede obtener
    
    Complejidad:
        Tiempo: O(n * W) donde n es el número de objetos y W la capacidad
        Espacio: O(W) para almacenar la tabla de programación dinámica
    """
    n = len(pesos)
    
    # Verificar que las listas tengan la misma longitud
    if len(pesos) != len(valores):
        raise ValueError("Las listas de pesos y valores deben tener la misma longitud")
    
    # dp[w] = valor máximo que se puede obtener con capacidad w
    dp = [0 for _ in range(capacidad + 1)]
    
    # Para cada capacidad de 1 a capacidad
    for w in range(1, capacidad + 1):
        # Considerar todos los objetos
        for i in range(n):
            # Si el objeto cabe en la capacidad actual
            if pesos[i] <= w:
                dp[w] = max(dp[w], dp[w - pesos[i]] + valores[i])
    
    return dp[capacidad]


def imprimir_solucion(capacidad, pesos, valores, valor_maximo, objetos_seleccionados):
    """
    Imprime la solución del problema de la mochila de manera legible.
    
    Args:
        capacidad (int): Capacidad máxima de la mochila
        pesos (list): Lista de pesos de los objetos
        valores (list): Lista de valores de los objetos
        valor_maximo (int): Valor máximo obtenido
        objetos_seleccionados (list): Lista de índices de objetos seleccionados
    """
    print(f"\n{'='*50}")
    print("SOLUCIÓN DEL PROBLEMA DE LA MOCHILA")
    print(f"{'='*50}")
    print(f"Capacidad de la mochila: {capacidad}")
    print(f"Valor máximo obtenido: {valor_maximo}")
    
    peso_total = sum(pesos[i] for i in objetos_seleccionados)
    print(f"Peso total utilizado: {peso_total}/{capacidad}")
    
    print(f"\nObjetos seleccionados:")
    print(f"{'Índice':<8} {'Peso':<8} {'Valor':<8} {'Ratio V/P':<10}")
    print("-" * 40)
    
    for i in objetos_seleccionados:
        ratio = valores[i] / pesos[i] if pesos[i] > 0 else 0
        print(f"{i:<8} {pesos[i]:<8} {valores[i]:<8} {ratio:<10.2f}")
    
    print(f"\nEficiencia de la solución: {peso_total/capacidad*100:.1f}% de capacidad utilizada")


def ejemplo_basico():
    """
    Ejemplo básico del problema de la mochila.
    """
    print("EJEMPLO BÁSICO DEL PROBLEMA DE LA MOCHILA")
    print("=" * 50)
    
    # Definir los objetos disponibles
    pesos = [10, 20, 30]
    valores = [60, 100, 120]
    capacidad = 50
    
    print("Objetos disponibles:")
    print(f"{'Índice':<8} {'Peso':<8} {'Valor':<8} {'Ratio V/P':<10}")
    print("-" * 40)
    for i in range(len(pesos)):
        ratio = valores[i] / pesos[i]
        print(f"{i:<8} {pesos[i]:<8} {valores[i]:<8} {ratio:<10.2f}")
    
    # Resolver el problema
    valor_maximo, objetos_seleccionados = mochila_01(capacidad, pesos, valores)
    
    # Mostrar la solución
    imprimir_solucion(capacidad, pesos, valores, valor_maximo, objetos_seleccionados)


def ejemplo_avanzado():
    """
    Ejemplo más complejo del problema de la mochila.
    """
    print("\n\nEJEMPLO AVANZADO DEL PROBLEMA DE LA MOCHILA")
    print("=" * 50)
    
    # Definir un conjunto más grande de objetos
    pesos = [5, 4, 6, 3, 2, 8, 7, 1]
    valores = [10, 40, 30, 50, 15, 20, 25, 5]
    capacidad = 20
    
    print("Objetos disponibles:")
    print(f"{'Índice':<8} {'Peso':<8} {'Valor':<8} {'Ratio V/P':<10}")
    print("-" * 40)
    for i in range(len(pesos)):
        ratio = valores[i] / pesos[i]
        print(f"{i:<8} {pesos[i]:<8} {valores[i]:<8} {ratio:<10.2f}")
    
    # Resolver el problema
    valor_maximo, objetos_seleccionados = mochila_01(capacidad, pesos, valores)
    
    # Mostrar la solución
    imprimir_solucion(capacidad, pesos, valores, valor_maximo, objetos_seleccionados)
    
    # Comparar con la versión ilimitada
    print(f"\n{'='*50}")
    print("COMPARACIÓN CON MOCHILA ILIMITADA")
    print(f"{'='*50}")
    valor_ilimitado = mochila_ilimitada(capacidad, pesos, valores)
    print(f"Valor máximo con mochila 0/1: {valor_maximo}")
    print(f"Valor máximo con mochila ilimitada: {valor_ilimitado}")
    print(f"Diferencia: {valor_ilimitado - valor_maximo}")


def main():
    """
    Función principal que ejecuta los ejemplos del problema de la mochila.
    """
    print("IMPLEMENTACIÓN DEL PROBLEMA DE LA MOCHILA")
    print("Usando Programación Dinámica")
    print("=" * 60)
    
    try:
        # Ejecutar ejemplo básico
        ejemplo_basico()
        
        # Ejecutar ejemplo avanzado
        ejemplo_avanzado()
        
        print(f"\n{'='*60}")
        print("ANÁLISIS DE COMPLEJIDAD")
        print(f"{'='*60}")
        print("Complejidad temporal: O(n × W)")
        print("  - n: número de objetos")
        print("  - W: capacidad de la mochila")
        print("\nComplejidad espacial: O(n × W)")
        print("  - Para almacenar la tabla de programación dinámica")
        print("\nOptimización espacial posible: O(W)")
        print("  - Usando solo una fila de la tabla en lugar de toda la matriz")
        
    except Exception as e:
        print(f"Error durante la ejecución: {e}")


if __name__ == "__main__":
    main()

