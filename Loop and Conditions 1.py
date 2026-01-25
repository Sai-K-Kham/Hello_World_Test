secret = 7
condition = True
while condition == True:
    guess = int(input("Guess a number between 1 & 10: "))

    if guess < secret:
        print(f'Your guess is too low.')
    elif guess > secret:
        print(f'Your guess is too High.')
    else:
        condition = False
        print(f'Your guess is just Right.')    