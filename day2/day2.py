levels = []

with open('day2/input.txt', 'r') as file:
    for line in file:
        numbers = []
        numbers = [int(x) for x in line.strip().split()]
        levels.append(numbers)

#task 1
def is_safe(level) :
    prev = level[0]
    isAsc = level[0] < level[1]
    safeFlag = True
    for i in range(1, len(level)):
        curr = level[i]
        if (isAsc and prev > curr) or (not isAsc and prev < curr) or (abs(prev - curr) > 3 or abs(prev - curr) < 1):
            safeFlag = False
        prev = curr
    return safeFlag

safeCount = 0
for level in levels:
    safeCount += is_safe(level)

print(safeCount)

#task 2
safeCount = 0

def is_safe_dampened(level):
    prev = level[0]
    isAsc = level[0] < level[1]
    safeFlag = True
    isDampened = False
    for i in range(1, len(level) - 1):
        curr = level[i]
        next = level[i + 1]
        if (isAsc and prev > curr) or (not isAsc and prev < curr) or (abs(prev - curr) > 3 or abs(prev - curr) < 1):
            if not isDampened:
               if (isAsc and prev > next) or (not isAsc and prev < next) or (abs(prev - curr) > 3 or abs(prev - next) < 1):
                    safeFlag = False
               else:
                   isDampened = True
            else:
                safeFlag = False
        else:
            prev = curr

    if not isDampened:
        if (isAsc and prev > level[-1]) or (not isAsc and prev < level[-1]) or (abs(prev - level[-1]) > 3 or abs(prev - level[-1]) < 1):
            safeFlag = False

    return safeFlag


def is_really_safe(level):
    if is_safe(level):
        return True
    for i in range(len(level)):
        if is_safe(level[:i] + level[i+1:]):
            return True
    return False

for level in levels:
    if is_safe(level):
        safeCount += 1
    elif is_really_safe(level):
        safeCount += 1

print(safeCount)
        



