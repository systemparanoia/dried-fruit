#!/usr/bin/env python3

'''This program converts all .XLS files in a directory to PDF using Libre/Open office
Created to assist dad in saving time every month in admin'''

import glob
import subprocess
import os

#set filetype to look for
path = "*.xls"

# Iterate through files in current working directory and remove spaces
def remspc():
    directory = glob.glob(path)
    for filename in directory:
        os.rename(filename, filename.replace(" ", "_"))

# Iterate through files in current working directory and convert to PDF
def convert():
    directory = glob.glob(path)
    for index, fname in enumerate(directory):
        subprocess.check_output(['soffice','--headless', '--convert-to', 'pdf', fname])
        print("\r {} Files Converted!".format(index), end='')

def main():
    print(" Removing spaces from filenames...")
    remspc()
    print(" Done...")
    print("\n Converting files to pdf...")
    convert()
    print("\r All Files Converted!")
    print(" All Done Dad!")

# Run Program
if __name__ == "__main__":
    main()
