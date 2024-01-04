import numpy as np

def step_by_step(instructions, network):
    A = []
    num_of_steps = 0
    num_of_a = 0
    for branch in network: 
        if(branch[0][2] == 'A'): 
            A.append(branch[0])
            num_of_a += 1
    j = 0
    while(get_number_of_z(A) < num_of_a):
        if(len(instructions) == j): j = 0
        for i in range(0, num_of_a):
            A[i] = calculate_step(instructions[j], A[i], network)
        j += 1
        num_of_steps += 1
        # print("Step ", num_of_steps)
        
        if(get_number_of_z(A) != 0): print("A: ", A)
    
    return num_of_steps

def calculate_step(instruction, position, network):
    destination = 0
    for branch in network:
        if(branch[0] == position):
            if(instruction == 'R'): destination = branch[2]
            else: destination = branch[1]
    return destination

def get_number_of_z(list):
    count = 0
    for element in list:
        if(element[2] == 'Z'):
            count += 1
    return count

def get_number_of_steps(instructions, network, position, simultaneously):
    num_of_steps = 0
    
    if(simultaneously):
        A = []
        for branch in network: 
            if(branch[0][2] == 'A'): 
                A.append(branch[0])
        numbers = [get_number_of_steps(instructions, network, a, False) for a in A]
        num_of_steps = np.lcm.reduce(numbers)
    
    else:
        i = 0
        while(position[2] != 'Z'):
            if(len(instructions) == i): i = 0
            position = calculate_step(instructions[i], position, network)
            num_of_steps += 1
            i += 1
            

    return num_of_steps

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 8/input.txt")
    instructions = [instruction for instruction in f.readline()][0:-1]
    print(instructions)

    network = [branch[0:-1] for branch in f.readlines() if(branch != '\n') ]
    network = [[char for char in branch  if(char.isalpha() or char.isdigit())] for branch in network]
    network = [[''.join(branch[i : i+3]) for i in range(0, len(branch) - 2, 3)] for branch in network]
    print(network)

    number_of_steps = get_number_of_steps(instructions, network, 'AAA', True)
    print(number_of_steps)
   
    return

if __name__ == "__main__":
    main()