from collections import deque

water_quantity = int(input())
input_line = input()
deque_of_people = deque()


while input_line != 'Start':
    name = input_line
    deque_of_people.append(name)
    input_line = input()

command_line = input()

while command_line != "End":
    tokens = command_line.split()
    if len(tokens) == 1:
        wanted_wated_quantity = int(tokens[0])
        if wanted_wated_quantity <= water_quantity:
            person_name = deque_of_people.popleft()
            print(f"{person_name} got water")
            water_quantity -= wanted_wated_quantity
        else:
            person_name = deque_of_people.popleft()
            print(f"{person_name} must wait")
    else:
        water_quantity += int(tokens[1])
    command_line = input()

print(f"{water_quantity} liters left")
