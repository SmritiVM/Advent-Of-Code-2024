from collections import defaultdict

def parse_input(file) -> list:
    return [list(map(int, line.strip().split())) for line in file.readlines()]

def have_same_sign(x: int, y: int) -> bool:
    return (x >= 0 and y >= 0) or (x <= 0 and y <= 0)

def is_safe(report: list) -> bool:
    prev_difference = 0
    # print(report)
    for index in range(len(report) - 1):
        x, y = report[index], report[index + 1]
        current_difference = x - y
        # print(x, y, current_difference)
        if abs(current_difference) > 3 or abs(current_difference) < 1:
            return False
        if not have_same_sign(prev_difference, current_difference):
            return False
        prev_difference = current_difference
    return True

# Part 1
def find_safe_reports(reports):
    return sum([is_safe(report) for report in reports])

# Part 2
def is_safe_with_dampening(report):
    for index in range(len(report)):
        if is_safe(report[:index] + report[index + 1:]):
            return True
    return False

def find_safe_report_with_dampener(reports):
    return sum([is_safe_with_dampening(report) for report in reports])


with open("./02.Red-Nosed_Report/input.txt") as file:
    REPORTS = parse_input(file)
    print(find_safe_reports(REPORTS))
    print(find_safe_report_with_dampener(REPORTS))
