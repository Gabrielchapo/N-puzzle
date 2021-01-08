def manhattan_dist(grid, target, size):
    count = 0
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        target_pos = (target[x])
        count += abs(current_pos[0] - target_pos[0]) \
            + abs(current_pos[1] - target_pos[1])
    return count


def hamming_dist(grid, target, size):
    count = 0
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        target_pos = (target[x])
        if x != 0 and current_pos != target_pos:
            count += 1
    return count