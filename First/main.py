import re
import sys
import shutil
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# translation table
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


known_file_extensions = set()
unknown_file_extensions = set()

max_file_name_len = 0

MAX_PRINT_STR_LEN = 60


def file_extension_print(extensions: set, header: str):
    if len(extensions):
        print(header + ":")
        out_str = ", ".join(extensions)
        while len(out_str) > MAX_PRINT_STR_LEN:
            pos = out_str[:MAX_PRINT_STR_LEN].rfind(",")
            if pos == -1:
                break
            else:
                print(out_str[:pos+1].lstrip())
                out_str = out_str[pos+1:].lstrip()
        print(out_str)
    else:
        print(f"{header} not found.\n")


def file_action(file: Path):
    global max_file_name_len  # I know I shouldn't do it.
    if len(file.name) > max_file_name_len: max_file_name_len = len(file.name)

    folder_name = FILE_EXT_LINKS.get(file.suffix.upper(), "unknown_files")
    FILE_TYPES[folder_name]["action"](file, folder_name)  # processing function call


def error_message_print(file: Path, error):
    print(f"An error occurred while processing the {file.name} file:\n{error}")


def known_files_sorting(file: Path, destination_folder: str):
    #new_file_name = normalize(file.stem) + file.suffix
    # with overwriting a file
    try:
        known_file_extensions.add(file.suffix.replace(".", ""))
        file.replace(Path(base_path_dir, destination_folder, normalize(file.stem) + file.suffix))
        FILE_TYPES[destination_folder]["file_list"].append(file.name)
    except OSError as err:
        error_message_print(file, err)


def unknown_files_sorting(file: Path, destination_folder: str):
    # with overwriting a file
    try:
        unknown_file_extensions.add(file.suffix.replace(".", ""))
        file.replace(Path(base_path_dir, destination_folder, file.name))
        FILE_TYPES[destination_folder]["file_list"].append(file.name)
    except OSError as err:
        error_message_print(file, err)


def archive_unpack(file: Path, destination_folder: str):
    # with deleting a archive file
    try:
        known_file_extensions.add(file.suffix.replace(".", ""))
        shutil.unpack_archive(str(file),
                              str(Path(base_path_dir, destination_folder, normalize(file.stem))))
        file.unlink()
        FILE_TYPES[destination_folder]["file_list"].append(file.name)
    except OSError as err:
        error_message_print(file, err)


def is_wrong_folder_name(folder_name: str) -> bool:
    return bool(re.search(r"[^0-9a-zA-Z_]", folder_name))


def is_folder_empty(path_dir: Path) -> bool:
    return not (any(path_dir.iterdir()))


def normalize(file_name: str) -> str:
    return "_".join(re.findall(r"\w+", file_name.translate(TRANS)))


FILE_TYPES = {"images": {"file_ext": (".JPEG", ".PNG", ".JPG", ".SVG"),
                         "file_list": [], "action": known_files_sorting},
              "video": {"file_ext": (".AVI", ".MP4", ".MOV", ".MKV"),
                        "file_list": [], "action": known_files_sorting},
              "documents": {"file_ext": (".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"),
                            "file_list": [], "action": known_files_sorting},
              "audio": {"file_ext": (".MP3", ".OGG", ".WAV", ".AMR"),
                        "file_list": [], "action": known_files_sorting},
              "archives": {"file_ext": (".ZIP", ".GZ", ".TAR"),
                           "file_list": [], "action": archive_unpack},
              "unknown_files": {"file_ext": (),
                                "file_list": [], "action": unknown_files_sorting}}

# An alternative for: for key, value in FILE_TYPES.items(): if file_ext in...
FILE_EXT_LINKS = \
    {file_ext: folder for folder, params in FILE_TYPES.items() for file_ext in params["file_ext"]}


def parsing_folder(path_dir: Path):
    for item in path_dir.iterdir():
        if item.is_dir():
            if item.name not in FILE_TYPES.keys():
                parsing_folder(item)
        else:
            file_action(item)

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

    print("\nStarting to sort files in a folder...")

    # Creating folders to store sorted files
    try:
        for folder in FILE_TYPES.keys():
            Path(base_path_dir, folder).mkdir(exist_ok=True)
    except OSError as err:
        sys.exit(f"An error occurred when creating folders:\n{err}")

    parsing_folder(base_path_dir)

    # Output to console
    if max_file_name_len:
        max_file_name_len = max(max_file_name_len, MAX_PRINT_STR_LEN)
        print("\nThe file sorting was successful.")
        print("\nThe following files were sorted:")

        for key, value in sorted(FILE_TYPES.items()):
            if len(value["file_list"]):
                print("+" + "-" * max_file_name_len + "+")
                print("|{:^{}}|".format(key, max_file_name_len))
                print("+" + "-" * max_file_name_len + "+")

                for i in sorted(value["file_list"]):
                    print("|{:<{}}|".format(i, max_file_name_len))

        print("+" + "-" * max_file_name_len + "+\n")

        file_extension_print(known_file_extensions, "Known file extensions")
        file_extension_print(unknown_file_extensions, "Unknown file extensions")
    else:
        print("No unsorted files found)).")