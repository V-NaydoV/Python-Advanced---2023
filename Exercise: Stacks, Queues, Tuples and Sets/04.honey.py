from collections import deque

bees = deque(int(bee) for bee in input().split())

nectars = deque(int(n) for n in input().split())

symbols = deque(input().split())

symbols_dict = {
    '+': lambda a, b : a + b,
    '-': lambda a, b : a - b,
    '*': lambda a, b : a * b,
    '/': lambda a, b : a / b,
}

collected_nectar = 0

while nectars and bees:
    bee = bees.popleft()
    nectar = nectars.pop()
    if bee > nectar:
        bees.appendleft(bee)
        continue
    elif nectar > bee:
        symbol = symbols.popleft()
        collected_nectar += abs(symbols_dict[symbol](bee, nectar))

print(f"Total honey made: {collected_nectar}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")
