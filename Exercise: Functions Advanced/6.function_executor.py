def func_executor(*arguments):
    result = []

    for func, args in arguments:
        result.append(f'{func.__name__} - {func(*args)}')

    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


results = func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
)


print(results)
