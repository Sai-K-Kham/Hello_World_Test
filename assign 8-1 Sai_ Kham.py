#Assignment 8-1
#Exercise 1
#Sai_K_Kham

from tabulate import tabulate

def inilize():
    file = open('Geraldines Businesses.csv','r')
    data = [["CustomerID","Last Name", "First Name","Address","City","State","Zip Code","Rate"],[]]
    return data,file

def addData(file,data):
    for line in file:
        data[1].append(line.split(','))
    return data

def turningTable(data):
    table = tabulate(
        data[1],
        headers = data[0],
        tablefmt = 'grid'
        )
    print(table)
    
def main():
    data,file = inilize()
    addData(file,data)
    turningTable(data)
    file.close()

main()
