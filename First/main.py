import re
import sys
import shutil
import time
from pathlib import Path

""" 
    ACHTUNG, ACHTUNG - всвязи с отсутствием образования по английскому языку повсеместно
    применяется гугловский диалект, который, как показала практика, весьма далек от совершенства
"""

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}


def is_wrong_folder_name(folder_name: str) -> bool:
    return bool(re.search(r"[^0-9a-zA-Z_]", folder_name))


def is_folder_empty(path_dir: Path) -> bool:
    return not bool(len([x for x in path_dir.iterdir()]))


def normalize(file_name: str) -> str:
    return "_".join(re.findall(r"\w+", file_name.translate(TRANS)))


def archive_unpack(archive_name: Path):
    shutil.unpack_archive(str(archive_name), str(Path(archive_name.parent, archive_name.stem)))


# folder - extensions - postprocessing function
FOLDER_PROPERTIES = {"images":     ((".JPEG", ".PNG", ".JPG", ".SVG"), None),
                     "video":      ((".AVI", ".MP4", ".MOV", ".MKV"), None),
                     "documents":  ((".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"), None),
                     "audio":      ((".MP3", ".OGG", ".WAV", ".AMR"), None),
                     "archives":   ((".ZIP", ".GZ", ".TAR"), archive_unpack)}


def parsing_folder(path_dir: Path):
    for item in path_dir.iterdir():
        if item.is_dir():
            if item.name not in FOLDER_PROPERTIES.keys():
                parsing_folder(item)
        else:
            folder_name = FILE_EXT_DICT.get(item.suffix.upper())
            if folder_name:
                new_item = Path(dir_path, folder_name, normalize(item.stem) + item.suffix)
                item.replace(new_item)

                # postprocessing
                post_func = FOLDER_PROPERTIES.get(folder_name)[1]
                if post_func:
                    post_func(new_item)
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
        dir_path = Path(sys.argv[1])
        if not (dir_path.exists() and dir_path.is_dir()): sys.exit("Folder not found.")

    # translation table creation
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    FILE_EXT_DICT = {extension: folder for folder, properties in FOLDER_PROPERTIES.items() for extension in properties[0]}

    for folder in FOLDER_PROPERTIES.keys():
        Path(dir_path, folder).mkdir(exist_ok=True)

    try:
        print("\nStart sorting and grouping files in a folder...\n")
        parsing_folder(dir_path)
        print("The file sorting and grouping was successful.")
    except: #I know it's not recommended
        sys.exit("An error occurred while sorting and grouping files ((")

