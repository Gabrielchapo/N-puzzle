import argparse
import heapq
from math import sqrt

def parse_content(content):
    
    try:
        size = int(content[1])
        matrix = []

        for line in content[2:]:
            sub = line.split('#')[0]
            sub = sub.split()
            sub = [int(x) for x in sub]
            [matrix.append(x) for x in sub]
        return size, matrix
    except:
        exit("Something went wrong with the file.")

def get_target(size):
    
    target = [[0 for x in range(size)] for y in range(size)]

    count = 1
    target = {}
    if size % 2 != 0:
        target[0] = (size // 2, size // 2)
    else:
        target[0] = (size // 2, size // 2 - 1)

    for i in range(size // 2):

        for j in range(size - 1 - i * 2):
            target[count] = (i, j + i)
            count += 1
        for j in range(size - 1 - i * 2):
            target[count] = (j + i, size - 1 - i)
            count += 1
        for j in range(size - 1 - i * 2):
            target[count] = (size - 1 - i, size - 1 - j - i)
            count += 1
        for j in range(size - 1 - i * 2):
            if count < size * size:
                target[count] = (size - 1 - j - i, i)
            count += 1

    return target

def get_heuristic(grid, target, heuristic):
    count = 0
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        target_pos = (target[x])
        if heuristic == 1:
            count += abs(current_pos[0] - target_pos[0]) + abs(current_pos[1] - target_pos[1])
        elif heuristic == 2:
            count += sqrt(pow(current_pos[0] - target_pos[0], 2) + pow(current_pos[1] - target_pos[1], 2))
        elif heuristic == 3:
            if current_pos != target_pos:
                count += 1
    return count

def get_next_nodes(process):

    next_nodes = []
    i = process.index(0)
    empty_pos = (i // size, i % size)
    if empty_pos[0] > 0:
        matrix = process[:]
        matrix[i] = matrix[(empty_pos[0] - 1) * size + empty_pos[1]]
        matrix[(empty_pos[0] - 1) * size + empty_pos[1]] = 0
        next_nodes.append(matrix)
    if empty_pos[0] < size - 1:
        matrix = process[:]
        matrix[i] = matrix[(empty_pos[0] + 1) * size + empty_pos[1]]
        matrix[(empty_pos[0] + 1) * size + empty_pos[1]] = 0
        next_nodes.append(matrix)
    if empty_pos[1] > 0:
        matrix = process[:]
        matrix[i] = matrix[i - 1]
        matrix[i - 1] = 0
        next_nodes.append(matrix)
    if empty_pos[1] < size - 1:
        matrix = process[:]
        matrix[i] = matrix[i + 1]
        matrix[i + 1] = 0
        next_nodes.append(matrix)

    return next_nodes

def search_algorithm(matrix, target, heuristic, G_COST):
    open_list = {}
    closed_list = {}
    h = get_heuristic(matrix, target, heuristic)
    queue = [(h, 0, h, matrix, None)]
    while queue:
        process = heapq.heappop(queue)
        if process[2] == 0:
            path = []
            while process:
                path.append(process[3])
                process = process[4]
            path.reverse()
            return path, {'space':len(open_list), 'time':len(closed_list)}
        if str(process[3]) not in closed_list:
            closed_list[str(process[3])] = None
            next_nodes = get_next_nodes(process[3])
            g = process[1] + G_COST
            for node in next_nodes:
                if str(node) not in closed_list:
                    if str(node) in open_list and g >= open_list[str(node)]:
                        continue
                    h = get_heuristic(node, target, heuristic)
                    heapq.heappush(queue, (g + h, g, h, node, process))
                    open_list[str(node)] = g
        
    exit("This puzzle is unsolvable.")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    content = args.file.readlines()


    size, matrix = parse_content(content)
    target = get_target(size)
    
    try:
        algo = int(input("1. A* search\n2. greedy search\n"))
        heuristic = int(input("1. Manhattan distance\n2. Euclidian distance\n3. tiles out of place\n"))
    except:
        exit("Error: wrong input.")
        
    if heuristic != 1 and heuristic != 2 and heuristic != 3:
        exit("Error: wrong input.")
    if algo != 1 and algo != 2:
        exit("Error: wrong input.")

    if algo == 1:
        G_COST = 1
    elif algo == 2:
        G_COST = 0
    else:
        exit("Error: wrong input.")
    
    path, complexity = search_algorithm(matrix, target, heuristic, G_COST)
    
    for each_path in path:
        for i, x in enumerate(each_path):
            if i % size == 0:
                print()
            print(x, end=" ")
        print("\n-----", end="")
    
    print("\nnb steps:", len(path))
    print(complexity)
