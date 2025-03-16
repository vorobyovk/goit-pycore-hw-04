import os

PATH = 'sallary2.txt' # path to file

def is_file_exist(path):  # function to check if file exist  
    return os.path.exists(path)

def total_salary(path): # function to calculate total salary and avarage salary
    if is_file_exist(path) == False:
        print("File is not exist")
        return 0,0
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
    
total, avarage = total_salary(PATH)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}") # print total salary and avarage salary
