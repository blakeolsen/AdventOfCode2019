import csv


def load_program():
    with open('input.csv') as input:
        lines = [r for r in csv.reader(input)]
        return lines[0], lines[1]


def get_coordinates(x, y, directions):
    if len(directions) == 0:
        return []
    else:
        direction = directions[0]
        f = {
            "R": lambda n: (x+n, y),
            "L": lambda n: (x-n, y),
            "U": lambda n: (x, y+n),
            "D": lambda n: (x, y-n),
        }[direction[0]]
        coordinates = [f(n+1) for n in range(int(direction[1:]))]
        (endX, endY) = coordinates[len(coordinates)-1]
        return coordinates + get_coordinates(endX, endY, directions[1:])


def main():
    # (["R8","U5","L5","D3"],["U7","R6","D4","L4"])
    # (["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"])
    # (["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])
    (directions1, directions2) = load_program()
    (coordinates1, coordinates2) = (get_coordinates(0,0,directions1), get_coordinates(0,0,directions2))
    intersections = list(set(coordinates1) & set(coordinates2))
    print(intersections)
    return min(map(lambda (a, b): abs(a)+abs(b), intersections))

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 3")
    print(main())