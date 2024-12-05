from collections import defaultdict

def parse_input(file):
    ordering_rule = defaultdict(lambda: list())

    # Process section 1 first
    for line in file:
        if line == '\n':
            break
        number, successor = line.strip('\n').split('|')
        ordering_rule[number].append(successor)

    # Process section 2 next
    updates = list()
    for line in file:
        updates.append(line.strip('\n').split(','))

    return ordering_rule, updates

# Part 1
def is_valid(update, update_length, ordering_rule):
    for index, number in enumerate(update):
        for next in range(index + 1, update_length):
            if update[next] not in ordering_rule[number]:
                return False
    return True

def get_middle_page(update, update_length):
    return update[update_length // 2]

def find_valid_middle_page_sum(ordering_rule, updates):
    middle_page_sum = 0
    for update in updates:
        update_length = len(update)
        if is_valid(update, update_length, ordering_rule):
            middle_page_sum += int(get_middle_page(update, update_length))
    return middle_page_sum


# Part 2
def correct_update(update, update_length, ordering_rule):
    while not is_valid(update, update_length, ordering_rule):
        for index, number in enumerate(update):
            for next in range(index + 1, update_length):
                if update[next] not in ordering_rule[number]:
                    update[next], update[index] = update[index], update[next]
    return update


def find_invalid_middle_page_sum(ordering_rule, updates):
    middle_page_sum = 0
    for update in updates:
        update_length = len(update)
        if not is_valid(update, update_length, ordering_rule):
            corrected_update = correct_update(update, update_length, ordering_rule)
            middle_page_sum += int(get_middle_page(corrected_update, update_length))
    return middle_page_sum

with open("./05.Print_Queue/input.txt") as file:
    ORDERING_RULE, UPDATES = parse_input(file)
    # print(find_valid_middle_page_sum(ORDERING_RULE, UPDATES))
    print(find_invalid_middle_page_sum(ORDERING_RULE, UPDATES))