from os import walk
import os
import colorama
import sys

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
        print('{}{}/'.format(indent, f"{colorama.Fore.BLUE}{os.path.basename(dirpath)}")) # Print directory
        subindent = ' ' * 2 * (level + 1)
        for f in filenames:
            print('{}{}'.format(subindent, f"{colorama.Fore.GREEN}{f}")) # Print file

def main(USER_PATH):
    if if_path_exists(USER_PATH) == True: # Check if path exists
        print_file_directory(USER_PATH) # Print tree of file and directory
    else: # If path does not exist
        print(f"{colorama.Fore.RED}Path does not exist!")
        
if __name__ == "__main__":
    USER_PATH = sys.argv[1] # Get user path    
    main(USER_PATH) # Call main function
    print(USER_PATH)