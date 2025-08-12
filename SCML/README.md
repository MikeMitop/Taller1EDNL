# Algoritmo de la Subsecuencia Común Más Larga (LCS) 

## Descripción
La **Subsecuencia Común Más Larga** (*Longest Common Subsequence*, LCS) es un problema clásico en informática que consiste en encontrar la secuencia de caracteres más larga que aparece **en el mismo orden** en dos cadenas dadas.  
A diferencia de la **subcadena**, la subsecuencia **no requiere que los caracteres sean consecutivos**.

Este algoritmo utiliza la **técnica de Programación Dinámica** para optimizar el cálculo, evitando recomputar resultados ya obtenidos.

---

##  Objetivo
Dadas dos cadenas, encontrar:
1. La **longitud** de la LCS.
2. La **subsecuencia** que corresponde a esa longitud.

---

## Idea del algoritmo
El algoritmo crea una matriz bidimensional (`matrix`) donde:
- **Filas** → caracteres de la primera cadena (`args1`)
- **Columnas** → caracteres de la segunda cadena (`args2`)
- `matrix[i][j]` almacena la longitud de la LCS entre:
  - Los primeros `i` caracteres de la primera cadena.
  - Los primeros `j` caracteres de la segunda cadena.

**Reglas para llenar la matriz**:
1. Si `args1[i-1] == args2[j-1]`:
```
   matrix[i][j] = matrix[i-1][j-1] + 1
```
   (Coincidencia → se suma 1 al valor de la diagonal superior izquierda).
2. Si no coinciden:
```
matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
```
(Tomamos el mayor valor entre la celda de arriba y la de la izquierda).

El resultado final está en matrix[n][m], donde:

`n` = longitud de la primera cadena.

`m` = longitud de la segunda cadena.

---

## Complejidad
- **Tiempo:** `O(n × m)`  
- **Espacio:** `O(n × m)`  
Donde:
- `n` = longitud de la primera cadena.
- `m` = longitud de la segunda cadena.

El tiempo que tarda el algoritmo depende del producto de las longitudes de las cadenas.

---

## Ejemplo

### Entrada
```
cadena1 = "ABCDGH"
cadena2 = "AEDFHR"
```

### Salida
```
3
```

|    | "" | A | E | D | F | H | R |
| -- | -- | - | - | - | - | - | - |
| "" | 0  | 0 | 0 | 0 | 0 | 0 | 0 |
| A  | 0  | 1 | 1 | 1 | 1 | 1 | 1 |
| B  | 0  | 1 | 1 | 1 | 1 | 1 | 1 |
| C  | 0  | 1 | 1 | 1 | 1 | 1 | 1 |
| D  | 0  | 1 | 1 | 2 | 2 | 2 | 2 |
| G  | 0  | 1 | 1 | 2 | 2 | 2 | 2 |
| H  | 0  | 1 | 1 | 2 | 2 | 3 | 3 |
