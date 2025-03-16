
PATH = 'sallary.txt'

def read_file(path):    
    with open(PATH, 'r') as file:
        


def total_salary(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        index = 0
        total = 0
        avarage = 0
        for line in lines:
            total = total + int(line.split(',')[1])
            index += 1
        avarage = total / index
        return total, avarage

print(total_salary(PATH))
