import re
import sys
import shutil
from pathlib import Path

""" 
    ACHTUNG, ACHTUNG - всвязи с отсутствием образования по английскому языку повсеместно
    применяется гугловский диалект, который, как показала практика, весьма далек от совершенства
"""

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

FILE_EXT_TABLE = (("images", (".JPEG", ".PNG", ".JPG", ".SVG")),
                  ("video",  (".AVI", ".MP4", ".MOV", ".MKV")),
                  ("documents", (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX")),
                  ("audio", (".MP3", ".OGG", ".WAV", ".AMR")),
                  ("archives", (".ZIP", ".GZ", ".TAR")))

def normalize(file_name: str) -> str:
    return "_".join(re.findall(r"(\w+)", file_name.translate(TRANS)))


def is_dir_empty(path_dir: Path) -> bool:
    return not bool(len([x for x in path_dir.iterdir()]))


def parsing_folder(path_dir: Path):
    for item in path_dir.iterdir():
        if item.is_dir():
            if item.name == "Test": raise Exception("Dfcz")
            if item.name not in EXCLUDE_FOLDERS:
                parsing_folder(item)
        else:
            folder_name = FILE_EXT_DICT.get(item.suffix.upper())
            if folder_name:
                item.replace(Path(dir_path, folder_name, normalize(item.stem) + item.suffix))
            else:
                item.replace(Path(item.parent, normalize(item.stem) + item.suffix))

    if is_dir_empty(path_dir): path_dir.rmdir()
    else: path_dir.replace(Path(path_dir.parent, normalize(path_dir.name)))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit("Specify the path to the folder as an argument of the command line.")
    else:
        dir_path = Path(sys.argv[1])
        if not (dir_path.exists() and dir_path.is_dir()): sys.exit("No such folder.")

    # translation table creation
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    FILE_EXT_DICT = {ext: item[0] for item in FILE_EXT_TABLE for ext in item[1]}
    EXCLUDE_FOLDERS = [item[0] for item in FILE_EXT_TABLE]

    for item in FILE_EXT_TABLE: Path(dir_path, item[0]).mkdir(exist_ok=True)

    try:
        parsing_folder(dir_path)
    except:
        sys.exit("When executing the program, an error occurred.")

