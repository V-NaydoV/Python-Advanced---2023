number = int(input())
longest_range = []

for _ in range(number):
    first_data, second_data = [x.split(',') for x in input().split('-')]

    first_range = range(int(first_data[0]), int(first_data[1])+1)
    second_range = range(int(second_data[0]), int(second_data[1])+1)

    intersection = list(set(first_range) & set(second_range))
    intersection_length = len(intersection)

    if intersection_length > len(longest_range):
        longest_range = intersection

print(f"Longest intersection is {longest_range} with length {len(longest_range)}")
