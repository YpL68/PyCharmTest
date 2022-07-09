import timeit
import random

#----------- 6. Zigzag Conversion -----------------#
def convert(s, numRows):
    if numRows == 1 or len(s) <= numRows: return s

    str_arr = []
    idx = 0
    inc = -1
    str_arr = [""] * numRows
    #for i in range(numRows): str_arr.append("")

    for i in range(len(s)):
        str_arr[idx] += s[i]
        if not i % (numRows - 1): inc = -inc
        idx += inc
    return "".join(str_arr)


#--------------- 9. Palindrome Number ---------------#

def isPalindrome(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    elif x < 10: return True

    in_list = list(str(x))

    # r = 0
    # in_list = []
    #
    # while x:
    #     x, r = divmod(x, 10)
    #     in_list.append(r)
    #
    # print(in_list)

    m_len = len(in_list)
    m_idx = m_len // 2

    if not m_len % 2:
        if in_list[m_idx] != in_list[m_idx - 1]: return False
        else:
            in_list.pop(m_idx - 1)
            m_len -= 1
            m_idx -= 1

    for i in range(m_idx + 1, m_len):
        if in_list[i] != in_list[-(i + 1)]: return False

    return True



def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x = -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])

    if -2**31 <= x <= 2**31 - 1: return x
    else: return 0

#print(reverse(123))

def myAtoi(s):

    i = 0
    s = s.lstrip()

    if not len(s): return 0

    if not (s[i].isdecimal() or s[i] == "+" or s[i] == "-"): return 0
    else:
        for i in range(1, len(s)):
            if not s[i].isdecimal(): break
        else:
            i += 1

    res_str = s[:i]
    if len(res_str) == 1 and not s[0].isdecimal(): return 0

    result = int(res_str)

    if result > (2**32 - 1): result = 2**31 - 1
    elif result < -2**31: result = -2**31

    return result

#print("The time taken is ",timeit.timeit(stmt=testcode))



#testcode = '''
def maxArea(height) -> int:
    # s_max = 0
    # idx_left = 0
    # idx_right = len(height) - 1
    # lenght = idx_right
    #
    # if (lenght) < 1: return 0
    #
    # while idx_left != idx_right:
    #     h_left = height[idx_left]
    #     h_right = height[idx_right]
    #     s = min(h_left, h_right) * lenght
    #     if s > s_max: s_max = s
    #     if h_left < h_right:
    #         while height[idx_left] <= h_left and idx_left != idx_right:
    #             idx_left += 1
    #             lenght -= 1
    #     else:
    #         while height[idx_right] <= h_right and idx_left != idx_right:
    #             idx_right -= 1
    #             lenght -= 1

    #return s_max

    # 5 вариант
    h = 0
    s_max = 0
    lenght = len(height) - 1
    regions = [0, -1]
    reg_index = 0
    delta = 1

    while lenght:
        if height[regions[0]] < height[regions[1]]:
            reg_index = 0
            delta = 1
            h = height[regions[0]]
        else:
            reg_index = 1
            delta = -1
            h = height[regions[1]]

        s = h * lenght
        if s > s_max: s_max = s
        while lenght and height[regions[reg_index]] <= h:
            regions[reg_index] += delta
            lenght -= 1

    return s_max

#'''
# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,8,6,2,5,4,8,25,7]))
#print(maxArea([8,10,14,0,13,10,9,9,11,11]))
# print(maxArea([100,0,0,0,46,0,0,0,0,20]))
# print(maxArea([1,2,4,3]))
# print(maxArea([1,2,4,4,1,1]))
# print(maxArea([1,2,5,5,2]))
print(maxArea([1,1]))
# print(maxArea([]))
# print(maxArea([0, 0]))

# bb = \
#     [76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111, 115,
#      76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20, 185, 171,
#      23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125, 143, 12, 76,
#      192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81, 163, 146, 75, 92,
#      198, 126, 191]
# print(maxArea(bb))

#print(timeit.timeit(stmt=testcode))













