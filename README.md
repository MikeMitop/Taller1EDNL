# Estructuras de Datos No Lineales: Programación Dinámica

## Descripción del Proyecto

Este proyecto presenta una implementación completa y educativa del tema de **Estructuras de Datos No Lineales** con enfoque específico en **Programación Dinámica**. Una implementación práctica del problema de la mochila.


### Requisitos Mínimos

- **Python 3.7 o superior**
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)
- **Sistema operativo**: Windows, macOS, Linux


- `unittest` - Para las pruebas unitarias
- `sys` - Para funciones del sistema
- `os` - Para operaciones del sistema operativo

## Ejemplos de Uso

### Ejemplo: Usar la Función de Mochila 0/1

```python
from mochila import mochila_01

# Definir objetos: [pesos], [valores], capacidad
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidad = 50

# Resolver el problema
valor_maximo, objetos_seleccionados = mochila_01(capacidad, pesos, valores)

print(f"Valor máximo: {valor_maximo}")
print(f"Objetos seleccionados: {objetos_seleccionados}")
```


## Documentación Técnica

### Algoritmo del Problema de la Mochila 0/1

El problema de la mochila 0/1 es un problema clásico de optimización combinatoria que se resuelve eficientemente mediante programación dinámica. La implementación utiliza un enfoque de tabla bidimensional para almacenar soluciones de subproblemas.

#### Formulación Matemática

Dado un conjunto de n objetos, cada uno con peso w_i y valor v_i, y una mochila con capacidad W, el objetivo es:

```
Maximizar: Σ(v_i * x_i) para i = 1 a n
Sujeto a: Σ(w_i * x_i) ≤ W para i = 1 a n
Donde: x_i ∈ {0, 1} para todo i
```

#### Recurrencia de Programación Dinámica

La solución se basa en la siguiente recurrencia:

```
dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
```

Donde:
- `dp[i][w]` = valor máximo usando los primeros i objetos con capacidad w
- `dp[i-1][w]` = valor sin incluir el objeto i
- `dp[i-1][w-weight[i]] + value[i]` = valor incluyendo el objeto i

#### Complejidad Algorítmica

- **Complejidad Temporal**: O(n × W)
  - n: número de objetos
  - W: capacidad de la mochila
  - Se debe llenar una tabla de n×W entradas

- **Complejidad Espacial**: O(n × W)
  - Para almacenar la tabla de programación dinámica
  - Optimizable a O(W) usando solo una fila


## Conclusión

La implementación del problema de la mochila sirve como un ejemplo paradigmático de cómo la programación dinámica puede resolver eficientemente problemas de optimización que serían intratables con enfoques de fuerza bruta. 


