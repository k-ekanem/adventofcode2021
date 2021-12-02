with open(day_2_aoc_2021_input.txt) as day2_file:
    planned_course = [i.split() for i in (day2_file.read().splitlines())]

def part_1():
    horizontal_position, depth = 0, 0
    for command in planned_course:
        move = command[0]
        steps = command[1]
        if move == 'down':
            depth += int(command[1])
        elif move == 'up':
            depth -= int(command[1])
        else:
            horizontal_position += int(command[1])
    return horizontal_position * depth

def part_2():
    horizontal_position, depth, aim = 0, 0, 0
    for command in planned_course:
        move = command[0]
        steps = command[1]
        if move == 'down':
            aim += int(command[1])
        elif move == 'up':
            aim -= int(command[1])
        else:
            horizontal_position += int(command[1])
            depth += aim * int(command[1])
    return horizontal_position * depth

print(part_1())
print(part_2())
