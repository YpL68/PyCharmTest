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

# translation table
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

# folder - file types
FILE_TYPES = {"images":     (".JPEG", ".PNG", ".JPG", ".SVG"),
              "video":      (".AVI", ".MP4", ".MOV", ".MKV"),
              "documents":  (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"),
              "audio":      (".MP3", ".OGG", ".WAV", ".AMR"),
              "archives":   (".ZIP", ".GZ", ".TAR")}

# An alternative for: for key, value in FILE_TYPES.items(): if file_ext in value...
FILE_FOLDER_LINKS = \
    {file_ext: folder for folder, file_types in FILE_TYPES.items() for file_ext in file_types}


def is_wrong_folder_name(folder_name: str) -> bool:
    return bool(re.search(r"[^0-9a-zA-Z_]", folder_name))


def is_folder_empty(path_dir: Path) -> bool:
    return not bool(len([x for x in path_dir.iterdir()]))


def normalize(file_name: str) -> str:
    return "_".join(re.findall(r"\w+", file_name.translate(TRANS)))


def archive_unpack(archive_name: Path):
    shutil.unpack_archive(str(archive_name), str(Path(archive_name.parent, archive_name.stem)))


def parsing_folder(path_dir: Path):
    for item in path_dir.iterdir():
        if item.is_dir():
            if item.name not in FILE_TYPES.keys():
                parsing_folder(item)
        else:
            folder_name = FILE_FOLDER_LINKS.get(item.suffix.upper())
            if folder_name:
                new_item = Path(base_path_dir, folder_name, normalize(item.stem) + item.suffix)
                item.replace(new_item) # with overwriting a file

                if folder_name == "archives": archive_unpack(new_item)
            else:
                item.replace(Path(item.parent, normalize(item.stem) + item.suffix))

    if is_folder_empty(path_dir):
        path_dir.rmdir()
    else:
        if is_wrong_folder_name(path_dir.name):
            path_dir.rename(Path(path_dir.parent, normalize(path_dir.name)))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit("Specify the path to the folder as a command line argument.")
    else:
        base_path_dir = Path(sys.argv[1])
        if not (base_path_dir.exists() and base_path_dir.is_dir()):
            sys.exit("Folder not found.")

    try:
        print("\nStart sorting and grouping files in a folder...\n")

        for folder in FILE_TYPES.keys():
            Path(base_path_dir, folder).mkdir(exist_ok=True)

        parsing_folder(base_path_dir)

        print("The file sorting and grouping was successful.")
    except: #I know it's not recommended
        sys.exit("An error occurred while sorting and grouping files ((")
