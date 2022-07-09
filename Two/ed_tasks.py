import math
import time


def sqrt(i): return i * i


# ----------- task 5  ---------------#
# Найдите три ключа с самыми высокими значениями в словаре

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

bb = [a for a in dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)).values()][:3]
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# print(bb)
# print(result)
# print(my_dict.get('a'))

"""Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине 
и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел."""

n = 10
n1 = [1]
n2 = [0]


# while n:
#     print(n1)
#     n1 = [n1[x] + n1[x+1] for x in range(len(n1) - 1)]
#     n1.insert(0, 1)
#     n1.append(1)
#     n -= 1

# print(n1 + n2)
# n1.extend(n2)
# print(n1)

def pascal_triangle(n):
    row = [1, 2, 3, 4, 7]
    y = [0]
    for x in range(n):
        if row: print(row)
        row = [left + right for left, right in zip(row, row[3::])]


#      row = [left + right for left, right in zip(row + y, y + row)]

# pascal_triangle(4)


kkk = [[1, "ggfg2", 3], [4, 5, 6]]

mf, lp = kkk

# df = list(zip(mf, lp))
# kf = [list(aa) for aa in zip(*kkk)]
# print(kf)
lll = list((1, 2, 3))

fgh = (1, 2, 3, 4, 5, 6)
# mkl = tuple([i for i in fgh])
# print(mkl)

# print(kkk)
#
# h, j, k = kkk[0]
#
# print(h)
# print(j)
# print(k)
#
# for a, b, c in kkk:
#    print(a)
#    print(b)
#    print(c)


# bbb = zip([1, 1] + [0], [0] + [1, 1])
# for left in bbb:
#     print(left)
# print(right)

# ddd = ((3, 4), (3, 6))
# for q, w in ddd:
#     print(q)
#     print(w)

# mm = map(sqrt, fgh)
# kkk = [sqrt(i) for i in fgh]
# print(tuple(mm))
# print(tuple(kkk))

#При заданном целом числе n посчитайте n + nn + nnn.


def calc_value(n):
   print(n + n**2 + n**3)


def solve(n):
   n1 = str(n)
   n2 = str(n) * 2 #int(str(n) * 2)
   n3 = str(n) * 3 #int(str(n) * 3)
   print(n1 + n2 + n3)

"""Напишите программу, которая выводит чётные числа из 
заданного списка и останавливается, если встречает число 237."""

# list5 = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,237,34,56,78,56]
# list_out = []
# for i in list5:
#    if i == 237: break
#    if not i % 2: list_out.append(i)
#
# print(list_out)

# def f(n):
#    if n == 3:
#       return 3
#    else:
#       return f(n - 1) + n
#
# print(f(5))
#
# print(math.pow(2, 2))

# def f2(**kwargs):
#    for i in kwargs.items(): print(i)
#
#
# f2(b1= 1, b32= 2, b43= "3", b50= 4)

def is_easy_num(n: int) -> bool:
    is_easy = True
    for i in range(2, n):
        if not n % i:
            is_easy = False
            break
    return is_easy


def easy_num_list(n):
    return [i for i in range(2, n + 1) if is_easy_num(i)]


# print(easy_num_list(30))


def converet_to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
    return seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60 + \
        weeks * 7 * 24 * 60 * 60


def twoSum(nums, target):
    d = {}
    for i, a in enumerate(nums):
        if (target - a) in d:
            return [d[target - a], i]
        else:
            d[a] = i




def two_sum(nums: list, target: int) -> list:
    result = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
            if result: break
    return result



def twoSum_a(nums, target):
    seen = {}
    # print(type(seen))

    for i, num in enumerate(nums):
        to_search = target - num

        if to_search in seen:
            return [i, seen[to_search]]

        seen[num] = i


# a = [4, 6, 7]
# print(twoSum_a([4, 6, 7], 13))


# b = list(enumerate(a))
# print(b)
# print(type(b))


# print(two_sum([-3,4,3,90],0))
# def add_two_numbers(l1, l2):
#     num1 = 0
#
#     def convert_list_to_num(list1):
#         num = 0
#         for i in range(len(list1)):
#             num += list1[i] * (10 ** i)
#         return num
#
#
#
#     len_l1 = len(l1)
#     len_l2 = len(l2)
#     for i in range(len_l1):
#         num1 += int(lambda i: l1[i] * (10 ** i))
#     return num1
#
#
# print(add_two_numbers([5, 6, 8], []))


# def test(l1: ListNode, l2):
#     num1 = sum(list(map(lambda x: l1[x] * 10 ** x, range(len(l1)))))
#     num2 = sum(list(map(lambda x: l2[x] * 10 ** x, range(len(l2)))))
#     return [x for x in (str(num1 + num2)[::-1])]


# print(test([2,4,3], [5,6,4]))

# def lengthOfLongestSubstring(s: str) -> int:
#     len_s = len(s)
#     if len_s < 2: return len_s
#
#     dop_str = ""
#     cur_max_len = 0
#     k = 0
#     i = 0
#     while i < len_s:
#         if cur_max_len == len_s - k:
#             break
#
#         if s[i] not in dop_str:
#             dop_str += s[i]
#             i += 1
#         else:
#             if len(dop_str) > cur_max_len:
#                 cur_max_len = len(dop_str)
#
#             dop_str = ""
#             k += 1
#             i = k
#
#     if len(dop_str) > cur_max_len: cur_max_len = len(dop_str)
#
#     return cur_max_len

