from collections import deque

numbers = deque()

map_function = {
    1: lambda x: numbers.append(x[1]),  # x == number_data
    2: lambda x: numbers.pop() if numbers else None, #if numbers numbers.pop() ilse None
    3: lambda x: print(max(numbers)) if numbers else None, # if numbers print(max(numbers)) else None
    4: lambda x: print(min(numbers)) if numbers else None # if numbers print(min(numbers)) else None
    #  print(min(numbers)) if numbers else None ako neshtoto e vqrno izpulni koda predi nego ako ne napravi sledvashtoto
}
for i in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_function[number_data[0]](number_data)



numbers.reverse()
print(*numbers, sep=', ')


