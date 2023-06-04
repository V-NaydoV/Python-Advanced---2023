rows = int(input())

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

first_sum = []
second_sum = []
for i in range(rows):
        first_sum.append(matrix[i][i])

for i in range(len(matrix)):
    column_index = len(matrix) - i - 1
    second_sum.append(matrix[i][column_index])


print(f"Primary diagonal: {', '.join(map(str, first_sum))}. Sum: {sum(first_sum)}")
print(f"Secondary diagonal: {', '.join(map(str, second_sum))}. Sum: {sum(second_sum)}")
