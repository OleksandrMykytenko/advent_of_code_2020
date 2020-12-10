raw_data = []

with open('input.txt', 'r') as input_file:
    # read file and get records splitted by empty line
    raw_data = [x.replace('\n', ' ') for x in input_file.read().split('\n\n')]

data = [set(rec.replace(' ', '')) for rec in raw_data]

total_count = sum([len(x) for x in data])

print("Number of answers: {}".format(total_count))
