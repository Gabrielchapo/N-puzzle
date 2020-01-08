import argparse
from parsing import get_target, parse_content
from Node import Node

def min_f(open_list):

    min_f = float('Inf')
    min_node = None

    for node in open_list:
        if node.get_f() < min_f:
            min_f = node.get_f()
            min_node = node
    return min_node


def A_search_algorithm(matrix, target):
    start = Node(matrix, target, None)
    open_list = []
    closed_list = []
    open_list.append(start)
    i = 0
    while len(open_list) > 0:
        i+= 1
        process = min_f(open_list)
        if process.get_matrix() == target:
            return process
        open_list.remove(process)
        closed_list.append(process)

        next_nodes = process.get_next_nodes()

        for next_node in next_nodes:

            in_closed_list = False

            for node in closed_list:
                if node.get_matrix() == next_node:
                    in_closed_list = True
            if in_closed_list == True:
                continue

            in_open_list = False
            tmp_node = Node(next_node, target, process)

            for node in open_list:
                if node.get_matrix() == next_node:

                    if tmp_node.get_g() < node.get_g():
                        node.set_g(tmp_node.get_g())
                        node.compute_f()
                        node.set_parent(tmp_node.get_parent())
                    
                    in_open_list = True

            if in_open_list == False:
                open_list.append(tmp_node)
        """print("++++STEP:", i + 1)
        print("----CLOSED LIST-----")
        for node in closed_list:
            print(node.get_matrix())
            print(node.get_g())
            print(node.get_h())
        
        print("----OPEN LIST-----")
        for node in open_list:
            print(node.get_matrix())
            print(node.get_g())
            print(node.get_h())"""
        
                            
    return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    content = args.file.readlines()

    matrix = parse_content(content[2:])
    target = get_target(len(matrix))
    result = A_search_algorithm(matrix, target)
    if result == False:
        print("no solution")
    else:
        path = result.get_path()
        for each_path in path:
            for x in each_path:
                print(*x)
            print()
