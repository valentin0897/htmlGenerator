import numpy as np
from functools import reduce

path_index = 'index.html'
path_matrix = 'matrix.txt'
path_new_file = 'generated'
mark = "links"
matrix = []
# matrix = np.array([[0,1,1,0], [0,0,0,0], [0,1,0,1], [0,0,1,0]], bool)
with open(path_matrix, 'r', encoding='utf-8-sig') as file:
    for line in file.readlines():
        matrix.append(list(line.split()))

for i, row in enumerate(matrix):
    matrix[i] = list(map(int, row))

matrix = np.array(matrix, bool)

with open(path_index, 'r', encoding='utf-8') as file:
    html = file.read()

def get_adjacency_matrix(matrix):
    powered_list = [matrix]
    for x in range(3):
        powered_list.append(np.dot(matrix, matrix))
    result = reduce(lambda x, y: x + y, powered_list)
    return result

def get_links(matrix):
    counter_i = 0
    for i in matrix:
        links = []
        counter_j = 0
        for j in i:
            if(j):
                links.append(counter_j)
            counter_j += 1
        write_file(counter_i, links)
        counter_i += 1
        
def write_file(i, links):
    with open(path_new_file + "\\" + str(i) +'.html', 'w', encoding='utf-8') as file:
        for line in html.splitlines(True):
            if mark in line:
                file.write(line)
                for link in links:
                    file.write("<a href=\"" + str(link) + ".html\">Ссылка " + str(link) + "</a>\n")
            else:
                file.write(line)
                            
matrix = get_adjacency_matrix(matrix)
print(matrix)
get_links(matrix)