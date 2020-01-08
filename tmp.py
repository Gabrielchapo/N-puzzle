import argparse
import heapq
from parsing import get_target, parse_content

def get_h(grid):
    count = 0
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        target_pos = (target[x])
        count += abs(current_pos[0] - target_pos[0]) \
            + abs(current_pos[1] - target_pos[1])
    return count

def get_next_nodes(process):
    next_nodes = []

    for i, x in enumerate(process):
        if x == 0:
            empty_pos = (i // size, i % size)

    if empty_pos[0] > 0:
        matrix = process[:]
        matrix[empty_pos[0] * size + empty_pos[1]] = matrix[(empty_pos[0] - 1) * size + empty_pos[1]]
        matrix[(empty_pos[0] - 1)* size + empty_pos[1]] = 0
        next_nodes.append(matrix)
    if empty_pos[0] < size - 1:
        matrix = process[:]
        matrix[empty_pos[0] * size + empty_pos[1]] = matrix[(empty_pos[0] + 1) * size + empty_pos[1]]
        matrix[(empty_pos[0] + 1)* size + empty_pos[1]] = 0
        next_nodes.append(matrix)
    if empty_pos[1] > 0:
        matrix = process[:]
        matrix[empty_pos[0] * size + empty_pos[1]] = matrix[empty_pos[0] * size + empty_pos[1] - 1]
        matrix[empty_pos[0] * size + empty_pos[1] - 1] = 0
        next_nodes.append(matrix)
    if empty_pos[1] < size - 1:
        matrix = process[:]
        matrix[empty_pos[0] * size + empty_pos[1]] = matrix[empty_pos[0] * size + empty_pos[1] + 1]
        matrix[empty_pos[0] * size + empty_pos[1] + 1] = 0
        next_nodes.append(matrix)

    return next_nodes

def A_search_algorithm():

    g = 0
    h = get_h(matrix)
    start = (g + h, g, h, matrix, None)
    open_list = []
    closed_list = {}
    heapq.heappush(open_list, start)
    hash_table = {}
    hash_table[str(start[3])] = {'g':g, 'parent':None}

    while len(open_list):

        process = heapq.heappop(open_list)

        if process[2] == 0:

            path = []
            while process:
                path.append(process[3])
                process = process[4]
            return path

        if str(process[3]) in hash_table:
            del hash_table[str(process[3])]
        else:
            hash_table[str(process[3])] = None
        
        closed_list[str(process[3])] = None

        next_nodes = get_next_nodes(process[3])

        for next_node in next_nodes:

            if str(next_node) not in closed_list:

                g = process[1] + 1
                h = get_h(next_node)
                new_node = (g + h, g, h, next_node, process)

                if str(new_node[3]) not in hash_table:
                    hash_table[str(new_node[3])] = {'g':g, 'parent':process}
                    heapq.heappush(open_list, new_node)

                else:
                    if g < hash_table[str(new_node[3])]['g']:
                        heapq.heappush(open_list, new_node)
                        hash_table[str(new_node[3])]['g'] = g
                        hash_table[str(new_node[3])]['parent'] = process

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
content = args.file.readlines()

size, matrix = parse_content(content[1:])
target = get_target(size)
print(target)

path = A_search_algorithm()
for each_path in path:
    for i, x in enumerate(each_path):
        if i % size == 0:
            print()
        print(x, end=" ")
    print("\n-----", end="")