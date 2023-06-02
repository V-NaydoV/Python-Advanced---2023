rows = int(input())

matrix = [[int(num) for num in input().split(', ')] for i in range(rows)]

even_num_matrix = [[x for x in listt if x % 2 == 0] for listt in matrix]

print(even_num_matrix)
