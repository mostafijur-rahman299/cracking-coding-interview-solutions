matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# Reverse matrix data
def reverseMatrix(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[::-1]) # reverse array
    return new_matrix
        
reversed_matrix = reverseMatrix(matrix) # Call matrix reverse function

# Transpose matrix
def transposeMatrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # Swap data
    return matrix

transpose_matrix = transposeMatrix(reversed_matrix) # Call matrix transpose function

# Print data
for row in transpose_matrix:
    print(row)
