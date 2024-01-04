def calc_total_winnings(hands):
    total_winnings = 0
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    return total_winnings

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 7/input.txt")
    # Initialize the list
    lists = [5, 4, 2, 3, 2, 3, 4, 2, 5, 4]
    print("Given list:", lists)

    # Get unique values from a list 
    # Using set() method
    set1 = set(lists)

    # Convert set to list
    result = [lists.count(set) for set in set1]
    print("Unique value list:", result)
    return

if __name__ == "__main__":
    main()