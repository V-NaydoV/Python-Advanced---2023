from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))


milkshakes = 0
while milkshakes < 5 and chocolates and milk:
    cup_of_milk = milk.popleft()
    chocolate = chocolates.pop()
    if cup_of_milk <= 0 and chocolate <= 0 :
        continue
    if chocolate <= 0:
        milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        milk.append(cup_of_milk)
        if chocolate -5 <= 0:
            continue
        chocolates.append(chocolate - 5)


if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(ch) for ch in chocolates)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(ch) for ch in milk)}")
else:
    print('Milk: empty')

