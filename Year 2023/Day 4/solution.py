# Part 1:

def calculate_points(win, my_numbers):
    points_worth = [pow(2, int(len(set(win[i]).intersection(my_numbers[i]))) - 1) for i in range(0, len(win)) if(len(set(win[i]).intersection(my_numbers[i])) > 0)]
    print(points_worth)

    return sum(points_worth)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part 2:

def calculate_scratchcards(win, my_numbers):
    card_points = [[int(len(set(win[i]).intersection(my_numbers[i])))] if(len(set(win[i]).intersection(my_numbers[i])) > 0) else [0] for i in range(0, len(win))]
    number_of_scratchcards = 0
    
    for i in range(0, len(card_points)):
        for j in range(0, len(card_points[i])):
            for k in range(i+1, i+card_points[i][j] + 1):
                card_points[k].append(card_points[k][0])
        number_of_scratchcards += len(card_points[i])
    
    return number_of_scratchcards

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 4/input.txt")
    puzzle_input = [line.rsplit(':', 1)[1] for line in f]
    
    winning_numbers = [line.rsplit('|', 1)[0] for line in puzzle_input]
    winning_numbers = [[int(s) for s in winning_card.split() if s.isdigit()] for winning_card in winning_numbers]

    my_numbers = [line.rsplit('|', 1)[1].replace("\n", "") for line in puzzle_input]
    my_numbers = [[int(s) for s in my_card.split() if s.isdigit()] for my_card in my_numbers]

    points_worth = calculate_points(winning_numbers, my_numbers)
    print(points_worth)

    num_of_scratchcards = calculate_scratchcards(winning_numbers, my_numbers)
    print(num_of_scratchcards)
    return

if __name__ == "__main__":
    main()
