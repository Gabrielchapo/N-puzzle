def get_manhattan_dist(grid, target, size):
    count = 0
    for i, x in enumerate(grid):
        current_pos = (i // size, i % size)
        target_pos = (target[x])
        count += abs(current_pos[0] - target_pos[0]) \
            + abs(current_pos[1] - target_pos[1])
    return count
