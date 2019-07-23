class Movie:
    title = ''
    year = 0
    price = 0.0
    stock = 0

    def __init__(self, title, year, price, stock):
        print("movie constructor")
        self.title = title
        self.year = year
        self.price = price
        self.stock = stock
    
    def print_info(self):
        print("Title: " + self.title)  
        print("Year: " + str(self.year))
        print("Price: " + str(self.price))
        print("Number currently in stock: " + str(self.stock))

#similar function to rent, but increase by 1 