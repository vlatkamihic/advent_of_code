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
    print_pipe_sketch(pipe_sketch)

    return number_of_steps

def print_pipe_sketch(pipe_sketch):
    for row in pipe_sketch:
        idx = pipe_sketch.index(row)
        new_row = []
        for char in row:
            new_row.append(str(char))
        pipe_sketch[idx] = new_row
        print(pipe_sketch[idx])

def main():
    pipe_sketch = list(np.loadtxt("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 10/input.txt", dtype='str'))
    
    print_pipe_sketch(pipe_sketch)
    print("\n")
    num_of_steps = get_number_of_steps(pipe_sketch)
    print(num_of_steps)
    return

if __name__ == "__main__":
    main()
