def fibonacci(n):
    """Вычисление элемента ряда Фибоначчи методом рекурсии"""

    if n < 0:
        result = fibonacci(n + 2) - fibonacci(n + 1) # Рекурсивный случай
    elif n < 2:
        result = n  # Базовый случай
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2) # Рекурсивный случай

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

if __name__ == '__main__':

    num = int(input("Input number: "))
    print("alt")
    print(fibonacci_alt(num))
    print("recurs")
    print(fibonacci(num))



