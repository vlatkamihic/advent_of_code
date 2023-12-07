# Part 1:

def map_numbers(values, maps):
    mapped = []
    
    for value in values:
        is_found = False
        for map in maps:
            destination = map[0]
            source = map[1]
            length = map[2]
            if(value >= source and value <= source + length):
                mapped.append(destination + (value - source))
                is_found = True
        if(is_found == False):
            mapped.append(value)

    return mapped

def get_locations(almanac):

    # seeds
    seeds = [int(s) for s in (almanac[0].rsplit(':', 1)[1]).split() if s.isdigit()]

    # seed-to-soil
    start = almanac.index("seed-to-soil map:") + 1
    end = almanac.index("soil-to-fertilizer map:")
    seed_to_soil_map = [almanac[i] for i in range(start, end)]
    seed_to_soil_map = [[int(s) for s in line.split() if s.isdigit()]for line in seed_to_soil_map]
    soil = map_numbers(seeds, seed_to_soil_map)

    # soil-to-fertilizer
    start = end + 1
    end = almanac.index("fertilizer-to-water map:")
    soil_to_fertilizer = [almanac[i] for i in range(start, end)]
    soil_to_fertilizer = [[int(s) for s in line.split() if s.isdigit()]for line in soil_to_fertilizer]
    fertilizer = map_numbers(soil, soil_to_fertilizer)

    # fertilizer-to-water
    start = end + 1
    end = almanac.index("water-to-light map:")
    fertilizer_to_water = [almanac[i] for i in range(start, end)]
    fertilizer_to_water = [[int(s) for s in line.split() if s.isdigit()]for line in fertilizer_to_water]
    water = map_numbers(fertilizer, fertilizer_to_water)

    # water-to-light
    start = end + 1
    end = almanac.index("light-to-temperature map:")
    water_to_light = [almanac[i] for i in range(start, end)]
    water_to_light = [[int(s) for s in line.split() if s.isdigit()]for line in water_to_light]
    light = map_numbers(water, water_to_light)

    # light-to-temperature
    start = end + 1
    end = almanac.index("temperature-to-humidity map:")
    light_to_temperature = [almanac[i] for i in range(start, end)]
    light_to_temperature = [[int(s) for s in line.split() if s.isdigit()]for line in light_to_temperature]
    temperature = map_numbers(light, light_to_temperature)

    # temperature-to-humidity
    start = end + 1
    end = almanac.index("humidity-to-location map:")
    temperature_to_humidity = [almanac[i] for i in range(start, end)]
    temperature_to_humidity = [[int(s) for s in line.split() if s.isdigit()]for line in temperature_to_humidity]
    humidity = map_numbers(temperature, temperature_to_humidity)

    # humidity-to-location
    start = end + 1
    end = len(almanac)
    humidity_to_loaction = [almanac[i] for i in range(start, end)]
    humidity_to_loaction = [[int(s) for s in line.split() if s.isdigit()]for line in humidity_to_loaction]
    location = map_numbers(humidity, humidity_to_loaction)
    # print("Locations: ", location)

    return location

# ----------------------------------------------------------------------------------------------------------------
# Part 2:

def loop_ranges(ranges, maps):
    mapped = []
    new_ranges = []
    
    for range in ranges:
        
        is_found = False
        
        for map in maps:
            destination = map[0]
            source = map[1]
            length = map[2]
            end = source + length - 1
            r1 = range[0]
            r2 = range[0] + range[1] - 1
            # case: map contains range
            if(r1 >= source and r2 <= end):
                mapped.append([destination + (r1 - source), range[1]])
                is_found = True
            # case: map contains left part of range
            elif(r1 >= source and r1 <= end and r2 > end):
                mapped.append([destination + (r1 - source), end - r1 + 1])
                range[1] = r2 - end
                range[0] = end + 1
                is_found = False
            # case: map contains right part of range
            elif(r1 < source and r2 >= source and r2 <= end):
                mapped.append([destination, r2 - source + 1])
                range[1] = source - r1
                is_found = False
            # case: map contains middle part of range
            elif(r1 < source and r2 > end):
                mapped.append([destination, length])
                new_ranges.append([source + length, r2 - end])
                range[1] = source - r1
                range[0] = r1
                is_found = False
            

        if(is_found == False):
            mapped.append([range[0], range[1]])

    return mapped, new_ranges

