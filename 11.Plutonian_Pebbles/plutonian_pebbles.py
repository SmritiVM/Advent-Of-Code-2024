import functools
from collections import Counter 

def parse_input(file):
    return Counter(map(int, file.read().strip().split()))

def blink(stones):
    new_arrangement = Counter()
    for stone, frequency in stones.items():
        if stone == 0: new_arrangement[1] += frequency
        elif len(str(stone)) % 2 == 0: 
            n = len(str(stone))
            new_arrangement[int(str(stone)[:n//2])] += frequency
            new_arrangement[int(str(stone)[n//2:])] += frequency
        else: new_arrangement[stone * 2024] += frequency
    return new_arrangement

def find_stones_after_n_blinks(n: int, stones: Counter):
    blink_count = 0
    while blink_count < n:
        stones = blink(stones)
        blink_count += 1
    return sum(stones.values())

with open("./11.Plutonian_Pebbles/input.txt") as file:
    STONES = parse_input(file)
    print(find_stones_after_n_blinks(25, STONES))
    print(find_stones_after_n_blinks(75, STONES))