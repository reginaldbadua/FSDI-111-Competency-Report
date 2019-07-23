# a class can contain:
#   attributes
#   a constructor
#   methods


class Vehicle: 
    make = ''
    year = 0
    cylinders = 0
    color = ''
    price = 0.0

    def __init__(self, make, year, cyls, color, price):
        print("I'm the constructor of Vehicle")
        self.make = make 
        self.year = year
        self.cylinders = cyls
        self.colors = color
        self.price = price

        #this.name = name 

    def start_engine(self):
        print('Engine has started!')

    def stop_engine(self):
        print ('Engine has stopped')

    def print_info(self):
        print ("Vehicle: ")
        print("Make: " + self.make)
        print("Year: " + str(self.year))
        print("Cylinders: "+ str(self.cylinders))
        print("Color: "+ self.color)
        print("Price: " + str(self.price))
    