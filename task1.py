import os

PATH = 'sallary.txt' # path to file

def is_file_exist(path):  # function to check if file exist  
    if os.path.exists(path) == True:
        return True
    else:
        return False

def total_salary(path): # function to calculate total salary and avarage salary
    if is_file_exist(path) == False:
        return "File is not exist"
    else:
        with open(path, 'r') as file:
            lines = file.readlines()
            index = 0 # index to count number of employers
            total = 0 # total salary
            avarage = 0 # avarage salary
            for line in lines:
                total = total + int(line.split(',')[1])
                index += 1
            avarage = total / index
        return total, avarage

print(total_salary(PATH)) # print total salary and avarage salary
