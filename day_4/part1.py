REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid" // this field is optional
]

def validate(person):
    keys = person.keys()
    for field in REQUIRED_FIELDS:
        if field not in keys:
            return False
    return True
        
data = []

with open('input.txt', 'r') as input_file:
    # read file and get records splitted by empty line
    data = [x.replace('\n\n', ' ') for x in input_file.read().split('\n\n')]

valid_count = 0

for passport in data:
    person = {}
    for field in passport.split():
        name, value = field.split(':')
        person[name] = value
    if validate(person):
        valid_count += 1

print("Valid passports count is: {}".format(valid_count))
