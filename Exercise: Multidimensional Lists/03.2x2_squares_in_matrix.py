rows, cols = [int(n) for n in input().split()]

matrix = [input().split() for _ in range(rows)]

equal_square_blocks = 0
for i in range(rows-1):
    for j in range(cols-1):
        symbol = matrix[i][j]
        if matrix[i][j+1] == symbol and matrix[i+1][j] == symbol and matrix[i+1][j+1] == symbol:
            equal_square_blocks += 1
            
print(equal_square_blocks)
