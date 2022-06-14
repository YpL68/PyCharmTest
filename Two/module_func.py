def fibonacci(n):

    n = int(n)
    if n < 0:
        result = fibonacci(n + 2) - fibonacci(n + 1) # Рекурсивный случай
    elif n < 2:
        result = n  # Базовый случай
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2) # Рекурсивный случай

    return result




print(fibonacci(11))