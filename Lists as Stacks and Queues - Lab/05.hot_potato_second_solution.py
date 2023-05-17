from collections import deque

def hot_potato(names, number):
    queue = deque(names)
    while len(queue) > 1:
        queue.rotate(-number)
        print(f'Removed {queue.pop()}')
    print(f"Last is {queue.pop()}")


names_of_kids = input().split()
number_of_passes = int(input())

hot_potato(names_of_kids, number_of_passes)
