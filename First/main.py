import importlib.util
import sys
# import module1
# import module2
from First.module1 import plus
from Two.module2 import plus2

def minus(a1, b1):
    return a1 - b1


if __name__ == '__main__':
    print(minus(1,2))
    print(plus(7,9))
    print(plus2(7,9))
