#Assignment 8-1
#Exercise 2
#Sai_K_Kham

def main():
    report = open('report.txt','w')
    UMM = input('Anything you write on the screen will duplicated in the report.txt file: ')
    report.write(UMM)
    report.close()

main()
