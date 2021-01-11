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
    target = [0] * (size**2)
    count = 1
    for i in range(size // 2):
        for j in range(size - 1 - i * 2):
            target[i * size + j + i] = count
            count += 1
        for j in range(size - 1 - i * 2):
            target[(j + i) * size + size - 1 - i] = count
            count += 1
        for j in range(size - 1 - i * 2):
            target[(size - 1 - i) * size + size - 1 - j - i] = count
            count += 1
        for j in range(size - 1 - i * 2):
            if count < size * size:
                target[(size - 1 - j - i) * size + i] = count
            count += 1
    return target

def get_heuristic(grid, target, heuristic, algo):
    count = 0
    if algo == 3:
        return count
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        tmp = target.index(x)
        target_pos = (tmp // size, tmp % size)
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

def search_algorithm(matrix, target, heuristic, algo):
    G_COST = 0
    if algo == 1 or algo == 3:
        G_COST = 1
    open_list = {}
    closed_list = {}
    h = get_heuristic(matrix, target, heuristic, algo)
    queue = [(h, 0, h, matrix, None)]
    while queue:
        process = heapq.heappop(queue)
        if str(process[3]) == str(target):
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
                    h = get_heuristic(node, target, heuristic, algo)
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
        algo = int(input("1. A* search\n2. greedy search\n3.Uniform-cost search\n"))
        if algo != 1 and algo != 2 and algo != 3:
            exit("Error: wrong input.")
        if algo != 3:
            heuristic = int(input("1. Manhattan distance\n2. Euclidian distance\n3. tiles out of place\n"))
            if heuristic != 1 and heuristic != 2 and heuristic != 3:
                exit("Error: wrong input.")
        else:
            heuristic = 0
    except:
        exit("Error: wrong input.")

    path, complexity = search_algorithm(matrix, target, heuristic, algo)
    
    for each_path in path:
        for i, x in enumerate(each_path):
            if i % size == 0:
                print()
            print(x, end=" ")
        print("\n-----", end="")
    
    print("\nnb steps:", len(path))
    print(complexity)
