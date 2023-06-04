rows, cols = [int(num) for num in input().split(", ")]

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

numbers = []
sum_numbers = 0
for i in range(rows-1):
    for j in range(cols-1):
        first_nums = matrix[i][j] + matrix[i][j+1]
        second_nums = matrix[i+1][j] + matrix[i+1][j+1]
        current_sum = first_nums + second_nums
        if current_sum > sum_numbers:
            sum_numbers = current_sum
            numbers = [matrix[i][j], matrix[i][j+1]],[matrix[i+1][j], matrix[i+1][j+1]]

for sublist in numbers:
    print(*sublist)
print(sum_numbers)
