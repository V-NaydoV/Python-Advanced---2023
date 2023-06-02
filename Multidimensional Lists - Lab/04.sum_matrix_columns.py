# rows, cols = [int(x) for x in input().split(', ')]
# 
# matrix = [[int(num) for num in input().split(' ')] for _ in range(rows)]
# 
# column_sums = [sum(matrix[row][col] for row in range(rows)) for col in range(cols)]
# 
# for final_sum in column_sums:
#     print(final_sum)


rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(num) for num in input().split(' ')] for i in range(rows)]

for i in range(cols):
    final_sum = 0
    for row in range(len(matrix)):
        final_sum += matrix[row][i]
    print(final_sum)
