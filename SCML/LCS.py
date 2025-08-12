def LCS(args1, args2):
  n = len(args1)
  m = len(args2)

  matrix = [[0] * (m + 1) for i in range(n + 1)]

  for i in range(1,n + 1):
    for j in range(1,m + 1):
      if args1[i - 1] == args2[j - 1]:
        matrix[i][j] = matrix[i - 1][j - 1] + 1
      else:
        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

  return matrix[n][m]

LCS("ABCDGH", "AEDFHR")
