import csv

def determine_fuel(mass):
    return int(mass/3)-2

def determine_total_fuel(initial_mass):
    if initial_mass <= 0:
        return 0
    else:
        fuel_required = determine_fuel(initial_mass)
        return determine_total_fuel(fuel_required) + initial_mass

def main():
    with open('input.csv') as input:
        reader = csv.reader(input)
        masses = map(lambda line: int(line[0]), reader)
        fuels = [determine_total_fuel(determine_fuel(mass)) for mass in masses]
        return sum(fuels)

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 1")
    print(main())