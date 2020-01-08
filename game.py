import argparse
from parsing import get_target, parse_content
from Node import Node

def min_f(open_list):

    min_f = None
    min_node = None

    for node in open_list:
        if min_f is None or node.get_f() < min_f:
            min_f = node.get_f()
            min_node = node
    return min_node


def A_search_algorithm(matrix, target, size):

    start = Node(matrix, target, size, None)
    open_list = []
    closed_list = []
    open_list.append(start)
    i = 0
    while len(open_list) > 0:

        process = min_f(open_list)

        if process.check() == True:
            return process
        
        open_list.remove(process)
        closed_list.append(process.get_matrix())

        next_nodes = process.get_next_nodes()

        for next_node in next_nodes:

            if next_node in closed_list:
                continue

            in_open_list = False

            tmp_node = Node(next_node, target, size, process)

            for node in open_list:
                if node.get_matrix() == next_node:

                    if tmp_node.get_g() < node.get_g():
                        node.set_g(tmp_node.get_g())
                        node.compute_f()
                        node.set_parent(tmp_node.get_parent())
                    
                    in_open_list = True

            if in_open_list == False:
                open_list.append(tmp_node)

    return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    content = args.file.readlines()

    size, matrix = parse_content(content[1:])
    target = get_target(size)
    

    result = A_search_algorithm(matrix, target, size)

    if result == False:
        print("no solution")
    else:
        path = result.get_path()
        for each_path in path:
            for i, x in enumerate(each_path):
                if i % size == 0:
                    print()
                print(x, end=" ")
            print("\n-----", end="")
