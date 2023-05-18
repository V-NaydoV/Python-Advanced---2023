
clothes = list(int(x) for x in input().split())

rack_capacity = int(input())

racks_used = 1
rack_space = 0


while clothes:
    if clothes[-1] + rack_space <= rack_capacity:
        rack_space += clothes.pop()
    else:
        racks_used += 1
        rack_space = 0

print(racks_used)

