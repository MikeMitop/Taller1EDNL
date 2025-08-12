 # ¿Qué es la distancia de edición?
La distancia de edición entre dos cadenas de texto es el mínimo número de operaciones necesarias para transformar una en otra.
Las operaciones clásicas son:

Inserción → Agregar un carácter.
Ej: "gato" → insertar "s" → "gatos".

Eliminación → Quitar un carácter.
Ej: "gatos" → eliminar "s" → "gato".

Sustitución → Reemplazar un carácter por otro.
Ej: "gato" → sustituir "g" por "p" → "pato".

Importante: todas las operaciones tienen un costo de 1 (en la versión básica).

# ¿Por qué usar programación dinámica?
Si intentas calcular todas las formas de transformar una cadena en otra por fuerza bruta, el número de posibilidades explota combinatoriamente.
La programación dinámica (PD) nos permite guardar resultados parciales para no recalcularlos, optimizando el tiempo de ejecución de exponencial a O(m × n), donde m y n son las longitudes de las cadenas.

# Como funciona computacionalmente 
Sea:

A = primera cadena, longitud m

B = segunda cadena, longitud n

Definimos una matriz DP (dp) de tamaño (m+1) × (n+1) donde:

dp[i][j] = distancia mínima para transformar los primeros i caracteres de A en los primeros j caracteres de B.

Casos base:

dp[0][j] = j → Si A está vacía, necesito j inserciones para obtener B [0..j-1].

dp[i][0] = i → Si B está vacía, necesito i eliminaciones para borrar A [0..i-1].

Recurrencia:
Para i > 0 y j > 0:

Si A[i-1] == B[j-1] →
dp[i][j] = dp[i-1][j-1] (sin costo extra, no hay que cambiar nada).

Si son distintos →

dp[i][j] = 1 + min(
    dp[i-1][j],    // eliminar
    dp[i][j-1],    // insertar
    dp[i-1][j-1]   // sustituir


# implementacion 

def levenshtein(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    #  aca eliminamos 
                    dp[i][j-1],    # aca insertamos
                    dp[i-1][j-1]   # aca sustituimos
                )

    return dp[m][n]


print(levenshtein("gato", "pato"))  # 1

)
