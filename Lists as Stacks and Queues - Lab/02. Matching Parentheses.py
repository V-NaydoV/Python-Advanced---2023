text = input()

stack_parent = []

for i in range(len(text)):
    if text[i]== '(':
        stack_parent.append(i)
    elif text[i] == ')':
        starting_index = stack_parent.pop()
        final_index = i
        print(text[starting_index:final_index+1])
