rows, cols = [int(num) for num in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

biggest_matrix = []

biggest_sum = float('-inf')

for i in range(rows - 2):
    for j in range(cols - 2):
        first_row = matrix[i][j:j+3]
        second_row = matrix[i+1][j:j+3]
        third_row = matrix[i+2][j:j+3]
        row_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if row_sum > biggest_sum:
            biggest_sum = row_sum
            biggest_matrix.clear()
            biggest_matrix = [first_row, second_row, third_row]
print(f'Sum = {biggest_sum}')
[print(*row) for row in biggest_matrix]
