from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))


for order in orders.copy():
    if order <= food_quantity:
        orders.popleft()
        food_quantity -= order
    else:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break

if not orders:
    print('Orders complete')
