# PROG 5: Transpose Matrix

# Input =>Original Matrix :
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Output =>
# ```
# Transpose matrix
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
# Concept Learned: How to deal with a nested list

def transpose_matrix(matrix):
    """
        Returns the transpose of the matrix
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    transposed_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(ROWS):
        for col in range(COLS):
            transposed_matrix[col][row] = matrix[row][col]

    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(f"The original matrix is: ")
for row in matrix:
    print(row)

transposed = transpose_matrix(matrix)

print(f"The tranpose of matrix is: ")
for row in transposed:
    print(row)
