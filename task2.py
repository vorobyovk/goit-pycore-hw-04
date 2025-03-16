import os

PATH = 'cats.txt'

def check_file_exists(path):
    return os.path.exists(path)

def get_cats_info(path):
    if not check_file_exists(path):
        return 'File does not exist'
    else:
        with open(path, 'r') as file:
            lines = file.readlines()
            cats = []
            for line in lines:
                cat = line.strip().split()
                cats.append(cat)
        return cats

print(get_cats_info(PATH))