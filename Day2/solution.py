
def solution1(course) -> int:
    horizontal = 0
    depth = 0
    for (direction, value) in course:
        if direction == "forward":
            horizontal+= value
        else:
            if direction == "up":
                depth -= value
            else:
                depth += value
    return horizontal * depth

def solution2(course) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for (direction, value) in course:
        if direction == "forward":
            horizontal+= value
            depth += (value * aim)
        else:
            if direction == "up":
                aim -= value
            else:
                aim += value
    return horizontal * depth    

plannedCourse = []

with open("input.txt") as f:
    for line in f:
        (direction, value) = line.split()
        plannedCourse.append((direction, int(value)))


#test = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]

print(f"Solution part 1: {solution1(plannedCourse)}")
print(f"Solution part 2: {solution2(plannedCourse)}")