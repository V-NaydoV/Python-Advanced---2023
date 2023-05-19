from collections import deque

parenthesis = deque(input())


opening_parenthesis = deque()

while parenthesis:
    current_parethesis = parenthesis.popleft()

    if current_parethesis in'({[':
        opening_parenthesis.append(current_parethesis)
    elif not opening_parenthesis:
        print("NO")
        break
    else:
        if f"{opening_parenthesis.pop()}" + current_parethesis not in '(){}[]':
            print('NO')
            break
else:
    print('YES')
