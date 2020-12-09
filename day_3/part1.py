import math

data = []

RIGHT_SHIFT = 3
DOWN_SHIFT = 1

with open('input.txt', 'r') as input_file:
    for line in input_file:
        data.append(line.strip('\n'))

# set starting point
x = y = 0
trees_num = 0

while(y < len(data) - 1):
    x = (x + RIGHT_SHIFT) % (len(data[0]))
    y += DOWN_SHIFT
    
    if (data[y][x] == '#'):
        trees_num += 1

print("Number of tress on my way: {}".format(trees_num))