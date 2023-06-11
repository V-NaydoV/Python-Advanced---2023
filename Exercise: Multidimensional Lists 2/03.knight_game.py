size = int(input())
matrix = [list(input()) for _ in range(size)]
positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'K':
                attacks = 0
                for pos in positions:
                    pos_row = i + pos[0]
                    pos_col = j + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks = [i, j]
                    max_attacks = attacks
    if knight_with_most_attacks:
        row, col = knight_with_most_attacks
        matrix[row][col] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)
