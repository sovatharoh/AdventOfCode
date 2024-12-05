puzzle = []

with open('day4/input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        puzzle.append(row)

# Get dimensions of the 2D array
rows = len(puzzle)
cols = len(puzzle[0]) if rows > 0 else 0
searchWord = 'XMAS'


# Loop through each element
for i in range(rows):
    for j in range(cols):
        element = puzzle[i][j]
        if element == 'X':
            














