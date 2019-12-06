import csv

def load_program():
    with open('input.csv') as input:
        return map(lambda r: int(r), [r for r in csv.reader(input)][0])

def manual_fix(program):
    program[1] = 12
    program[2] = 2
    return program

def loop(i, program):
    op = program[i]
    if op == 99:
        return program
    elif op == 1:
        program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
    elif op == 2:
        program[program[i+3]] = program[program[i + 1]] * program[program[i + 2]]
    else:
        print("ERROR: " + str(op))
        return []
    return loop(i+4, program)

def main():
    program = manual_fix(load_program())
    result = loop(0, program)
    return result[0]

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 2")
    print(main())