guess_me = 7
number = 1
condition = True
while condition == True:
    if number < guess_me:
        print('Too low.')
    elif number > guess_me:
        print('oops')
        condition = False
    elif number == guess_me:
        print('fount it!')
    number += 1