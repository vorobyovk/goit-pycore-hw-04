import os

PATH = 'cats.txt'

def check_file_exists(path): # function to check if file exist
    return os.path.exists(path)

def get_cats_info(path): # function to get cats info
    if not check_file_exists(path):
        return 'File does not exist'
    else:
        with open(path, 'r') as file:
            lines = file.readlines()
            cats = [] # list to store cats info
            for line in lines:
                # Check if the line has 25 symbols and the third element is a digit
                if line.split(',')[0].count('') == 25 and line.rstrip('\n').split(',')[2].isdigit() == True:
                    cat = {"id":line.split(',')[0], "name":line.split(',')[1], "age":line.rstrip('\n').split(',')[2]}  
                    cats.append(cat)
                else:
                    return 'Invalid data'
        return cats
# Print the result
print(get_cats_info(PATH))