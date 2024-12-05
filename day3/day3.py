import re

with open('day3/input.txt', 'r') as file:
    instructions = file.read()


# task 1
pattern = r'mul\((\d+),\s*(\d+)\)'
matches = re.findall(pattern, instructions)
matches_array = [(int(match[0]), int(match[1])) for match in matches]

# Initialize total
total = 0

# Multiply each pair and add to total
for a, b in matches_array:
    total += a * b

print(total)

# task 2
total = 0
do_state = True

do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'
do_matches = re.finditer(do_pattern, instructions)
dont_matches = re.finditer(dont_pattern, instructions)

# Convert matches to lists of indices
do_indices = [m.start() for m in do_matches]
dont_indices = [m.start() for m in dont_matches]

print(do_indices)
print(dont_indices)



