first_set = set(map(int,input().split()))
second_set = set(map(int, input().split()))

n = int(input())

for i in range(n):
    command , position, *numbers = input().split()
    numbers = set(map(int, numbers))

    if command == 'Add':
        if position == 'First':
            first_set.update(numbers)
        elif position == 'Second':
           second_set.update(numbers)
    elif command == 'Remove':
        if position == "First":
                first_set.difference_update(numbers)
        elif position == 'Second':
            second_set.difference_update(numbers)
    elif command == 'Check':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

first_set_sorted = sorted(first_set)
second_set_sorted = sorted(second_set)

print(', '.join(str(x) for x in first_set_sorted))
print(', '.join(str(x) for x in second_set_sorted))
