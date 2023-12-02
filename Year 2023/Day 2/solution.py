import re
import math

def getGamePower(game):
    game = re.sub('Game ', '', game)
    id = game.rsplit(':', 1)[0]
    game = (re.sub(id+': ', '', game)).split("; ")
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    for set in game:
        dictionary = dict((y.strip(), x.strip())
                for x, y in (element.split(' ') 
                for element in set.split(', ')))
        if 'blue' in dictionary: 
            blue = int(dictionary['blue'])
            if(blue > maxBlue): maxBlue = blue
        if 'red' in dictionary: 
            red = int(dictionary['red'])
            if(red > maxRed): maxRed = red
        if 'green' in dictionary: 
            green = int(dictionary['green'])
            if(green > maxGreen): maxGreen = green
    power = maxBlue*maxGreen*maxRed
    print(power)
    return power

def validateGame(game, maxBlue, maxRed, maxGreen):
    game = re.sub('Game ', '', game)
    id = game.rsplit(':', 1)[0]
    game = (re.sub(id+': ', '', game)).split("; ")
    blue = 0
    red = 0
    green = 0
    for set in game:
        dictionary = dict((y.strip(), x.strip())
                for x, y in (element.split(' ') 
                for element in set.split(', ')))
        if 'blue' in dictionary: blue = int(dictionary['blue'])
        if 'red' in dictionary: red = int(dictionary['red'])
        if 'green' in dictionary: green = int(dictionary['green'])
        if(blue > maxBlue or red > maxRed or green > maxGreen):
            id  = 0
            break
    print(id)
    return int(id)

def main():
    
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 2/input.txt")
    inputCode = [line for line in f]
    # print(inputCode)
    possibleGames = [validateGame(game, 14, 12, 13) for game in inputCode]
    print("Sum of possible game iDs: ", sum(possibleGames))
    powerGames = [getGamePower(game) for game in inputCode]
    print("Sum of power: ", sum(powerGames))
    return

if __name__ == "__main__":
    main()