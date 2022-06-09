# import importlib.util
# import sys
import First.module1 as m1
import Two.module2 as m2

# import module2
# from First.module1 import plus
# from Two.module2 import plus2

def minus(a1, b1):
    return a1 - b1


if __name__ == '__main__':
    print(minus(1,2))
    print(m1.plus(7,9))
    print(m2.plus2(7,9))
