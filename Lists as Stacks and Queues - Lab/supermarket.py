from collections import deque

command = input()
custemours = deque()

while command != 'End':
    if command == "Paid":
        while custemours:
            print(custemours.popleft())
    else:
        custemours.append(command)
    command = input()

print(f"{len(custemours)} people remaining.")

