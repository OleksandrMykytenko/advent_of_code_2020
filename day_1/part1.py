from math import prod

REQ_SUM = 2020

numbers = []
res = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        numbers.append(int(line.strip('\n')))

for num in numbers:
    diff = REQ_SUM - num
    if (diff in numbers):
        print("Matching pair: {} + {}".format(num, diff))
        res.append(num)

total = prod(set(res))

print("Result: {}".format(total))
