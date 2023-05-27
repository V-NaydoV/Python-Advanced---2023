n = int(input())
unique_elements = {elements for _ in range(n) for elements in input().split()}
print('\n'.join(unique_elements))
