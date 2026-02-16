#Sai Khay Kham
#Captalize elements in the list
class Cap:
    def cap(things, match):
        counter = 0
        for thing in things:
            if thing == match:
                print(things[counter].capitalize())
                print(things)
            counter += 1

if __name__ == "__main__":
    things = ["mozzarella","cinderalla","salmonella"]
    match = "cinderalla"
    Cap.cap(things, match)
    match = "mozzarella"
    Cap.cap(things, match)
    match = "salmonella"
    Cap.cap(things, match)
#output
#Cinderalla
#['mozzarella', 'cinderalla', 'salmonella']
#Mozzarella
#['mozzarella', 'cinderalla', 'salmonella']
#Salmonella
#['mozzarella', 'cinderalla', 'salmonella']

#with capitalize() method, it only captalize when the method is called.
#but not captalized the element in the list itself.