def lengthOfLongestSubstring(s: str) -> int:
    chars = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        res = max(res, r - l + 1)

    return res


    # len_s = len(s)
    # if len_s < 2: return len_s
    #
    # dop_str = ""
    # cur_max_len = 0
    # k = 0
    # i = 0
    # while i < len_s:
    #     if cur_max_len >= len_s - k:
    #         break
    #     if s[i] not in dop_str:
    #         dop_str += s[i]
    #         i += 1
    #     else:
    #         if len(dop_str) > cur_max_len:
    #             cur_max_len = len(dop_str)
    #         dop_str = ""
    #         k += 1
    #         i = k
    #
    # if len(dop_str) > cur_max_len: cur_max_len = len(dop_str)
    #
    # return cur_max_len

#print(lengthOfLongestSubstring("pwwkew"))

#print(lengthOfLongestSubstring("assdfghjkl"))

# s = "qwertyeoiertue toirt oiet uoierut eoitu oiutueoiruteoirtu reoiut eorit oier utoi!er"
# i = 0
# print("start")
# while i < 10000000:
#     i += 1
#     a = "!" in s
# print("end")
# print(a)

# s = "qwertyeoiertue toirt oiet uoierut eoitu oiutueoiruteoirtu reoiut eorit oier utoi!er"
# i = 0
# print("start")
# while i < 10000000:
#     i += 1
#     a = s.i
# print("end")
# print(a)


# def test():
#     s = "qwertyeoiertue toirt oiet uoierut eoitu oiutueoiruteoirtu reoiut eorit oier utoi!er"
#     i = 0
#     while i < 10000000:
#         i += 1
#         a = s[12]


# start = time.process_time()
# test()
# end = time.process_time()
# print(str(end-start))

#print(math.log(3 + 2))

# fg = [1, 6, 67, 80]
# fgf = [2, 5, 10, 12, 30, 45, 100]
# k = fg + fgf
# print()

# def findMedianSortedArrays(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: float
#     """
#     if len(nums2) == len(nums1) == 1: return (nums1[0] + nums2[0]) / 2
#
#     if len(nums2) > len(nums1):
#         list_min, list_max = nums1, nums2
#     else:
#         list_min, list_max = nums2, nums1
#
#     max_index = (len(nums2) + len(nums1)) // 2
#     elem_max = list_max[max_index]
#     elem_min = list_max[max_index - 1]
#
#
#
#     for i in list_min:
#         if i >= elem_max: break
#         elif i > elem_min:
#             elem_min = i
#
#
#
#
#     return (elem_max + elem_min) / 2

# print(findMedianSortedArrays([1,3], [2]))

# s = "asdfgh"
# if "asd" in s: print("ccc")

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
#-----------------------------------------------------------
    # len_s = len(s)
    # for i in range(len_s):
    #     for k in range(i + 1):
    #         str1 = s[k: len_s - (i - k)]
    #         if str1 == str1[::-1]: return str1
#-----------------------------------------------------------
    if len(s) < 2: return s

    d = 1
    start = end = 0
    str_out = ""
    count = 0

    while count < 2:
        for i in range(d, len(s)):
            s1 = s[i - d: i + 1]
            if s1 == s1[::-1]:
                end = i + 1
                start = i - d

                if i - d >= 1:
                    d += 2

        d = end - start
        if d > len(str_out): str_out = s[start: end]
        end = start = 0

        count += 1

    return str_out

# print(longestPalindrome("112555567893asdfdsa7469862064gtsjgclkj"))
# print(longestPalindrome("11112345556789"))


#print(longestPalindrome(""))


# def longestPalindrome1(s):
#     mx = 1
#     st = 0
#
#     if len(s) <= 1 or s == s[::-1]:
#         return s
#
#     for i in range(1, len(s)):
#
#         o = s[i - mx - 1:i + 1]
#         e = s[i - mx:i + 1]
#
#         if o == o[::-1] and i - mx - 1 >= 0:
#             st = i - mx - 1
#             mx += 2
#         elif e == e[::-1]:
#             st = i - mx
#             mx += 1
#
#     return s[st:st + mx]

# def longestPalindrome2(s):
#     maxx = 1
#     start = 0
#     if len(s) <= 1 or s == s[::-1]:
#         return s
#     else:
#         for i in range(1, len(s)):
#             odd = s[i - maxx - 1:i + 1]
#             even = s[i - maxx:i + 1]
#             print(f"odd {odd}")
#             print(f"even {even}")
#
#             if odd == odd[::-1] and i - maxx - 1 >= 0:
#                 start = i - maxx - 1
#                 maxx = maxx + 2
#             elif even == even[::-1]:
#                 start = i - maxx
#                 maxx = maxx + 1
#     return s[start:start + maxx]

# print(longestPalindrome2("bbcdqwert"))


def convert(s, numRows):
    if numRows <= 1 or len(s) <= numRows: return s

    str_arr = []
    idx = 0
    inc = -1
    str_arr = [""] * numRows
    #for i in range(numRows): str_arr.append("")

    for i in range(len(s)):
        str_arr[idx] += s[i]
        if not i % (numRows - 1):
            inc = -inc
        idx += inc

    return "".join(str_arr)

print(convert("1234", 3))

divmod()