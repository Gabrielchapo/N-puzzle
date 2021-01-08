import argparse
import heapq
from parsing import parse_content
from generate_target import get_target
from A_search_algo import A_search_algorithm

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
content = args.file.readlines()

size, matrix = parse_content(content[1:])
target = get_target(size)

path = A_search_algorithm(matrix, target, size)
for each_path in path:
    for i, x in enumerate(each_path):
        if i % size == 0:
            print()
        print(x, end=" ")
    print("\n-----", end="")