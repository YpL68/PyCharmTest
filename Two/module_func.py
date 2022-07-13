import re


def fibonacci(n):
    """Вычисление элемента ряда Фибоначчи методом рекурсии"""

    if n < 0:
        result = fibonacci(n + 2) - fibonacci(n + 1)  # Рекурсивный случай
    elif n < 2:
        result = n  # Базовый случай
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный случай

    return result


def fibonacci_alt(n):
    """Вычисление элемента ряда Фибоначчи без применения рекурсии"""

    result = None

    fib_n_minus_1 = 1
    fib_n_minus_2 = 0
    fib_n_plus_2 = 1
    fib_n_plus_1 = 0

    if n < 0:
        i = -1
        while i >= n:
            result = fib_n_plus_2 - fib_n_plus_1
            fib_n_plus_2 = fib_n_plus_1
            fib_n_plus_1 = result
            i -= 1
    elif 0 <= n < 2:
        result = n
    else:
        i = 1
        while i < n:
            result = fib_n_minus_2 + fib_n_minus_1
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = result
            i += 1

    return result


def is_wrong_folder_name(folder_name: str) -> bool:
    return bool(re.search(r"[^0-9a-zA-Z_]", folder_name))

MAX_PRINT_STR_LEN = 6
out_str = "11,22,33,44,55,66,77,88,99"
while len(out_str) > MAX_PRINT_STR_LEN:
    pos = out_str[:MAX_PRINT_STR_LEN].rfind(",")
    if pos == -1:
        break
    else:
        print(out_str[:pos+1].lstrip())
        out_str = out_str[pos+1:].lstrip()
print(out_str)


