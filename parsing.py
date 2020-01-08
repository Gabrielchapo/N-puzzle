def parse_content(content):
    
    matrix = []

    for line in content:
        sub = line.split()
        sub = [int(x) for x in sub]
        matrix.append(sub)

    return matrix

def get_target(size, target_type="snail"):
    
    target = [[0 for x in range(size)] for y in range(size)]

    count = 1

    if target_type == "snail":
        for i in range(size // 2):

            for j in range(size - 1 - i * 2):
                target[i][j + i] = count
                count += 1
            for j in range(size - 1 - i * 2):
                target[j + i][size - 1 - i] = count
                count += 1
            for j in range(size - 1 - i * 2):
                target[size - 1 - i][size - 1 - j - i] = count
                count += 1
            for j in range(size - 1 - i * 2):
                if count < size * size:
                    target[size - 1 - j - i][i] = count
                count += 1

    return target
