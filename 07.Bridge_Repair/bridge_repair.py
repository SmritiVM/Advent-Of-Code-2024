# import sys
# sys.setrecursionlimit(10**6)

def parse_input(file):
    test_values, operands = list(), list()
    for line in file:
        test_value, operand = line.strip().split(':')
        test_values.append(int(test_value))
        operands.append(list(map(int, operand.strip().split())))
    return test_values, operands

def is_valid(test_value, operands, with_concat):
    if len(operands) == 1:
        return operands[0] == test_value
    
    add_choice = operands[0] + operands[1]
    if is_valid(test_value, [add_choice] + operands[2:], with_concat): return True

    mul_choice = operands[0] * operands[1]
    if is_valid(test_value, [mul_choice] + operands[2:], with_concat): return True

    if with_concat:
        concat_choice = int(str(operands[0]) + str(operands[1]))
        if is_valid(test_value, [concat_choice] + operands[2:], with_concat): return True

    return False


def find_test_value_sum(test_values, operands, with_concat = False):
    valid_test_sum = 0
    for (test_value, operand) in zip(test_values, operands):
        if is_valid(test_value, operand, with_concat):
            valid_test_sum += test_value
    return valid_test_sum

with open("./07.Bridge_Repair/input.txt") as file:
    TEST_VALUES, OPERANDS = parse_input(file)
    print(find_test_value_sum(TEST_VALUES, OPERANDS))
    print(find_test_value_sum(TEST_VALUES, OPERANDS, with_concat = True))

   
