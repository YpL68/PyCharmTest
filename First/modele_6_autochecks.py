from pathlib import Path
import itertools
import re
import base64
import shutil

pets = [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
       ]

"""
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
"""

bb = ['60b90c1c13067a15887e1ae1,Tayson,3\n',
      '60b90c2413067a15887e1ae2,Vika,1\n',
      '60b90c2e13067a15887e1ae3,Barsik,2\n',
      '60b90c3b13067a15887e1ae4,Simon,12\n',
      '60b90c4613067a15887e1ae5,Tessi,5\n']

cc = [["60b90c1c13067a15887e1ae1","Tayson","3", [1,2,3]], ["60b90c2e13067a15887e1ae3" ,"Barsik","2", [2,4,5]]]


# def get_cats_info(path):
#     result = []
#     with open(path, "r") as file:
#         for item in file.readlines():
#             key, name, age = item.replace("\n", "").split(",")
#             result.append({"id": key, "name": name, "age": age})
#
#     print(result)
#
#     return result

#get_cats_info(r"f:\PythonPrj\Test\First\Test\Test.txt")
#print(Path(__file__).resolve().parent)
#print(Path(".").absolute())

was = {
        "id": "60b90c3b13067a15887e1ae4",
        "name": "Watermelon Cucumber Salad",
        "ingredients": [
            "1 large seedless watermelon",
            "12 leaves fresh mint",
            "1 cup crumbled feta cheese"]
        }

def get_recipe(path, search_id):
    with open(path, "r") as file:
        for line in file:
            if line.startswith(search_id):
                list = line.replace("\n", "").split(",")
                return {"id": list[0], "name": list[1], "ingredients": list[2:]}

    return None

#print(get_recipe(r"f:\PythonPrj\Test\First\Test\Test.txt", "56644"))


def sanitize_file(source, output):
    data = None
    with open(source, "r") as file:
        data = file.read()

    with open(output, "w") as file:
        file.write(re.sub(r"\d", "", data))

#sanitize_file(r"f:\PythonPrj\Test\First\Test\Test.txt", r"f:\PythonPrj\Test\First\Test\Test1.txt")

abit = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

ass = ['Robert Stivenson,28', 'Alex Denver,30']

def save_applicant_data(source, output):
    with open(output, "w") as file:
        for stud in source:
            file.write(",".join([str(data) for data in stud.values()]) + "\n")

#save_applicant_data(abit, r"f:\PythonPrj\Test\First\Test\Test1.txt")


str16 = "Вася".encode("utf16")
str8 = "Вася1".encode("utf8")

def is_equal_string(utf8_string, utf16_string):
    return utf8_string.decode('utf-8').casefold() == \
           utf16_string.decode('utf-16').casefold()

#print(is_equal_string(str8, str16))

users = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}


def save_credentials_users(path, users_info):
    with open(path, "wb") as file:
        for usr, pas in users_info.items():
            file.write(f"{usr}:{pas}\n".encode())

#save_credentials_users(r"f:\PythonPrj\Test\First\Test\Test1.txt", users)


def get_credentials_users(path):
    with open(path, "rb") as file:
        bb = [line.decode().replace("\n", "") for line in file.readlines()]
        return [base64.b64encode(line.encode()).decode() for line in bb]

#print(get_credentials_users(r"f:\PythonPrj\Test\First\Test\Test1.txt"))

employee_res = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

def create_backup(path, file_name, employee_residence):
    with open(f"{path}/{file_name}", "wb") as file:
        for usr, country in employee_residence.items():
            file.write(f"{usr} {country}\n".encode())

    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name


#print(create_backup(r"f:\PythonPrj\Test\First\Test", "Test1.txt", employee_res))

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


unpack(r"f:\PythonPrj\Test\First\backup_folder.zip", r"f:\PythonPrj\Test\First\Test2")