# Function that rotates a matrix
def rotateMatrix(matrix):
  # Init rows, cols, and new matrix
  size = len(matrix)
  result = [[0 for col in range(size)] for row in range(size)]

  for x in range(0, size):
    for y in range(0, size):
      print(f"matrix[{x}][{y}] = {matrix[x][y]}")
      result[y][size-1-x] = matrix[x][y]

  return result

m = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25]
] 
response = rotateMatrix(m)
for row in response:
  print(row)
print(f"new matrix: {response}")

# Time Complexity: O(N^2)

m2 = [
  [21, 16, 11, 6, 1],
  [22, 17, 12, 7, 2],
  [23, 18, 13, 8, 3],
  [24, 19, 14, 9, 4],
  [25, 20, 15, 10, 5]
] 