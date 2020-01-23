def get_next_nodes(process, size):
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