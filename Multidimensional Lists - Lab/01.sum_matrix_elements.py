rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]

final_sum = 0

for row in matrix:
    final_sum += sum(row)

print(final_sum)
print(matrix)
