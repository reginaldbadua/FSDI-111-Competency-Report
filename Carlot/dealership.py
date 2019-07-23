from vehicle import Vehicle
from menu import menu
#list of vehicles in the system
inventory = []
sales = []
data_file = "inventory.dat"
sales_file = "sales.dat"
vehicle_shown = -1

import pickle


# check history of sales; sales []
# push sold vehicles to sales array; add another file
data_file = "sales.dat"
# save sales array
def save_sales():
    writter = open(sales_file,"wb")
    pickle.dump(sales, writter)
    writter.close()
    print('Data Saved!!')

def load_sales():
    reader = open(sales_file, "rb")
    temp = pickle.load(reader)
    for auto in temp:
        sales.append(auto) #put the vehicle back in array
    print('Loaded from DB: ' + str(len(sales)))

# add a menu option to see the history
# add at the bottom of the history, the total amount of money
# (sum each vehicle price)


# logic to ask the user for the vehicle object
# create a vehicle object
# add the vehicle to a list

def save_data():
    writter = open(data_file,"wb")
    pickle.dump(inventory, writter)
    writter.close()
    print('Data Saved!!')

def load_data():
    try:
        reader = open(data_file, "rb")
        temp = pickle.load(reader)
        for auto in temp:
            inventory.append(auto) #put the vehicle back in array
        print('Loaded from DB: ' + str(len(inventory)))
    except:
        print ("nothing to read")

def count_year():
    count = 0
    y = int(input('What year we are looking for: '))
    for item in inventory:
        if(item.year == y):
            count += 1

    print("You have " + str(count))

def create_new():
    print('The user wants to create x')

    try:
        # ask the user for the info
        make = input('Please provide the Make:')
        year_string = input('Please provide the year')
        cyls_string = input ("How many Cylinders")
        color = input("what's the color?")
        price_string = input("what's the price? ")

        year = int(year_string)
        cyls = int(cyls_string)
        price = float(price_string)

        v = Vehicle(make, year, cyls, color, price)
        # push to the list
        inventory.append(v)

        input('Vehicle Created. Press ENTER to continue')

        save_data() #data saved

    except:
        #something crashed above
        print('**Error: some of your data is not valid.')

def show_sales():
    load_sales()
    print ("-"*20)
    print ("  Sales History  ")
    print ("-"*20)
    total = 0.0
    for item in sales:
        print (" " + str(item.year) + " " + item.make + " " + str(item.price))
        total += item.price
    
    print ("-"*20)
    print (" Grand Total: " + str(total))
    input ("Press ENTER to continue")

def sell_vehicle():

    print_list()
    global vehicle_shown

    if (vehicle_shown >= 0):

        conf  = input("Do you want to sell this vehicle [y/n]?: ")
        if (conf == "Y" or conf == "y" ):
            print("Congrats! The sale is final")
            theV = inventory[vehicle_shown] #theMovie
            del inventory[vehicle_shown] # do not execute
            #inventory.pop(vehicle_shown)
            save_data
            theV.start_engine() #theMovie.stock -=1
            sales.append(theV)
            save_sales
        elif (conf == "N" or conf == "n" ):
            print("Too bad...")
        else:
            print("Wrong option, please try again and type y or n")
    else:
        print("***No vehicle is being shown to the client")

def print_list():
    global vehicle_shown
    vehicle_shown = -1
    print("-" * 20)
    print(" Inventory ")
    print("-" * 20)
    count = 1
    for item in inventory:
        #item.print_list()
        print(str(count) + " " + str(item.year) + " " + item.make)
        count +=1
    print("-" * 20)

    try:
        index = input ("View details: ")
        if (index !=""):
            pos = int(index)
            pos -= 1
            vehicle_shown = pos
            car = inventory[pos] #return one vehicle from list
            car.print_info()
    except:
        print("***Error, please try again")
    
        


load_data() 
selection = ''
while selection !='x':
    selection = menu()

    if(selection == '1'):
        create_new()
    elif(selection == '2'):
        print_list()
    elif(selection == '3'):
        count_year()
    elif(selection == '4'):
        sell_vehicle()
    elif(selection == '5'):
        show_sales()