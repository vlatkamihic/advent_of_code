
import numpy as np

def find_s_position(pipe_sketch):
    s_pos = 0
    for row in pipe_sketch:
        for el in row:
            if(el == 'S'): s_pos = pipe_sketch.index(row), row.index(el)
    return s_pos

def get_max_number(pipe_sketch):
    maximum = 0
    list = [[el for el in row if(isinstance(el, (int, float)))] for row in pipe_sketch]
    nums = []
    for numbers in list:
        for number in numbers:
            nums.append(number)
    maximum = max(nums)

    return maximum

def get_next_positions(pipe_sketch, pos, counter):

    up = ['|', '7', 'F']
    right = ['-', '7', 'J']
    down = ['|', 'L', 'J']
    left = ['-', 'F', 'L']

    directions = [(0, -1, left), (-1, 0, up), (0, 1, right), (1, 0, down)]
    
    

    next_positions = []
    for dr, dc, direction in directions:
        if(pos[0]+dr < 0 or pos[0]+dr >= len(pipe_sketch) or pos[1]+dc < 0 or pos[1]+dc >= len(pipe_sketch[0])): continue
        else:
            char = pipe_sketch[pos[0]+dr][pos[1]+dc]
            next_position = (pos[0]+dr, pos[1]+dc)
            if(char in direction): 
                next_positions.append(next_position)
                pipe_sketch[pos[0]+dr][pos[1]+dc] = counter

    return next_positions

def get_number_of_steps(pipe_sketch):

    positions = [find_s_position(pipe_sketch)]
    is_running = True
    counter = 1

    while(is_running):
        new_positions = []
        is_running = False
        for pos in positions:
            new_pos = get_next_positions(pipe_sketch, pos, counter)
            if len(new_pos) > 0: is_running = True
            for position in new_pos:
                new_positions.append(position)
        positions = new_positions
        counter += 1
    number_of_steps = get_max_number(pipe_sketch)

    return number_of_steps

def print_pipe_sketch(pipe_sketch):
    for row in pipe_sketch:
        idx = pipe_sketch.index(row)
        new_row = []
        for char in row:
            new_row.append(str(char))
        pipe_sketch[idx] = new_row
        print(pipe_sketch[idx])

def check_is_in_loop(numbered_list, letter_list, direction, s):
    i = 0
    symbols = []
    crossed = 0
    for element in numbered_list:
        if(element.isdigit() and (direction == "up" or direction == "down")):
            if(letter_list[i] == '-'):
                crossed += 1
            if(letter_list[i] != '-' and letter_list[i] != '|'):
                symbols.append(letter_list[i])
        if(element.isdigit() and ((direction == "right" or direction == "left"))):
            if(letter_list[i] == '|'):
                crossed += 1
            if(letter_list[i] != '|' and letter_list[i] != '-'):    
                symbols.append(letter_list[i])
        if(element == 'S'):
            symbols.append(s)
        i = i + 1
    
    if(direction == "up" or direction == "down"):
        for i in range(0, len(symbols)-1):
            if((symbols[i] == 'F' or symbols[i] == 'S') and (symbols[i+1] == 'J' or symbols[i] == 'S')):
                crossed +=1
            elif((symbols[i] == '7' or symbols[i] == 'S') and (symbols[i+1] == 'L' or symbols[i] == 'S')):
                crossed +=1
    elif(direction == "right" or direction == "left"):
        for i in range(len(symbols)-1):
            if((symbols[i] == 'L' or symbols[i] == 'S') and (symbols[i+1] == '7' or symbols[i] == 'S')):
                crossed +=1
            elif((symbols[i] == 'F' or symbols[i] == 'S') and (symbols[i+1] == 'J' or symbols[i] == 'S')):
                crossed +=1
    if(crossed % 2 == 0):
        return False
    else:
        return True

def get_s_symbol(pipe_sketch):

    i, j = find_s_position(pipe_sketch)
    s = ''
    if(int(pipe_sketch[i][j+1]) == 1 and int(pipe_sketch[i+1][j]) == 1):
        s = 'F'
    elif(int(pipe_sketch[i-1][j]) == 1 and int(pipe_sketch[i][j+1]) == 1):
        s = 'L'
    elif(int(pipe_sketch[i-1][j]) == 1 and int(pipe_sketch[i][j-1]) == 1):
        s = 'J'
    elif(int(pipe_sketch[i+1][j]) == 1 and int(pipe_sketch[i][j-1]) == 1):
        s = '7'
    elif(int(pipe_sketch[i][j+1]) == 1 and int(pipe_sketch[i][j-1]) == 1):
        s = '-'
    elif(int(pipe_sketch[i-1][j]) == 1 and int(pipe_sketch[i+1][j]) == 1):
        s = '|'

    return s

def check_all_directions(pipe_sketch, copy, i, j, n, m):
    
    s = get_s_symbol(pipe_sketch)
    in_loop = 0
    numbered_list = [row[j] for row in pipe_sketch[0:i]]
    letter_list = [row[j] for row in copy[0:i]]
    if(len(numbered_list) != 0):
        if(check_is_in_loop(numbered_list, letter_list, "up", s)): in_loop += 1

    numbered_list = [row[j] for row in pipe_sketch[min(n, i+1):n]]
    letter_list = [row[j] for row in copy[min(n, i+1):n]]
    if(len(numbered_list) != 0):
        if(check_is_in_loop(numbered_list, letter_list, "down", s)): in_loop += 1

    numbered_list = pipe_sketch[i][:j]
    letter_list = copy[i][:j]
    if(len(numbered_list) != 0):
        if(check_is_in_loop(numbered_list, letter_list, "left", s)): in_loop += 1

    numbered_list = pipe_sketch[i][min(m, j + 1):m]
    letter_list = copy[i][min(m, j + 1):m]
    if(len(numbered_list) != 0):
        if(check_is_in_loop(numbered_list, letter_list, "right", s)): in_loop += 1

    if(in_loop == 4): return True
    else: return False

    

def get_occupancy_grid(pipe_sketch, copy):
    occupancy_grid = np.zeros((len(pipe_sketch), len(pipe_sketch[0])))
    n, m = len(pipe_sketch), len(pipe_sketch[0])
    print("Pipe sketch: ")
    print_pipe_sketch(pipe_sketch)
    for i in range(0, n):
        for j in range(0, m):
            if(pipe_sketch[i][j].isdigit()):
                occupancy_grid[i][j] = 5
            else:
                if(check_all_directions(pipe_sketch, copy, i, j, n, m)):
                    occupancy_grid[i][j] = 1
                else:
                    occupancy_grid[i][j] = 0
    
    return occupancy_grid

def get_num_of_elements_in_loop(new_sketch):
    number = 0
    for line in new_sketch:
        for element in line:
            if(element == 1):
                number += 1

    return number

def main():
    pipe_sketch = list(np.loadtxt("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 10/input.txt", dtype='str'))
    copy = list(np.loadtxt("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 10/input.txt", dtype='str'))
    
    for row in pipe_sketch:
        idx = pipe_sketch.index(row)
        new_row = []
        for char in row:
            new_row.append(str(char))
        pipe_sketch[idx] = new_row

    # print("\n")
    num_of_steps = get_number_of_steps(pipe_sketch)
    # print_pipe_sketch(pipe_sketch)
    # print("\n")
    # print_pipe_sketch(copy)
    
    new_sketch = get_occupancy_grid(pipe_sketch, copy)
    print(new_sketch)
    num_of_elements_in_loop = get_num_of_elements_in_loop(new_sketch)
    print(num_of_elements_in_loop)

    return

if __name__ == "__main__":
    main()