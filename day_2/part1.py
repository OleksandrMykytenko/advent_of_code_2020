def custom_split(record):
    policy, password = record.split(':')
    password = password.strip()
    num_constraints, char = policy.split()
    min_num, max_num = [int(x) for x in num_constraints.split('-')]

    return (password, char, min_num, max_num)


def validate(password, char, min, max):
    c = password.count(char)
    if (c < min or c > max):
        return False
    else:
        return True

res = 0

with open('input.txt', 'r') as input_file:
    for line in input_file:
        if (validate(*custom_split(line.strip('\n')))):
            res += 1


print("Number of valid passwords: {}".format(res))