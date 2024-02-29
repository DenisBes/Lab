import os.path as os
def Check(filename):
    os.exists(filename)
    if True:
        print("файл существует")
    if False:
        print("файла нет")

def Dates(filename):
    months = []
    years = []
    with open(filename,'r') as f:
        for l in f:
            part = l.strip().split('/')
            day, month, year = map(int, part)
            months.append(month)
            years.append(year)
    return months, years


def CreateFile(month, year):
    with open('month.txt', 'w') as mf:
        for m in month:
            mf.write(str(m) + '\n')
    with open('year.txt','w') as yf:
        for y in year:
            yf.write(str(y) + '\n')


#main
Check("lab1.txt")
with open("lab1.txt", "r", encoding="utf-8") as f:
    content=f.read()
    print('внутри файла:' + '\n' + content)

month, year = Dates('lab1.txt')
CreateFile(month, year)
