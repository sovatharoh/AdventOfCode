# input file
left = []
right = []
with open('day1/input.txt', 'r') as file:
    for line in file:
        left_val, right_val = line.strip().split()
        left.append(int(left_val))
        right.append(int(right_val))


#print("Left array:", left)
#print("Right array:", right)

# Sort while keeping track of original indices
sorted_left_with_indices = sorted(enumerate(left), key=lambda x: x[1])
sorted_right_with_indices = sorted(enumerate(right), key=lambda x: x[1])

#print("Sorted Left array:", sorted_left_with_indices)
#print("Sorted Right array:", sorted_right_with_indices)

# task 1
totalDistance = 0

for i in range(len(sorted_left_with_indices)):
    totalDistance += abs(sorted_left_with_indices[i][1] - sorted_right_with_indices[i][1])

print(totalDistance)

# task 2
similaryScore = 0
for i in range(len(sorted_left_with_indices)):
    current_left_value = sorted_left_with_indices[i][1]
    count = 0
    for right_value in right:
        if right_value == current_left_value:
            count += 1
    similaryScore += current_left_value * count

print(similaryScore)