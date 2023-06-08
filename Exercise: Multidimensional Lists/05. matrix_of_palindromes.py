rows, cols = [int(x) for x in input().split()]

starting_num = ord('a')

for row in range(starting_num, starting_num + rows):
    for col in range(starting_num, cols + starting_num):
        print(f"{chr(row)}{chr(row + col - starting_num)}{chr(row)}", end=" ")
    print()
