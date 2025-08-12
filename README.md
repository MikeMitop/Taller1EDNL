# Estructuras de Datos No Lineales: Programación Dinámica

## Descripción del Proyecto

Este proyecto presenta una implementación completa y educativa del tema de **Estructuras de Datos No Lineales** con enfoque específico en **Programación Dinámica**. El proyecto incluye una presentación profesional y una implementación práctica del problema de la mochila, diseñado para estudiantes y profesionales que deseen comprender a fondo estos conceptos fundamentales de la ciencia de la computación.

## Contenido del Proyecto

### 📊 Presentación Académica

El proyecto incluye una presentación profesional de 12 diapositivas que cubre:

1. **Introducción a la Programación Dinámica**
   - Conceptos fundamentales y definiciones
   - Historia y desarrollo de la técnica
   - Principios básicos de funcionamiento

2. **Características de la Programación Dinámica**
   - Subestructura óptima
   - Subproblemas superpuestos
   - Memorización (memoization)
   - Enfoque ascendente vs descendente

3. **Aplicaciones y Casos de Uso**
   - Teoría de grafos
   - Bioinformática
   - Procesamiento de texto
   - Optimización de recursos

4. **Problemas Clásicos Implementados**
   - Subsecuencia Común más Larga (LCS)
   - Distancia de Edición (Levenshtein)
   - Problema de la Mochila (Knapsack)

### 💻 Implementación en Código

El proyecto incluye una implementación completa en Python del **Problema de la Mochila** con:

- Algoritmo para mochila 0/1 (cada objeto una vez)
- Algoritmo para mochila ilimitada (objetos múltiples veces)
- Reconstrucción de la solución óptima
- Análisis de complejidad temporal y espacial
- Ejemplos prácticos y casos de prueba
- Suite completa de pruebas unitarias


### Requisitos Mínimos

- **Python 3.7 o superior**
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)
- **Sistema operativo**: Windows, macOS, Linux


- `unittest` - Para las pruebas unitarias
- `sys` - Para funciones del sistema
- `os` - Para operaciones del sistema operativo

## Instalación y Configuración



## Ejemplos de Uso

### Ejemplo Básico: Usar la Función de Mochila 0/1

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

Este proyecto representa una implementación completa y educativa de conceptos fundamentales en estructuras de datos no lineales, específicamente enfocado en programación dinámica. A través de la combinación de material teórico presentado de manera visual y implementación práctica con código bien documentado, los estudiantes pueden desarrollar una comprensión profunda de estos conceptos esenciales en ciencias de la computación.

La implementación del problema de la mochila sirve como un ejemplo paradigmático de cómo la programación dinámica puede resolver eficientemente problemas de optimización que serían intratables con enfoques de fuerza bruta. El código incluido no solo resuelve el problema, sino que también demuestra mejores prácticas en programación, documentación y pruebas.

Esperamos que este material sea útil tanto para estudiantes que están aprendiendo estos conceptos por primera vez como para instructores que buscan recursos de calidad para enseñar programación dinámica de manera efectiva y práctica.

