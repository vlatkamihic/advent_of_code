import numpy as np
import time

def findNumbers(line):
    textNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    newLine = line
    res = 0
    # print(line)
    for char in newLine:
        for number in textNumbers:
            if(char == number[0]):
                if(newLine.find(number) != -1):
                    res = newLine.find(number)
                    newLine = newLine[:res] + str(textNumbers.index(number) + 1) + newLine[res + 1:] 
    # print(newLine)
    return newLine

def part1():
    inputCode = list(np.loadtxt("input.txt", dtype='str'))
    f=filter(str.isdigit,inputCode)
    numbers = ["".join(filter(str.isdigit, line)) for line in inputCode]
    suma = sum([int(number[0]+number[-1]) if len(number) >= 2 else int(number[0]+number[0]) for number in numbers])
    print(suma)

def part2():
    # inputCode = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']  -- testCase
    inputCode = list(np.loadtxt("input.txt", dtype='str'))
    txtToNumbers = [ findNumbers(line) for line in inputCode]
    numbers = ["".join(filter(str.isdigit, line)) for line in txtToNumbers]
    # print(numbers)
    suma = sum([int(number[0]+number[-1]) if len(number) >= 2 else int(number[0]+number[0]) for number in numbers])
    print(suma)

def main():
    print("Part one answer: ")
    part1()

    print("Part two answer: ")
    part2()


if __name__ == "__main__":
    main() 