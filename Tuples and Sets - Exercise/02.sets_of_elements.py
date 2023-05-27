n, m = [int(x) for x in input().split()]

first_set = {int(input()) for _ in range(n)}
secont_set = {int(input()) for _ in range(m)}

diff_in_first_set = first_set.discard(secont_set)
diff_in_first_set = secont_set.discard(first_set)

print(*first_set.intersection(secont_set), sep='\n')
