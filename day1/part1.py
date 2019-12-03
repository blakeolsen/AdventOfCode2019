import csv

def main():
    with open('input.csv') as input:
        masses = csv.reader(input)
        fuels = [int(int(mass[0])/3)-2 for mass in masses]
        return sum(fuels)

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 1")
    print(main())