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

## Estructura del Proyecto

```
proyecto/
├── README.md                           # Este archivo
├── presentacion_estructuras_datos/     # Diapositivas de la presentación
│   ├── portada.html
│   ├── intro_prog_dinamica.html
│   ├── prog_dinamica_descripcion.html
│   ├── prog_dinamica_caracteristicas.html
│   ├── prog_dinamica_aplicaciones.html
│   ├── subsecuencia_descripcion.html
│   ├── subsecuencia_aplicaciones.html
│   ├── distancia_descripcion.html
│   ├── distancia_aplicaciones.html
│   ├── mochila_descripcion.html
│   ├── mochila_aplicaciones.html
│   └── mochila_implementacion.html
└── problema_mochila/                   # Implementación del código
    ├── mochila.py                      # Implementación principal
    └── test_mochila.py                 # Pruebas unitarias
```

## Autor

**Manus AI** - Implementación y documentación completa del proyecto educativo sobre programación dinámica.

---

*Este proyecto fue desarrollado como material educativo para el estudio de estructuras de datos no lineales y técnicas de programación dinámica.*



## Requisitos del Sistema

### Requisitos Mínimos

- **Python 3.7 o superior**
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)
- **Sistema operativo**: Windows, macOS, Linux

### Dependencias de Python

El proyecto utiliza únicamente bibliotecas estándar de Python, por lo que no requiere instalación de paquetes adicionales:

- `unittest` - Para las pruebas unitarias
- `sys` - Para funciones del sistema
- `os` - Para operaciones del sistema operativo

## Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes acceso al repositorio
git clone [URL_DEL_REPOSITORIO]
cd estructuras-datos-no-lineales

# O simplemente descargar y extraer los archivos
```

### Paso 2: Verificar la Instalación de Python

```bash
# Verificar que Python 3 esté instalado
python3 --version

# En Windows, puede ser:
python --version
```

### Paso 3: Verificar la Estructura del Proyecto

Asegúrate de que todos los archivos estén en su lugar correcto según la estructura mostrada anteriormente.

## Guía de Uso

### Ejecutar la Implementación del Problema de la Mochila

Para ejecutar el programa principal con ejemplos demostrativos:

```bash
cd problema_mochila
python3 mochila.py
```

Este comando ejecutará:
- Un ejemplo básico con 3 objetos
- Un ejemplo avanzado con 8 objetos
- Comparación entre mochila 0/1 e ilimitada
- Análisis de complejidad algorítmica

### Ejecutar las Pruebas Unitarias

Para verificar que la implementación funciona correctamente:

```bash
cd problema_mochila
python3 test_mochila.py
```

Las pruebas verifican:
- Casos básicos y casos límite
- Manejo de errores
- Correctitud de los algoritmos
- Validación de entrada

### Visualizar la Presentación

Para ver las diapositivas de la presentación:

1. Navega al directorio `presentacion_estructuras_datos/`
2. Abre cualquier archivo `.html` en tu navegador web
3. Las diapositivas están diseñadas para visualización en pantalla completa (1280x720px)

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

### Ejemplo Avanzado: Mochila Ilimitada

```python
from mochila import mochila_ilimitada

# Definir objetos y capacidad
pesos = [1, 3, 4, 5]
valores = [1, 4, 5, 7]
capacidad = 7

# Resolver el problema
valor_maximo = mochila_ilimitada(capacidad, pesos, valores)

print(f"Valor máximo con mochila ilimitada: {valor_maximo}")
```

### Ejemplo de Análisis Completo

```python
from mochila import mochila_01, imprimir_solucion

# Definir un problema personalizado
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 8

# Resolver y mostrar resultados detallados
valor_maximo, objetos_seleccionados = mochila_01(capacidad, pesos, valores)
imprimir_solucion(capacidad, pesos, valores, valor_maximo, objetos_seleccionados)
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

### Algoritmo de Mochila Ilimitada

En la variante ilimitada, cada objeto puede ser seleccionado múltiples veces. La recurrencia se modifica para considerar esta posibilidad:

```
dp[w] = max(dp[w], dp[w-weight[i]] + value[i]) para todo i
```

#### Diferencias Clave

1. **Espacio de estados**: Solo necesita un arreglo unidimensional
2. **Recurrencia**: Permite reutilizar objetos
3. **Complejidad espacial**: O(W) en lugar de O(n × W)

### Reconstrucción de la Solución

La implementación incluye un algoritmo para reconstruir qué objetos fueron seleccionados en la solución óptima:

```python
def reconstruir_solucion(dp, pesos, capacidad):
    objetos_seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            objetos_seleccionados.append(i-1)
            w -= pesos[i-1]
    return objetos_seleccionados
```

### Optimizaciones Implementadas

#### 1. Validación de Entrada
- Verificación de longitudes de listas
- Manejo de casos límite (capacidad cero, sin objetos)
- Validación de tipos de datos

#### 2. Eficiencia de Memoria
- Uso de listas de comprensión para inicialización
- Minimización de copias de datos
- Gestión eficiente de la tabla DP

