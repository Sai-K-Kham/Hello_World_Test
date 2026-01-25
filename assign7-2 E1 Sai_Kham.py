5#Assignment 7-2 E1
#Sai_K_Kham

def captureError():
    alist = []
    count = 1
    while count<=20:
        number = input(f'Type number {count} or Enter to quit: ')
        if number !='':
            try:
                number = int(number)
                alist.append(number)
                count = count + 1
                print(alist)
            except:
                print(f'{number} is not an Integer!')
                continue
        else: quit()
    return alist

def main():
    alist = captureError()
    alist.sort()
    alist.reverse()
    print(f'This is the list of numbers from highest to lowest value: {alist}')
    
main()
