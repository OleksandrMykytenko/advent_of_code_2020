from math import prod

REQ_SUM = 2020

pairs = []
numbers = []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        numbers.append(int(line.strip('\n')))

for num in numbers:
    for sec_num in numbers[1:]:
        sum_local = num + sec_num
        if (sum_local < REQ_SUM):
            pairs.append((num, sec_num))

for pair in pairs:
    sum_local = sum(pair)
    third = REQ_SUM - sum_local
    if third in numbers:
        print(third, pair)
        print(third * pair[0] * pair[1])
        break