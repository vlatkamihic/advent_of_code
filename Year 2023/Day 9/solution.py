def get_next_value(values, backwards):

    l = len(values)
    placeholder = values
    is_running = True
    extrapolated = []
    j = 1
    
    while(is_running):
        new_row = [str(int(placeholder[i+1]) - int(placeholder[i])) for i in range(l-j)]
        numbers = [int(number) for number in new_row]
        extrapolated.append(numbers)
        placeholder = new_row
        # print(placeholder)
        j += 1
        if(all(v == 0 for v in numbers)):
            is_running = False

    print("List: ", extrapolated)
    next_value = 0
    
    if(backwards):
        temp = 0
        extrapolated.reverse()
        values_n = [int(number) for number in values]
        extrapolated.append(values_n)
        extrapolated = [list(reversed(line)) for line in extrapolated]
        for i in range(len(extrapolated)-1):
            if i == 0: temp = extrapolated[i+1][-1] - extrapolated[i][-1]
            else: temp = extrapolated[i+1][-1] - temp
        next_value = temp
    
    else:
        next_value = sum([line[-1] for line in extrapolated]) + int(values[-1])
    
    return next_value

def get_sum_of_extrapolated_values(report, backwards):

    sum = 0
    for sensor_values in report:
        sum += get_next_value(sensor_values, backwards)

    return sum

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 9/input.txt")
    report = [sensor_value.split() for sensor_value in f.readlines()]

    sum = get_sum_of_extrapolated_values(report, True)
    print("Sum of extrapolated values: ", sum)

   
    return

if __name__ == "__main__":
    main()