def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        print('processing layer ', layer)
        first, last = layer, n - layer - 1
        for i in range(first, last):
            print('processing index ', i)
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
            print(matrix)
    return matrix


import numpy as np

#matrix = np.arange(16).reshape(4,4)
# matrix = np.arange(9).reshape(3,3)
matrix = np.arange(64).reshape(8,8)
print(matrix)
print(rotate_matrix(matrix))