def even_odd(*args):
    command = args[-1]

    if command == even:
        return [x for x in args[:-1] if int(x) % 2 == 0]
    else:
        return [x for x in args[:-1] if int(x) % 2 != 0]


print(even_odd(1, 2, 3, 4, 6, 'even'))
