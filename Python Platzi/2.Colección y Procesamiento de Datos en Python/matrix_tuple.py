matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])
numbers = 1,2,3,4,5,[3,4],6,7,7,9,10
print(numbers)
print("Numbers:", type(numbers))
print("Matrix:", type(matrix))
print(numbers[0])

# a pesar de que las tuplas son inmutables, si contienen elementos mutables como listas, esos elementos pueden ser modificados
numbers[5][1] = 100
print(numbers)
