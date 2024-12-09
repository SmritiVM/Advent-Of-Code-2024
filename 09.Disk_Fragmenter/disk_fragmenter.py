def parse_input(file):
    disk = list()
    file_id = 0
    for index, number in enumerate(file.read()):
        # Even indices -> file space, Odd indices -> free space
        if index % 2:
            disk.extend(['.'] * int(number))
        else:
            disk.extend([file_id] * int(number))
            file_id += 1
    return disk

def out_of_bounds(blank_index, number_index, disk_length):
    return blank_index >= number_index or blank_index >= disk_length or number_index < 0

# Part 1
def compress(disk):
    # Find first '.' from right and first number from left. Swap
    # Stop when index of number < index of '.'
    disk_length = len(disk)
    blank_index, number_index = 0, disk_length - 1
    while True:
        while disk[blank_index] != '.':
            blank_index += 1
        while not isinstance(disk[number_index], int):
            number_index -= 1
        if out_of_bounds(blank_index, number_index, disk_length): break
        disk[blank_index], disk[number_index] = disk[number_index], disk[blank_index]
    return disk

def find_end_index(disk, disk_length, index, offset):
    end_index = index
    while 0 <= end_index < disk_length and disk[end_index] == disk[index]:
        end_index += offset
    return end_index


# Part 2 
def find_contiguous_blank_blocks(disk, disk_length):
    blanks = []
    blank_start = 0
    while True:
        while blank_start < disk_length and disk[blank_start] != '.':
            blank_start += 1
        if blank_start >= disk_length: break
        blank_end = find_end_index(disk, disk_length, blank_start, 1)
        blanks.append((blank_start, blank_end))
        blank_start = blank_end
    return blanks

def find_continguous_number_blocks(disk, disk_length):
    numbers = []
    number_start = disk_length - 1
    while True:
        while number_start >= 0 and not isinstance(disk[number_start], int):
            number_start -= 1
        if number_start < 0: break
        number_end = find_end_index(disk, disk_length, number_start, -1)
        numbers.append((number_end + 1, number_start + 1))
        number_start = number_end
    return numbers

def blockwise_compress(disk):
    disk_length = len(disk)
    blanks = find_contiguous_blank_blocks(disk, disk_length)
    numbers = find_continguous_number_blocks(disk, disk_length)
    blank_block_count, number_block_count = len(blanks), len(numbers)
    blank_pointer, number_pointer = 0, 0
    print(blanks)
    print(numbers)
    while number_pointer < number_block_count:
        blank_start, blank_end = blanks[blank_pointer]
        number_start, number_end = numbers[number_pointer]
        difference = number_end - number_start
        if blank_start > number_start:
            number_pointer += 1
            blank_pointer = 0
            print(number_pointer)
            continue
        if blank_end - blank_start >= difference:
            disk[blank_start:blank_start + difference], disk[number_start:number_end] = disk[number_start:number_end], disk[blank_start:blank_start + difference]
            number_pointer += 1
            print(number_pointer)
            blanks = find_contiguous_blank_blocks(disk, disk_length)
            blank_block_count, blank_pointer = len(blanks), 0
        else:
            blank_pointer += 1
        if blank_pointer >= blank_block_count:
            number_pointer += 1
            print(number_pointer)
            blank_pointer = 0
    return disk


def find_checksum(compact_disk):
    checksum = 0
    for index, number in enumerate(compact_disk):
        if number == '.': continue
        checksum += index * number
    return checksum

with open("./09.Disk_Fragmenter/input.txt") as file:
    DISK = parse_input(file)
    # COMPACT_DISK = compress(DISK)
    # print(find_checksum(COMPACT_DISK))
    # print(DISK)
    BLOCKWISE_COMPACT_DISK = blockwise_compress(DISK)
    print(BLOCKWISE_COMPACT_DISK)
    print(find_checksum(BLOCKWISE_COMPACT_DISK))