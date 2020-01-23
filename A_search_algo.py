from heuristics import get_manhattan_dist
from get_next_nodes import get_next_nodes
import heapq

def A_search_algorithm(matrix, target, size):

    g = 0
    h = get_manhattan_dist(matrix, target, size)
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

        next_nodes = get_next_nodes(process[3], size)

        for next_node in next_nodes:

            if str(next_node) not in closed_list:

                g = process[1] + 1
                h = get_manhattan_dist(next_node, target, size)
                new_node = (g + h, g, h, next_node, process)

                if str(new_node[3]) not in hash_table:
                    hash_table[str(new_node[3])] = {'g':g, 'parent':process}
                    heapq.heappush(open_list, new_node)

                else:
                    if g < hash_table[str(new_node[3])]['g']:
                        heapq.heappush(open_list, new_node)
                        hash_table[str(new_node[3])]['g'] = g
                        hash_table[str(new_node[3])]['parent'] = process