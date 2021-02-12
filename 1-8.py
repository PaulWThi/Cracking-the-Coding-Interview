# Algo that if an element in an M x N matrix is 0, its entire row and column are set to 0.

matrix = [
  [0, 2, 3, 4, 5],
  [6, 7, 8, 0, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 0, 25]
]

def zeroMatrix():
  # Initializers
  rowSize = len(matrix)
  colSize = len(matrix[0])
  zRows = set()
  zCols = set()

  # Add zeroes to sets
  for row in range(rowSize):
    for col in range(colSize):
      if matrix[row][col] == 0:
        print(f"[row][col]: [{row}][{col}]")
        zRows.add(row)
        zCols.add(col)
  
  # Traverse matrix and set element to 0 if exists in zero sets
  for row in range(rowSize):
    for col in range(colSize):
      if row in zRows or col in zCols:
        matrix[row][col] = 0
  
zeroMatrix()

for r in matrix:
  print(r)

print(f"matrix: {matrix}")

# Time Complexity: 0