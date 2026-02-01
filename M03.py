#Sai Khay Kham
#Captalize elements in the list
class Cap:
    def cap(things, elem):
        things = ["mozzarella","cinderalla","salmonella"]
        counter = 0
        for thing in things:
            if thing == "cinderalla":
                print(things[counter].capitalize())
                print(things)
            counter += 1