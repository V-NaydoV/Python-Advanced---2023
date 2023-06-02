rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_of_numbers = 0

for i in range(rows):
    sum_of_numbers += matrix[i][i]

print(sum_of_numbers)

