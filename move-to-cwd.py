#!/usr/bin/python3
# Move all files with the listed suffixes to the cwd

import os
import shutil

cwd = os.getcwd()
file_list = []
suffix0 ="jpg"
suffix1 ="jpeg"
suffix2 ="JPG"
suffix3 ="JPEG"

def move(src, dest):
    shutil.move(src, dest)

def filescan():
    for root, _, filenames in os.walk(cwd):
        for filename in filenames:
            if filename.endswith(suffix0) or filename.endswith(suffix1) or filename.endswith(suffix2) or filename.endswith(suffix3):
                move(os.path.join(root, filename), os.path.join(cwd, filename))
                file_list.append(os.path.join(root, filename))

if __name__ == "__main__":
    filescan()
    print(len(file_list), " Files moved successfully")
