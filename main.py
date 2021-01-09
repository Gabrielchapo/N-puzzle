import argparse
import heapq

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

def get_h(grid, target):
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
        matrix[(empty_pos[0] - 1) * size + empty_pos[1]] = 0
        next_nodes.append(matrix)
    if empty_pos[0] < size - 1:
        matrix = process[:]
        matrix[empty_pos[0] * size + empty_pos[1]] = matrix[(empty_pos[0] + 1) * size + empty_pos[1]]
        matrix[(empty_pos[0] + 1) * size + empty_pos[1]] = 0
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

def A_search_algorithm(matrix, target):

    open_list = []
    closed_list = {}
    
    h = get_h(matrix, target)
    g = 0

    # structure : (g + h, g, h, matrix, parent)
    start = (g + h, g, h, matrix, None)
    heapq.heappush(open_list, start)

    g_scores = {}
    g_scores[str(start[3])] = {'g': g, 'parent': None}

    while len(open_list) > 0:

        #print("open list:", len(open_list), "closed list:", len(closed_list),end="\r")
        
        process = heapq.heappop(open_list)

        # If we reach the target
        if process[2] == 0:
            path = []
            nb_step = 0
            while process:
                path.append(process[3])
                process = process[4]
                nb_step += 1
            return path, nb_step

        # add the current to the closed list
        closed_list[str(process[3])] = None

        next_nodes = get_next_nodes(process[3])
        
        for node in next_nodes:

            # If it's already in closed list, the one in the closed list,
            # has to be better (better g) so we pass.
            if str(node) not in closed_list:
                g = process[1] + 1
                h = get_h(node, target)

                # add it to the open list of nor present
                if str(node) not in g_scores:
                    g_scores[str(node)] = {'g': g, 'parent': process}
                    heapq.heappush(open_list, (g + h, g, h, node, process))
                
                # replace the actual one in the open list if the g score is better 
                elif g < g_scores[str(node)]['g']:
                    heapq.heappush(open_list, (g + h, g, h, node, process))
                    g_scores[str(node)]['g'] = g
                    g_scores[str(node)]['parent'] = process
        
    exit("This puzzle is unsolvable.")




if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    content = args.file.readlines()

    size, matrix = parse_content(content)
    target = get_target(size)
    
    path, nb_step = A_search_algorithm(matrix, target)
    
    for each_path in path:
        for i, x in enumerate(each_path):
            if i % size == 0:
                print()
            print(x, end=" ")
        print("\n-----", end="")
    
    print("nb steps:", nb_step)