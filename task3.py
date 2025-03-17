from os import walk
import os
import colorama

#USER_PATH = "c:/Games"

def if_path_exists(path_var): # Check if path exists
    if os.path.exists(path_var) == True:
        return True
    else:
        return False

def print_file_directory(path_var): # Print tree of file and directory
    structure = walk(path_var)
    level = 0
    for (dirpath, dirnames, filenames) in structure:
        level += 1
        indent = ' ' * 2 * (level)
        print('{}{}/'.format(indent, f"{colorama.Fore.GREEN}{os.path.basename(dirpath)}"))
        subindent = ' ' * 2 * (level + 1)
        for f in filenames:
            print('{}{}'.format(subindent, f"{colorama.Fore.RED}{f}"))

def main(USER_PATH):
    if if_path_exists(USER_PATH) == True:
        print_file_directory(USER_PATH)

if __name__ == "__main__":
    USER_PATH = input("Enter path: ")
    main(USER_PATH)