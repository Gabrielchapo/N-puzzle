def parse_content(content):
    
    try:
        size = int(content[0])
    except:
        print("Error: size is incorrect")
        exit()
    
    # check map size
    if size <= 2:
        print("Error: Map too small")
        exit()

    content = content[1:]
    count = 0
    matrix = []

    for line in content:
        
        # pick off comments
        if "#" in line:
            line = line[:line.index("#")]

        sub = line.split()

        if len(sub) > 0:
            # map values must be integers
            try:
                sub = [int(x) for x in sub]
            except:
                print("Error: invalid map")
                exit()
            
            # check map size
            if len(sub) != size:
                print("Error: invalid map")
                exit()
            [matrix.append(x) for x in sub]
            
            count += 1

    # check map size
    if count != size:
        print("Error: invalid map")
        exit()
        
    return size, matrix
