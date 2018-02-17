import numpy as np
from functools import reduce

matrix = np.array([[0,1,1,0], [0,0,0,0], [0,1,0,1], [0,0,1,0]], bool)

# matrix = np.dot(matrix, matrix)

def get_adjacency_matrix(matrix):
    powered_list = [matrix]
    for x in range(3):
        powered_list.append(np.dot(matrix, matrix))
    result = reduce(lambda x, y: x + y, powered_list)
    return result

print(get_adjacency_matrix(matrix))