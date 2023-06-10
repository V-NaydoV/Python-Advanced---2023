rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command_line = input()

while command_line != 'END':
    command, *indices = command_line.split()
    row, col, value = (int(x) for x in indices)
    if row < 0 or col < 0 or row > rows - 1 or col > rows - 1:
        print('Invalid coordinates')
    elif command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value
    command_line = input()

for sub_list in matrix:
    print(*sub_list)
