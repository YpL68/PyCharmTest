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


FILE_TYPES = {"images": {"file_extensions": (".JPEG", ".PNG", ".JPG", ".SVG"),
                         "action": "file_move"},
              "video": {"file_extensions": (".AVI", ".MP4", ".MOV", ".MKV"),
                        "action": "file_move"},
              "documents": {"file_extensions": (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"),
                            "action": "file_move"},
              "audio": {"file_extensions": (".MP3", ".OGG", ".WAV", ".AMR"),
                        "action": "file_move"},
              "archives": {"file_extensions": (".ZIP", ".GZ", ".TAR"),
                           "action": "file_move"}}

# An alternative for: for key, value in FILE_TYPES.items(): if file_ext in value[0]...
FILE_FOLDER_LINKS = \
    {file_ext: folder for folder, params in FILE_TYPES.items() for file_ext in params.get("file_extensions")}

dict1 =  {"file_extensions": (".JPEG", ".PNG", ".JPG", ".SVG"), "action": "file_move"}

dict2 = [i for i in dict1]

print(FILE_FOLDER_LINKS)
print(dict2)
