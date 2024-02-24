import os

INPUT_DIRECTORY = "src"
OUTPUT_DIRECTORY = "."

FILE_LIST = []

for path, subdirs, files in os.walk(INPUT_DIRECTORY):
    for name in files:
        file_name = os.path.join(path, name)

        if not os.path.isfile(file_name):
            continue

        splitted_path = os.path.normpath(file_name).split(os.sep)
        new_path = os.path.splitext((os.sep).join([OUTPUT_DIRECTORY] + splitted_path[1:]))[0] + ".pdf"
        new_path_parent = (os.sep).join([OUTPUT_DIRECTORY] + splitted_path[1:-1])

        print(new_path_parent)

        if not os.path.exists(new_path_parent):
            os.makedirs(new_path_parent, exist_ok=True)

        FILE_LIST.append((file_name, new_path))

for entry in FILE_LIST:
    os.system(f"typst compile --font-path fonts/ {entry[0]} {entry[1]}")