#### 3. Legibilidad del Código
- Documentación exhaustiva con docstrings
- Nombres de variables descriptivos
- Separación clara de responsabilidades

### Casos de Prueba Implementados

La suite de pruebas cubre los siguientes escenarios:

1. **Casos Básicos**
   - Problema estándar con solución conocida
   - Verificación de valor óptimo y objetos seleccionados

2. **Casos Límite**
   - Capacidad cero
   - Sin objetos disponibles
   - Un solo objeto
   - Objetos que no caben

3. **Casos de Error**
   - Listas de diferentes longitudes
   - Valores inválidos

4. **Casos Complejos**
   - Múltiples objetos con diferentes ratios valor/peso
   - Verificación de restricciones de capacidad
   - Validación de coherencia en resultados

### Análisis de Rendimiento

#### Benchmarks Teóricos

Para un problema con n=1000 objetos y capacidad W=1000:
- **Operaciones**: ~1,000,000 iteraciones
- **Memoria**: ~4 MB para la tabla DP (enteros de 32 bits)
- **Tiempo estimado**: <1 segundo en hardware moderno

#### Escalabilidad

El algoritmo es práctico para:
- **Pequeña escala**: n ≤ 100, W ≤ 1000 (instantáneo)
- **Mediana escala**: n ≤ 1000, W ≤ 10000 (segundos)
- **Gran escala**: n ≤ 10000, W ≤ 100000 (minutos)

Para problemas más grandes, se recomiendan aproximaciones heurísticas o algoritmos especializados.

### Comparación con Otros Enfoques

#### Enfoque Greedy (Voraz)
- **Ventaja**: O(n log n) tiempo, O(1) espacio
- **Desventaja**: No garantiza solución óptima
- **Uso**: Aproximaciones rápidas

#### Fuerza Bruta
- **Ventaja**: Simplicidad conceptual
- **Desventaja**: O(2^n) tiempo exponencial
- **Uso**: Solo para n muy pequeño (n < 20)

#### Programación Dinámica
- **Ventaja**: Solución óptima garantizada
- **Desventaja**: O(n×W) tiempo y espacio
- **Uso**: Problemas de tamaño moderado con pesos enteros


## Aspectos Educativos

### Objetivos de Aprendizaje

Este proyecto está diseñado para que los estudiantes logren los siguientes objetivos:

#### Conocimientos Conceptuales
1. **Comprender la programación dinámica** como técnica de resolución de problemas
2. **Identificar** cuándo aplicar programación dinámica vs otras técnicas
3. **Analizar** la complejidad temporal y espacial de algoritmos dinámicos
4. **Reconocer** patrones de subestructura óptima y subproblemas superpuestos

#### Habilidades Prácticas
1. **Implementar** algoritmos de programación dinámica desde cero
2. **Diseñar** casos de prueba comprehensivos
3. **Optimizar** soluciones para eficiencia de memoria y tiempo
4. **Documentar** código de manera profesional

#### Competencias Analíticas
1. **Evaluar** diferentes enfoques algorítmicos para un problema
2. **Comparar** rendimiento teórico vs práctico
3. **Adaptar** algoritmos base para variantes del problema
4. **Justificar** decisiones de diseño algorítmico

### Metodología Pedagógica

#### Aprendizaje Progresivo
El proyecto sigue una estructura pedagógica que va de lo general a lo específico:

1. **Introducción teórica** mediante presentación visual
2. **Conceptos fundamentales** con ejemplos ilustrativos
3. **Aplicación práctica** con implementación de código
4. **Validación** mediante pruebas exhaustivas
5. **Reflexión** sobre complejidad y optimizaciones

#### Enfoque Constructivista
- Los estudiantes construyen conocimiento sobre conceptos previos
- Cada sección refuerza y expande conceptos anteriores
- Los ejemplos van aumentando en complejidad gradualmente
- Se fomenta la experimentación y modificación del código

### Actividades Sugeridas para Instructores

#### Actividades de Aula
1. **Análisis de casos**: Discutir cuándo usar programación dinámica vs greedy
2. **Trazado de algoritmos**: Seguir paso a paso la ejecución en ejemplos pequeños
3. **Comparación de enfoques**: Implementar el mismo problema con diferentes técnicas
4. **Optimización colaborativa**: Trabajar en equipos para mejorar la eficiencia

#### Tareas y Proyectos
1. **Implementar variantes**: Mochila fraccionaria, múltiples mochilas
2. **Análisis empírico**: Medir tiempos de ejecución con diferentes tamaños
3. **Aplicaciones reales**: Encontrar problemas del mundo real que usen esta técnica
4. **Presentación técnica**: Explicar el algoritmo a audiencia no técnica

#### Evaluación
1. **Comprensión conceptual**: Preguntas sobre cuándo y por qué usar DP
2. **Implementación práctica**: Codificar variantes del problema
3. **Análisis crítico**: Evaluar pros y contras de diferentes enfoques
4. **Comunicación técnica**: Documentar y explicar soluciones

### Extensiones y Proyectos Avanzados

