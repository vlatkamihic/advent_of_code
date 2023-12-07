import numpy as np

#---------------------------------------------------------------------------------------------------------------------------
# Part 1:

def is_part_number(number, matrix, i, j):
    length = len(number)
    submatrix = matrix[max(i-1, 0):min(i+2, len(matrix))]
    submatrix = [string[max(j-length-1, 0):min(j+1, len(matrix[0]))] for string in submatrix]
    is_part = any(not (char.isalpha() or char.isdigit() or char == '.') for element in submatrix for char in element)

    return is_part


def get_part_number_sum(matrix):
    part_number_sum = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(0, n):
        number = ''
        for j in range(0, m):
            if(matrix[i][j].isdigit()):
                number += matrix[i][j]
                if(j == m-1):
                    if(number and is_part_number(number, matrix, i, j)):
                        part_number_sum += int(number)
                    number = ''
            else:
                if(number and is_part_number(number, matrix, i, j)):
                    part_number_sum += int(number)  
                number = ''

    return part_number_sum

#---------------------------------------------------------------------------------------------------------------------------
# Part 2:

def get_number(matrix, i, j):
    number = 0
    scale = 0
    
    for k in range(j, -1, -1):
        if(matrix[i][k].isdigit()):
            number += pow(10, scale)*int(matrix[i][k])
            scale += 1
        else:
            break
    
    for k in range(j+1, len(matrix[i])):
        if(matrix[i][k].isdigit()):
            number *= 10
            number += int(matrix[i][k])
        else:
            break

    return number


def get_geer_ratio(matrix):
    geer_ratio_sum = 0
    n = len(matrix)
    m = len(matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(0, n):
        for j in range(0, m):
            if(matrix[i][j] == '*'):
                idx = []
                idy = []
                for dr, dc in directions:
                    if(matrix[i+dr][j+dc].isdigit()):
                        idx.append(i+dr)
                        idy.append(j+dc)
                if(len(idx) < 2 or (idx.count(idx[0]) == len(idx) and (len(idx) == 3 or (len(idx) == 2 and idy[0] == idy[1]-1)))):
                    continue
                else:
                    if(len(idx) == 2):
                        num1 = get_number(matrix, idx[0], idy[0])
                        num2 = get_number(matrix, idx[1], idy[1])
                        geer_ratio_sum += num1*num2
                        print("Num1: ", num1, "\nNum2: ", num2)
                    else:
                        unique = list(set(idx))
                        num1 = get_number(matrix, idx[idx.index(unique[0])], idy[idx.index(unique[0])])
                        num2 = get_number(matrix, idx[idx.index(unique[1])], idy[idx.index(unique[1])])
                        print("Num1: ", num1, "\nNum2: ", num2)
                        geer_ratio_sum += num1*num2
                    print("NJO")

    
    return geer_ratio_sum

#---------------------------------------------------------------------------------------------------------------------------

def main():
    engine_schematic = list(np.loadtxt("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 3/input.txt", dtype='str', comments=None))
    # print(engine_schematic)
    part_number_sum = get_part_number_sum(engine_schematic)
    print("Sum of part numbers: ", part_number_sum)

    geer_ratio_sum = get_geer_ratio(engine_schematic)
    print("Sum of geer ratios: ", geer_ratio_sum)
    return

if __name__ == "__main__":
    main()
