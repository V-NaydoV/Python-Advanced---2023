input_line = input().split('|')

sub_list = []

for sub_string in input_line[::-1]:
    sub_list.extend(sub_string.split())

print(*sub_list)

