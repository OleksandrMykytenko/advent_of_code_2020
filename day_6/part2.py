raw_data = []

with open('input.txt', 'r') as input_file:
    # read file and get records splitted by empty line
    raw_data = [x.replace('\n', ' ') for x in input_file.read().split('\n\n')]

data = [x.split() for x in raw_data]

res_list = []

for record in data:
    intersection = set(record[0])
    for r in record[1:]:
        intersection = intersection & set(r)
        
    res_list.append(intersection)

total_count = sum([len(x) for x in res_list])

print("Number of answers: {}".format(total_count))