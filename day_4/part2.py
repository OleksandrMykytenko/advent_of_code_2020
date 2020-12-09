import re

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

ALLOWED_EYES_COLORS = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
]


def validate_year(value, min_year, max_year, metric):
    try:
        i = int(value)
        if (i < min_year or i > max_year):
            raise ValueError
        return True
    except ValueError:
        return False


def validate_eyes_color(value):
    if (value not in ALLOWED_EYES_COLORS):
        return False
    return True


def validate_hair_color(value):
    return bool(re.search("#[a-fA-F0-9]{6}$", value))


def validate_height(value):
    try:
        if (re.search("[0-9]{3}cm$", value)):
            digit = int(value.strip('cm'))
            if (digit < 150 or digit > 193):
                return False
        elif (re.search("[0-9]{2}in$", value)):
            digit = int(value.strip('in'))
            if (digit < 59 or digit > 76):
                return False
        else:
            raise Exception("unrecognized unit")
        return True
    except Exception:
        return False

def validate_pid(value):
    return bool(re.search("^[0-9]{9}$", value))

def validate(record):
    try:
        if (
            not validate_year(record['byr'], 1920, 2002, 'byr')
            or not validate_year(record['iyr'], 2010, 2020, 'iyr')
            or not validate_year(record['eyr'], 2020, 2030, 'eyr')
            or not validate_height(record['hgt'])
            or not validate_hair_color(record['hcl'])
            or not validate_eyes_color(record['ecl'])
            or not validate_pid(record['pid'])
        ):
            return False
    except KeyError as e:
        return False
    print(record['pid'])
    return True
        
data = []

with open('input.txt', 'r') as input_file:
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
