import re

def is_integer(s: str):
    s = s.strip()
    return len(s) > 0 and (s.isdigit() or
                           (s[1::].isdigit() and
                            (s[0] == "+" or s[0] == "-")))


def capital_text(s):
    if not s: return ""

    spec_chars = (".", "!", "?")

    list_char = list(s)
    last_char_is_spec = True

    for ind in range(len(list_char)):
        if list_char[ind] in spec_chars:
            last_char_is_spec = True
        else:
            if last_char_is_spec and list_char[ind] != " ":
                list_char[ind] = str(list_char[ind]).upper()
                last_char_is_spec = False

    return "".join(list_char)


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    result = ""
    if reverse: riddle = riddle[::-1]

    start_index = riddle.find(start_letter)
    if start_index != -1 and start_index + word_length <= len(riddle):
        result = riddle[start_index: start_index + word_length]

    return result


test_list = [[1,2,3,7,8,0], [3,4], [5,6]]

def data_preparation(list_data: list):
    out_list = []
    for lst in list_data:
        if len(lst) > 2:
            lst.sort()
            out_list.extend(lst[1:len(lst)-1])
        else: out_list.extend(lst)

    out_list.sort(reverse=True)

    return out_list

ss = "((2)+ 34 ) -(5 * 3)"
def token_parser(s: str):
    if not s: return []

    out_list = []
    temp_str = ""
    operators = ["*", "/", "-", "+", "(", ")"]
    for char in s:
        if char == " ": continue

        if char in operators:
            if temp_str: out_list.append(temp_str)
            out_list.append(char)
            temp_str = ""
        else:
            temp_str += char

    if temp_str: out_list.append(temp_str)

    return out_list

#print(token_parser(ss))


list_ss = [1,2,3]
oo = [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]
aa = [[], [4, 6, 1, 3], [6, 1, 3], [1, 3], [3], [4, 6, 1], [6, 1], [1], [4, 6], [6], [4]]

def all_sub_lists(data: list):
    out_list = [[]]
    for i in range(len(data)):
        for j in range(0, len(data)-i):
            out_list.append(data[j:j+(i+1)])

    return out_list


    # while len(data):
    #     for index in range(len(data)):
    #         out_list.append(data[index:])
    #
    #     data.pop()

def make_request(keys: list, values: list) -> dict:
    if len(keys) != len(values):
        return {}
    else:
        return dict(zip(keys, values))


#print(make_request([3,2,1], ["a", "b", "c"]))

CHARS = ((" ",), (".", ",", "?", "!", ":"), ("A", "B", "C"), ("D", "E", "F"), ("G", "H", "I"), ("J", "K", "L"),
         ("M", "N", "O"), ("P", "Q", "R", "S"), ("T", "U", "V"), ("W", "X", "Y", "Z"))

TRANS = {ord(char): str(i) * (CHARS[i].index(char) + 1) for i in range(len(CHARS)) for char in CHARS[i]}


def sequence_buttons(string):
    return re.sub(r"[^0-9]", "", string.upper().translate(TRANS))


#print(sequence_buttons("Hello, World!"))


def file_operations(path, additional_info, start_pos, count_chars):
    result = ""
    if not path: return ""
    with open(path, 'a') as fh:
        fh.write(additional_info)

    with open(path, 'r') as fh:
        fh.seek(start_pos)
        try:
            result = fh.read(count_chars)
        except MemoryError:
            print("Memory Error")

    return result



#print(file_operations("Text3.txt", "additional_info", 5, 10))


def get_employees_by_profession(path: str, profession: str):
    with open(path, 'r') as fh:
        list_str = fh.readlines()

    return " ".join([i.split()[0] for i in list_str if i.lower().
                    find(profession.lower()) != -1])


#print(get_employees_by_profession(r"Test\Test1.txt", "cook"))

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh_src:
        with open(output_file, 'w') as fh_dest:
            num_str = 0
            for line_src in fh_src:
                fh_dest.write(str(num_str) + ": " + line_src)
                num_str += 1

#to_indexed(r"Test\Test1.txt", r"Test\Test2.txt")


#in_list = [[1, 2, [3, 4, [5, 6]], 7]]
#in_list = [0, [1,2], 5, 6]


def flatten(data: list):
    if not len(data): return []

    if type(data[0]) == list:
        list1 = flatten(data[0])
        list2 = flatten(data[1:])
    else:
        list1 = data[0:1]
        list2 = flatten(data[1:])

    list1.extend(list2)

    return list1

in_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
qw_wqwq = ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
out_list = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]



def decode(data):
    if not len(data): return []

    list1 = list((data[0] * data[1]))
    list2 = decode(data[2:])

    list1.extend(list2)

    return list1


#print(decode(in_list))


def encode(data):
    if not len(data): return []

    old_char = data[0]
    count = 0

    for char in data:
        if char == old_char:
            count += 1
        else: break

    list1 = [old_char, count]
    list2 = encode(data[count:])

    list1.extend(list2)

    return list1

print(encode(out_list))