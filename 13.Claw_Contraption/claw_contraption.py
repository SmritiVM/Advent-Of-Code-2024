import re
from sympy import symbols, Symbol, Eq, solve

def parse_input(file):
    sections = file.read().split('\n\n')
    machines = []
    for section in sections:
        machines.append(list(map(int, re.findall("\d+", section))))
        # [0, 1] -> A, [2, 3] -> B, [4, 5] -> Prize
    return machines

def solve_equations(a1, b1, c1, a2, b2, c2):
    t1, t2 = symbols('t1,t2')
    eq1 = Eq((a1*t1+b1*t2), -c1)
    eq2 = Eq((a2*t1+b2*t2), -c2)
    return solve((eq1, eq2), (t1, t2))

def count_tokens():
    tokens = 0
    for machine in MACHINES:
        ax, ay, bx, by, px, py = machine
        solution = solve_equations(ax, bx, px, ay, by, py)
        if not solution: continue
        a, b = solution.values()
        if int(a) != a or int(b) != b: continue
        a, b = abs(a), abs(b)
        if a > 100 or b > 100: continue
        else: 
            tokens += a * 3 + b * 1
    return tokens

with open("./13.Claw_Contraption/input.txt") as file:
    MACHINES = parse_input(file)
    print(count_tokens())






# Data structure [{Prize: (X, Y), A:(X, Y), B(X, Y)}, ...]
# 94a + 22b = 8400
# 34a + 67b = 5400

# from sympy import symbols, Symbol, Eq, solve
# a, b = symbols('a,b')
# e1 = Eq((26*a+66*b), -12748)
# e2 = Eq((67*a+21*b), -12176)
# c = solve((e1, e2), (a, b))
# print(c)
