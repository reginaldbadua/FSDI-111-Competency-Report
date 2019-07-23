from movie import Movie
from menu import menu
stock = []
stock_file = "stock.dat"
movies_shown = -1

import pickle

def load_stock():
    try:
        reader = open(stock_file, "rb")
        temp = pickle.load(reader)
        for auto in temp:
            stock.append(auto) 
        print('Loaded from DB: ' + str(len(stock)))
    except:
        print ("nothing to read")

# logic to create movie
# add the vehicle to a list
def save_stock():
    writer = open(stock_file,"wb")
    pickle.dump(stock, writer)
    writer.close()
    print('Data Saved!!')

def create_new():
    try:
        title = input('Title of the movie: ')
        year_string = input('Year movie was made: ')
        year = int(year_string)
        price_string = input ("Rental price: ")
        price = float(price_string)
        number_available = int(input('Number in stock:  '))
        m = Movie(title, year, price, number_available)

        stock.append(m)

        input('Movie created -- Press ENTER to continue')

        save_stock()

    except Exception as e:
        print('**Error: some of your data is not valid.')
        print (e)

def print_list():
    global movies_shown
    movies_shown = -1
    print("-" * 20)
    print(" Stock ")
    print("-" * 20)
    count = 1
    for item in stock:
        #item.print_list()
        print(str(count) + " " + (item.title) + " " + str(item.year) + " " + str(item.stock))
        count +=1
    print("-" * 20)

    try:
        index = input ("View details: ")
        if (index !=""):
            pos = int(index)
            pos -= 1
            movies_shown = pos
            movie = stock[pos] 
            movie.print_info()
    except:
        print("***Error, please try again")

def rent_movie():
    print_list()
    global movies_shown

    if(movies_shown >= 0):

        conf = input ("Do you want to rent this movie [Y/N]?:  ")
        if (conf == "Y" or conf == "y" ):
            print("Movie is rented")
            theMovie = stock[movies_shown]
            theMovie.stock -=1
            save_stock()
        elif (conf == "N" or conf == "n" ):
            print ("Choose another movie")
    else:
        print("No movie is currently being shown to user")

def return_movie():
    print_list()
    global movies_shown

    if (movies_shown >= 0):

        conf =  input ("Return this movie?")
        if (conf == "Y" or conf == "y" ):
            print("Movie is rented")
            theMovie = stock[movies_shown]
            theMovie.stock +=1
            save_stock()
        elif (conf == "N" or conf == "n" ):
            print ("Choose another movie")
    else:
        print("No movie is currently being shown to user")


load_stock()
selection = ''
while selection !='x':
    selection = menu()

    if(selection == '1'):
        create_new()
    elif(selection == '2'):
        print_list()
    elif(selection == '3'):
        rent_movie()
    elif(selection == '4'):
        return_movie()
