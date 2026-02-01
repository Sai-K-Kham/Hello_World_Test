#Sai
#Functions

#part_1
def good():
    good = ['Harry', 'Ron', 'Hermione']
    return good

print(good())

#part_2
def get_odds():
    odds = []
    for i in range(10):
        if i%2 != 0:
            odds.append(i)
    print(odds)
    return odds

odds = get_odds()
print(odds[2]) #Third position of the list
