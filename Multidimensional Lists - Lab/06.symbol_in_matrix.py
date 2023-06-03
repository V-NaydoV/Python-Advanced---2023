rows = int(input())

matrix = [(list(input())) for _ in range(rows)]

symbol = input()

first_occurrence = None

for row in range(len(matrix)):
    if first_occurrence:
        break
    for col in range(len(matrix)):
        if matrix[row][col] == symbol:
            first_occurrence = (row, col)
            break

if first_occurrence:
    print(first_occurrence)
else:
    print(f'{symbol} does not occur in the matrix')