def map_ranges(ranges, maps):

    mapped, new_ranges = loop_ranges(ranges, maps)
    
    while(len(new_ranges) > 0):
        new_mapped, new_ranges = loop_ranges(new_ranges, maps)
        for map in new_mapped:
            mapped.append(map)

    # print(mapped)
    return mapped

def get_locations_ranges(almanac):

     # seeds
    seeds = [int(s) for s in (almanac[0].rsplit(':', 1)[1]).split() if s.isdigit()]
    seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

    # seed-to-soil
    start = almanac.index("seed-to-soil map:") + 1
    end = almanac.index("soil-to-fertilizer map:")
    seed_to_soil_map = [almanac[i] for i in range(start, end)]
    seed_to_soil_map = [[int(s) for s in line.split() if s.isdigit()]for line in seed_to_soil_map]
    soil = map_ranges(seeds, seed_to_soil_map)

    # soil-to-fertilizer
    start = end + 1
    end = almanac.index("fertilizer-to-water map:")
    soil_to_fertilizer = [almanac[i] for i in range(start, end)]
    soil_to_fertilizer = [[int(s) for s in line.split() if s.isdigit()]for line in soil_to_fertilizer]
    fertilizer = map_ranges(soil, soil_to_fertilizer)

    # fertilizer-to-water
    start = end + 1
    end = almanac.index("water-to-light map:")
    fertilizer_to_water = [almanac[i] for i in range(start, end)]
    fertilizer_to_water = [[int(s) for s in line.split() if s.isdigit()]for line in fertilizer_to_water]
    water = map_ranges(fertilizer, fertilizer_to_water)

    # water-to-light
    start = end + 1
    end = almanac.index("light-to-temperature map:")
    water_to_light = [almanac[i] for i in range(start, end)]
    water_to_light = [[int(s) for s in line.split() if s.isdigit()]for line in water_to_light]
    light = map_ranges(water, water_to_light)

    # light-to-temperature
    start = end + 1
    end = almanac.index("temperature-to-humidity map:")
    light_to_temperature = [almanac[i] for i in range(start, end)]
    light_to_temperature = [[int(s) for s in line.split() if s.isdigit()]for line in light_to_temperature]
    temperature = map_ranges(light, light_to_temperature)

    # temperature-to-humidity
    start = end + 1
    end = almanac.index("humidity-to-location map:")
    temperature_to_humidity = [almanac[i] for i in range(start, end)]
    temperature_to_humidity = [[int(s) for s in line.split() if s.isdigit()]for line in temperature_to_humidity]
    humidity = map_ranges(temperature, temperature_to_humidity)

    # humidity-to-location
    start = end + 1
    end = len(almanac)
    humidity_to_loaction = [almanac[i] for i in range(start, end)]
    humidity_to_loaction = [[int(s) for s in line.split() if s.isdigit()]for line in humidity_to_loaction]
    location = map_ranges(humidity, humidity_to_loaction)
    # print("Locations: ", location)

    return location

def main():
    f = open("/Users/vlatkamihic/Documents/Development/Advent Of Code/advent_of_code/Year 2023/Day 5/input.txt")
    almanac = [line.rsplit('\n', 1)[0] for line in f if(line.rsplit('\n', 1)[0] != '') ]

    locations = get_locations(almanac)
    print("Part 1: ", min(locations))

    locations_range = get_locations_ranges(almanac)
    min_location = min([location[0] for location in locations_range])
    print("Part 2: ", min_location)

    return

if __name__ == "__main__":
    main()