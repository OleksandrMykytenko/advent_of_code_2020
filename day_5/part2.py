seats = []


def convert_to_seat_id(seat):
    row = seat[:7]
    column = seat[7:]

    row = row.replace('F', '0').replace('B', '1')
    column = column.replace('L', '0').replace('R', '1')

    row = int(row, 2)
    column = int(column, 2)

    return row * 8 + column


with open('input.txt', 'r') as input_file:
    for line in input_file:
        seats.append(line.strip('\n'))

seat_ids = []
for seat in seats:
    seat_ids.append(convert_to_seat_id(seat))

seat_ids = sorted(seat_ids)

for i in range(len(seat_ids) - 1):
    if ((seat_ids[i+1] - seat_ids[i]) > 1):
        print("Your seat ID is: {}".format(seat_ids[i] + 1))