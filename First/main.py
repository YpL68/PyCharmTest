# import importlib.util
# import sys
import First.module1 as m1
import Two.module2 as m2


# from First.module1 import plus
# from Two.module2 import plus2


def minus(a1, b1):
    return a1 - b1


if __name__ == '__main__':
    TestStr = "Вася Пупкин"
    for i in range(20):
        if not i % 2:
            print(f"Iteration {i}")
        else:
            print("------")



    # iCounter = 0
    # while iCounter < 10:
    #     print(f"Iteration {iCounter + 1}")
    #     iCounter += 1

    # i = int("asd")
    # print(i)
