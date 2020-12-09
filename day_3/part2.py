import math

data = []

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open('input.txt', 'r') as input_file:
    for line in input_file:
        data.append(line.strip('\n'))

total = 1

for index, slope in enumerate(slopes):
    print("Testing slope for right = {} and down = {}".format(slope[0], slope[1]))

    # set starting point
    x = y = 0
    trees_num = 0

    while(y < len(data) - 1):
        x = (x + slope[0]) % (len(data[0]))
        y += slope[1]
        
        if (data[y][x] == '#'):
            trees_num += 1

    print("Number of tress on my way: {}".format(trees_num))

    total *= trees_num

print("Total number of trees: {}".format(total))