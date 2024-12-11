def parse_input(file):
    return list(map(int, file.read().strip().split()))

def blink(stones):
    new_arrangement = list()
    for stone in stones:
        if stone == 0: new_arrangement.append(1)
        elif len(str(stone)) % 2 == 0: 
            n = len(str(stone))
            new_arrangement.extend([int(str(stone)[:n//2]), int(str(stone)[n//2:])])
        else: new_arrangement.append(stone * 2024)
    return new_arrangement

def find_stones_after_n_blinks(n, stones):
    blink_count = 0
    while blink_count < n:
        stones = blink(stones)
        blink_count += 1
        print(blink_count)
        # print(stones)
    return len(stones)

with open("./11.Plutonian_Pebbles/input.txt") as file:
    STONES = parse_input(file)
    # print(STONES)
    print(find_stones_after_n_blinks(25, STONES))