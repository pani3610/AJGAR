def diagonalsum(m):
  count = 0
  for i in range(0, len(m)):
    count += m[i][i]
  return count
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(diagonalsum(matrix))
