#A simple program to define matrix in python
#matrix[row][column]

matrix = [
    [0, 1, 2],
    [1, 2, 4],
    [9, 1, 0]
    ]

#print specific item
print(matrix[0][2])

#iterate whole matrix
for row in matrix:
    for item in row:
        print(item)
    
