import os

for path, subdirs, files in os.walk("."):
    for name in files:
        print(os.path.join(path, name))