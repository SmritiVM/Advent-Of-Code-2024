from collections import Counter

def process_input(file):
    left_list, right_list = list(), list()
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list

# Part 1
def find_distance(left_list, right_list):
    total_distance = 0
    for l,r in zip(sorted(left_list), sorted(right_list)):
        total_distance += abs(l - r)
    return total_distance


# Part 2
def find_similarity_score(left_list, right_list):
    score = Counter(right_list)
    total_score = 0
    for element in left_list:
        total_score += element * score[element]
    return total_score


with open("./01.Historian_Hysteria/input.txt") as file:
    left_list, right_list = process_input(file)
    # print(find_distance(left_list, right_list))
    print(find_similarity_score(left_list, right_list))