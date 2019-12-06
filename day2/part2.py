import csv

def load_program():
    with open('input.csv') as input:
        return map(lambda r: int(r), [r for r in csv.reader(input)][0])

def manual_fix(program, noun, verb):
    program[1] = noun
    program[2] = verb
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
        return []
    return loop(i+4, program)

def main():
    program = load_program()
    for noun in range(0, 99):
        for verb in range(0, 99):
            result = loop(0, manual_fix(program[:], noun, verb))
            if len(result) > 0 and result[0] == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    print("Advent of Code 2019 - Day 2")
    print(main())