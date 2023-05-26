num = int(input())

names = set()

for i in range(num):
    name = input()
    names.add(name)

for name in names:
    print(name)
