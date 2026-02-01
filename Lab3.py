#Sai Khay Kham
#Lab 3 Super Class

class Vehicle:
    def __init__(self, type):
        self.color = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def get_input():
    while True:
        type = input("What is your vehicle type? (Car, Truck, Plane, Boat or Broomstick) "
              "or type 'q' to quit: ")
        if type.upper() == "Q":
            break
        year = input("What is your vehicle year?: ")
        make = input("What is your vehicle make?: ")
        model = input("What is your vehicle model?: ")
        doors = input("How many doors do you have?(2 or 4): ")
        roof = input("What is your vehicle roof? (solid or sunroof): ")
        return type, year, make, model, doors, roof

#def show_info(type, year, make, model, doors, roof):
#    print(f'Vehicle type: {.type}\n'
#          f'year: {year}\n'
#          f'make: {make}\n'
#          f'model: {model}\n'
#          f'doors: {doors}\n'
#          f'roof: {roof}\n')

def main():
    type, year, make, model, doors, roof = get_input()
    automobile = Automobile(type, year, make, model, doors, roof)
    print(f'Vehicle type: Car\n'    #for some reason I cannot call automobile.type
          f'year: {automobile.year}\n'
          f'make: {automobile.make}\n'
          f'model: {automobile.model}\n'
          f'doors: {automobile.doors}\n'
          f'roof: {automobile.roof}\n')

if __name__ == '__main__':
    main()