#### Variantes del Problema de la Mochila
1. **Mochila Multidimensional**: Múltiples restricciones (peso, volumen, etc.)
2. **Mochila con Dependencias**: Objetos que requieren otros objetos
3. **Mochila Estocástica**: Valores o pesos probabilísticos
4. **Mochila Online**: Objetos que llegan secuencialmente

#### Otros Problemas de Programación Dinámica
1. **Subsecuencia Común más Larga (LCS)**
2. **Distancia de Edición (Levenshtein)**
3. **Multiplicación de Cadenas de Matrices**
4. **Problema del Cambio de Monedas**
5. **Camino Más Corto (Floyd-Warshall)**

#### Optimizaciones Avanzadas
1. **Optimización de espacio**: Reducir de O(nW) a O(W)
2. **Paralelización**: Aprovechar múltiples núcleos
3. **Aproximaciones**: Algoritmos FPTAS para problemas grandes
4. **Estructuras de datos especializadas**: Heaps, árboles de segmentos

## Recursos Adicionales

### Libros Recomendados
1. **"Introduction to Algorithms"** - Cormen, Leiserson, Rivest, Stein
   - Capítulo 15: Programación Dinámica
   - Análisis riguroso y múltiples ejemplos

2. **"Algorithm Design"** - Kleinberg, Tardos
   - Capítulo 6: Programación Dinámica
   - Enfoque en técnicas de diseño

3. **"Dynamic Programming and Optimal Control"** - Dimitri Bertsekas
   - Tratamiento matemático avanzado
   - Aplicaciones en control y optimización

### Recursos en Línea
1. **GeeksforGeeks**: Tutoriales paso a paso con código
2. **LeetCode**: Problemas de práctica con diferentes dificultades
3. **Coursera/edX**: Cursos universitarios sobre algoritmos
4. **YouTube**: Visualizaciones y explicaciones interactivas

### Herramientas de Visualización
1. **VisuAlgo**: Animaciones de algoritmos de programación dinámica
2. **Algorithm Visualizer**: Herramienta interactiva para ver ejecución
3. **Python Tutor**: Visualización paso a paso del código Python

## Contribuciones y Mejoras

### Cómo Contribuir
Este proyecto está diseñado para ser extensible y mejorable. Las contribuciones son bienvenidas en las siguientes áreas:

#### Mejoras de Código
- Optimizaciones de rendimiento
- Nuevas variantes del problema
- Mejor manejo de errores
- Documentación adicional

#### Contenido Educativo
- Más ejemplos prácticos
- Ejercicios adicionales
- Casos de estudio reales
- Visualizaciones interactivas

#### Pruebas y Validación
- Casos de prueba adicionales
- Benchmarks de rendimiento
- Validación en diferentes plataformas
- Pruebas de estrés

### Estándares de Calidad
- **Código**: Seguir PEP 8 para Python
- **Documentación**: Docstrings completos y comentarios claros
- **Pruebas**: Cobertura mínima del 90%
- **Rendimiento**: Mantener complejidad teórica óptima

## Licencia y Uso Académico

### Términos de Uso
Este proyecto se distribuye bajo una licencia educativa que permite:
- **Uso académico libre** en instituciones educativas
- **Modificación y adaptación** para propósitos educativos
- **Distribución** con atribución apropiada

### Atribución
Al usar este material, por favor incluye la siguiente atribución:
```
"Estructuras de Datos No Lineales: Programación Dinámica"
Desarrollado por Manus AI
Proyecto educativo sobre algoritmos de programación dinámica
```

### Restricciones
- **No uso comercial** sin autorización explícita
- **Mantener atribución** en todas las copias y derivados
- **Compartir mejoras** bajo los mismos términos

## Contacto y Soporte

### Soporte Técnico
Para preguntas técnicas sobre la implementación:
- Revisar la documentación en el código
- Ejecutar las pruebas unitarias para verificar funcionamiento
- Consultar los ejemplos incluidos

### Soporte Educativo
Para preguntas sobre el uso educativo del material:
- Revisar la sección de aspectos educativos
- Consultar las actividades sugeridas
- Adaptar el contenido según el nivel de los estudiantes

### Reporte de Problemas
Si encuentras errores o tienes sugerencias:
1. Verificar que el problema no esté ya documentado
2. Proporcionar información detallada sobre el entorno
3. Incluir pasos para reproducir el problema
4. Sugerir posibles soluciones si las tienes

---

## Conclusión

Este proyecto representa una implementación completa y educativa de conceptos fundamentales en estructuras de datos no lineales, específicamente enfocado en programación dinámica. A través de la combinación de material teórico presentado de manera visual y implementación práctica con código bien documentado, los estudiantes pueden desarrollar una comprensión profunda de estos conceptos esenciales en ciencias de la computación.

La implementación del problema de la mochila sirve como un ejemplo paradigmático de cómo la programación dinámica puede resolver eficientemente problemas de optimización que serían intratables con enfoques de fuerza bruta. El código incluido no solo resuelve el problema, sino que también demuestra mejores prácticas en programación, documentación y pruebas.

Esperamos que este material sea útil tanto para estudiantes que están aprendiendo estos conceptos por primera vez como para instructores que buscan recursos de calidad para enseñar programación dinámica de manera efectiva y práctica.

