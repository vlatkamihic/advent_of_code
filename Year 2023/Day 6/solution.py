import numpy as np

def num_win_race(time, distance):
    num_winning_races = 0
    if(isinstance(time, int)):
        for i in range(time):
            distance_i = i*(time-i)
            if(distance_i > distance):
                num_winning_races += 1
    else:
        num_winning_races = [0] * len(time)

        for i in range(len(time)):
            for j in range(time[i]):
                distance_j = j*(time[i]-j)
                if(distance_j > distance[i]):
                    num_winning_races[i] += 1

    return num_winning_races

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 6/input.txt")
    # part 1:
    # time = [int(number) for number in f.readline().rsplit("Time:     ", 1)[1].split() if (number.isdigit()) ]
    # distance = [int(number) for number in f.readline().rsplit("Distance: ", 1)[1].split() if (number.isdigit()) ]

    # kerning, part 2:
    time = int(''.join(f.readline().rsplit("Time:     ", 1)[1].split()))
    distance = int(''.join(f.readline().rsplit("Distance: ", 1)[1].split()))
    
    num_winning_races = num_win_race(time, distance)
    print("Number of ways you can beat the record: ", np.prod(num_winning_races))
    return

if __name__ == "__main__":
    main()