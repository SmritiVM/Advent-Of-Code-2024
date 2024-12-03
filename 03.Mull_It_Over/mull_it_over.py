import re

def parse_input(file):
    return file.read()

def get_multiplication_result(instruction):
    numbers = re.findall("[0-9]+", instruction)
    return int(numbers[0]) * int(numbers[1])

def find_uncorrupted_mul(program, enable):
    if not enable:
        pattern = "mul\([0-9]+,[0-9]+\)"
        return re.findall(pattern, program)
    pattern = "do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)"
    instructions = re.findall(pattern, program)
    uncorrupted_muls = list()
    for instruction in instructions:
        if instruction == "don't()": enable = False
        elif instruction == "do()": enable = True
        else:
            if enable: uncorrupted_muls.append(instruction)
    return uncorrupted_muls

def sum_of_uncorrupted_mul(program, enable = False):
    instructions = find_uncorrupted_mul(program, enable)
    return sum([get_multiplication_result(instruction) for instruction in instructions])


with open("./03.Mull_It_Over/input.txt") as file:
    PROGRAM = parse_input(file)
    print(sum_of_uncorrupted_mul(PROGRAM)) 
    print(sum_of_uncorrupted_mul(PROGRAM, enable = True)) 
