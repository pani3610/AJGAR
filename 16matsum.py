def sumRow(matrix,row):
   row=i
   total = 0
   for column in range(len(matrix[i])):
      total += matrix[row][column]
   return total
def sumColumn(matrix,column):
   column=i
   total = 0
   for row in range(len(matrix)):
      total += matrix[row][column]
   return total
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for i in range(len(matrix)):
   print(sumRow(matrix,i))
for i in range(len(matrix[0])):
   print(sumColumn(matrix,i))
