import re
import os.path as os

def Check(filename):
    os.exists(filename)
    if True:
        print("файл существует")
    if False:
        print("файла нет")
def Numbers(file_name):
    num = []
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file, start=0): #перебирает элементы объекта
            numbers = re.findall(r'\d+', line) #ищет все последовательности цифр
            for number in numbers:
                num.append(f'число {number} – номер строки {line_number}')
    return num

def CreateNewFile(num):
    with open('g.txt', 'w') as f:
        for i in num:
            f.write(i + '\n')

#main
Check('lab2.txt')

num = Numbers('lab2.txt')
CreateNewFile(num)

with open("lab2.txt", "r", encoding="utf-8") as f:
    content=f.read()
    print('внутри файла:' + '\n' + content)
