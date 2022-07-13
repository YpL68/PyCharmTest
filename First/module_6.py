import re
import sys
import shutil
from pathlib import Path

""" 
    Альтернатива со списками
"""

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# translation table
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def file_sorting(file: Path):
    folder_name = FILE_EXT_LINKS.get(file.suffix.upper())
    if folder_name:
        FILE_TYPES[folder_name]["file_list"].append(file)
        known_file_types.add(file.suffix)
    else:
        unknown_files.append(file)
        unknown_file_types.add(file.suffix)


def file_action(file: Path):
    folder_name = FILE_EXT_LINKS.get(file.suffix.upper())
    if folder_name:
        FILE_TYPES[folder_name]["action"](file, folder_name)  # processing function call
    else:  # unknown extension
        file.replace(Path(file.parent, normalize(file.stem) + file.suffix))


def file_move(file: Path, destination_folder: str):
    # with overwriting a file
    file.replace(Path(base_path_dir, destination_folder, normalize(file.stem) + file.suffix))


def archive_unpack(archive_name: Path, destination_folder: str):
    # with deleting a archive file
    shutil.unpack_archive(str(archive_name),
                          str(Path(base_path_dir, destination_folder, normalize(archive_name.stem))))
    archive_name.unlink()


def is_wrong_folder_name(folder_name: str) -> bool:
    return bool(re.search(r"[^0-9a-zA-Z_]", folder_name))


def is_folder_empty(path_dir: Path) -> bool:
    return not bool(len([x for x in path_dir.iterdir()]))


def normalize(file_name: str) -> str:
    return "_".join(re.findall(r"\w+", file_name.translate(TRANS)))

unknown_files = []
unknown_file_types = set()
known_file_types = set()

FILE_TYPES = {"images": {"file_ext": (".JPEG", ".PNG", ".JPG", ".SVG"), "file_list": [], "action": file_move},
              "video": {"file_ext": (".AVI", ".MP4", ".MOV", ".MKV"), "file_list": [], "action": file_move},
              "documents": {"file_ext": (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"), "file_list": [], "action": file_move},
              "audio": {"file_ext": (".MP3", ".OGG", ".WAV", ".AMR"), "file_list": [], "action": file_move},
              "archives": {"file_ext": (".ZIP", ".GZ", ".TAR"), "file_list": [], "action": archive_unpack}
              "unknown": {"file_ext": ("-"), "file_list": [], "action": archive_unpack}
             }

# An alternative for: for key, value in FILE_TYPES.items(): if file_ext in...
FILE_EXT_LINKS = \
    {file_ext: folder for folder, params in FILE_TYPES.items() for file_ext in params["file_ext"]}


def parsing_folder(path_dir: Path):
    for item in path_dir.iterdir():
        if item.is_dir():
            if item.name not in FILE_TYPES.keys():
                parsing_folder(item)
        else:
            file_sorting(item)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit("Specify the path to the folder as a command line argument.")
    else:
        base_path_dir = Path(sys.argv[1])
        if not (base_path_dir.exists() and base_path_dir.is_dir()):
            sys.exit("Folder not found.")

    # try:
    print("\nStarting to group files in a folder...\n")

    # Creating folders to store sorted files
    for folder in FILE_TYPES.keys():
        Path(base_path_dir, folder).mkdir(exist_ok=True)

    parsing_folder(base_path_dir)

    print(unknown_files)
    print(unknown_file_types)
    print(known_file_types)

    for item, value in FILE_TYPES.items():
        print(item)
        print(value["file_list"])

    print("The file grouping was successful.")
    # except:  # I know it's not recommended
    #     sys.exit("An error occurred when grouping files ((")
