import re

text1 = "Alex\nKdfe23\t\f\v.\r"


def real_len(text):
    return len([i for i in text if i not in ["\n", "\f", "\r", "\t", "\v"]])


articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def sanitize_phone_number(phone):
    return "".join([i for i in phone if i.isdecimal()])


tel_codes = {"SG": "65", "JP": "81", "UA": "380", "TW": "886"}


def get_phone_numbers_for_countries(list_phones: list) -> dict:
    # tel_codes = {"65": "SG", "81": "JP", "380": "UA", "886": "TW"}
    out = {"UA": [], "JP": [], "TW": [], "SG": []}

    for phone in list(map(sanitize_phone_number, list_phones)):
        for itm, val in tel_codes.items():
            if phone.find(val, 0, 3) == 0:
                out.get(itm).append(phone)
                break
        else:
            out.get("UA").append(phone)

    return out



def is_spam_words(text, spam_words, space_around=False):
    spec_symbols = [" ", ",", "."]
    text = text.lower()

    for itm in spam_words:
        pos = text.find(itm.lower())
        if pos != -1 and (space_around == False or
                          ((pos == 0 or text[pos - 1] == " ") and
                           (len(text) == pos + len(itm) or
                            text[pos + len(itm)] in spec_symbols))):
            return True

    return False


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}


def translate(name):
    print(name.title())

#translate("вася пупкин")

def find_word(text, word):
    result = {'result':         False,
              'first_index':    None,
              'last_index':     None,
              'search_string':  word,
              'string':         text}

    match_res = re.search("\\b" + word + "\\b", text)
    if match_res:
        result["result"] = True
        result["first_index"], result["last_index"] = match_res.span()
    return result

def find_all_words(text, word):
    return re.findall("\\b" + word + "\\b", text, re.IGNORECASE)


# print(find_all_words("Guido van Rossum began working on python in the late 1980s, as a \
#         successor to the ABC programming language, and first released it in 1991 as PytHoN 0.9.0.", "Python"))

spam_words1 = ["хрен", "ПиДаРас"]


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub("\\b" + word + "\\b", "*"*len(word), text, flags=re.IGNORECASE)

    return text

#print(replace_spam_words("2 Хрен редьки не слаще. Путин еще тот пидарас.", spam_words1))

def find_all_emails(text):
    result = re.findall(r"([a-zA-Z]{1}[a-zA-Z0-9_.]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})", text)
    #result = re.findall(r"([A-Z])", text)
    return result

def find_all_phones(text):
    # result = re.findall(r"\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{1}-\d{3}", text)
    result = re.findall(r"\+380\(\d{2}\)\d{3}-(?:\d{2}-\d{2}|\d{1}-\d{3})", text)
    #result = re.findall(r"тот (?:\w{3}\d3|\w{4}\d2)", text)
    return result


def find_all_links(text):
    result = []
    iterator = re.finditer(r"(?:https|http)://([a-z0-9_]+\.?)+", text, re.I)
    for match in iterator:
        if match.group()[-1] != '.': result.append(match.group())
    return result

print(find_all_links("The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"))

