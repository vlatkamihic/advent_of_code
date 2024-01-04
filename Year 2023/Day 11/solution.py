import numpy as np

def expand_image(image, isMillion):
    n, m = image.shape
    rows = []
    colms = []
    for i in range(n):
        num_r = 0
        for j in range(m):
            if(image[i].item(j) == '#'):
                num_r += 1
            
        if(num_r == 0): rows.append(i)
        
    for i in range(m):
        num_c = 0
        for j in range(n):
            if(image[j].item(i) == '#'):
                num_c += 1
        if(num_c == 0): colms.append(i)
    # print(rows, colms)
    expand_image = []
    if(not isMillion):
        for i in range(n):
            row = []
            for j in range(m):
                row.append(image[i].item(j))
                if(j in colms):
                    row.append('.')
            expand_image.append(row)
            if(i in rows):
                expand_image.append(row)
        
        return expand_image
    else:
        for i in range(n):
            row = []
            for j in range(m):
                row.append(image[i].item(j))
            expand_image.append(row)

        return expand_image, rows, colms

def get_length(x1, y1, x2, y2, isMillion, rows, colms):
    if(isMillion):
        temp = 0
        for colm in colms:
            if(colm in range(y1, y2) or colm in range(y2, y1)):
                temp += 999999
        if(y1 > y2): y1 += temp
        else: y2 += temp
        temp = 0
        for row in rows:
            if(row in range(x1, x2) or row in range(x2, x1)):
                temp += 999999
        if(x1 > x2): x1 += temp
        else: x2 += temp

    length = abs(x2 - x1) + abs(y2 - y1)
    # print(length)
    return length

def get_sum_of_lengths(image, isMillion, rows, colms):
    n, m = len(image), len(image[0])
    
    count = sum([line.count('#') for line in image if('#' in line)])
    nums = list(range(count, 0, -1))
    numbered_image = [[str(nums.pop()) if(image[i][j] == '#') else image[i][j] for j in range(m)] for i in range(n)]

    for row in numbered_image: print(row)
    lengths = []
    
    for num1 in range(1, count):
        for num2 in range(num1, count + 1):
            if(num1 != num2):
                # print(num1, num2)
                indices_of_num1 = [[i, j] for i, row in enumerate(numbered_image) for j, element in enumerate(row) if element == str(num1)]
                indices_of_num2 = [[i, j] for i, row in enumerate(numbered_image) for j, element in enumerate(row) if element == str(num2)]
                # print(num1, indices_of_num1)
                # print(num2, indices_of_num2)
                lengths.append(get_length(indices_of_num1[0][0], indices_of_num1[0][1], indices_of_num2[0][0], indices_of_num2[0][1], isMillion, rows, colms))
                print(sum(lengths))
    return sum(lengths)

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 11/input.txt")
    image = [[element for element in line if(element != '\n')] for line in f.readlines()]
    # print(np.matrix(image))
    expanded_image, rows, colms = expand_image(np.matrix(image), True)
    # print(expanded_image)
    num_of_lengths = get_sum_of_lengths(expanded_image, True, rows, colms)
    print(num_of_lengths)
    return

if __name__ == "__main__":
    main()