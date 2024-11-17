# Eugenia Ceinos
# UWYO COSC 1010
# Submission Date: 11/17/2024
# Lab 09
# Lab Section: 16
# Sources, people worked with, help given to: none

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria

# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    def __init__(self, size, sauce = "red"):
        self.size = size
        self.sauce = sauce
        self.toppings = ["cheese (free)"]
    
    def get_size(self):
        return self.size
    
    def get_sauce(self):
        return self.sauce
    
    def get_toppings(self):
        return self.toppings
    
    #ex. newToppings = ["Pepperoni", "...", ",,,"]
    def add_toppings(self, newToppings):
        for topping in newToppings:
            self.toppings.append(topping)

    def getAmountOfToppings(self):
        return len(self.toppings)
    
    def set_size(self, size):
        if size.isdigit() == False or int(size) < 10:
            self.size = 10
        else:
            self.size = int(size)


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


#INCLUDE ALL THE TOPPINGS EXCEPT THE ONE'S THAT'S ALREADY THERE, "CHEESE" TO THE PRICE.
class Pizzeria:
    def __init__(self, orders = 0, price_per_topping = 0.3, price_per_inch = 0.6):
        self.pizzas = []
        self.orders = orders
        self.price_per_topping = price_per_topping
        self.price_per_inch = price_per_inch

    def placeOrder(self):
        #   - This method will allow a customer to order a pizza.
        #     - Which will increment the number of orders.
        #   - It will need to create a pizza object.
        #   - You will need to prompt the user for:
        #     - the size
        #     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
        #     - all the toppings the user wants, ending prompting on an empty string.
        #     - Implementation of this is left to you; you can, for example:
        #       - have a while loop and append new entries to a list
        #       - have the user separate all toppings by a space and turn that into a list.
        #   - Upon completion, create the pizza object and store it in the list.
        size = input("Please enter the size of pizza, as a whole number. The smallest size is 10\n")
        sauce = input("What kind of sauce would you like?\nLeave blank for red sauce \n")
        if not sauce:
            sauce = "red"
        order = Pizza(size, sauce)
        order.set_size(size)

        toppings = []
        while True:
            toppings_inp = input("Please enter the toppings you would like, leave blank when done\n")
            if not toppings_inp:
                break
            toppings.append(toppings_inp)
        order.add_toppings(toppings)

        self.orders += 1
        self.pizzas.append(order)
    
    def getPrice(self):
        # - getPrice()
        #   - You will need to determine the price of the pizza.
        #   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
        #   - You will have to retrieve the pizza from the pizza list.
        current = self.pizzas[-1]
        topping = current.getAmountOfToppings()
        topping -= 1
        price = (current.get_size() * self.price_per_inch) + topping * self.price_per_topping
        return price
    
    def getReceipt(self):
        # - getReceipt()
        #   - Creates a receipt of the current pizza.
        #   - Show the sauce, size, and toppings.
        #   - Show the price for the size.
        #   - The price for the toppings.
        #   - The total price.
        current = self.pizzas[-1]
        sauce = current.get_sauce()
        size = current.get_size()
        toppings = current.get_toppings()
        n_of_toppings = current.getAmountOfToppings()
        n_of_toppings -= 1
        size_price = size * self.price_per_inch
        toppings_price = n_of_toppings * self.price_per_topping
        print(f"You ordered a {size}'' pizza with {sauce} sauce and the following toppings:")
        for topping in toppings:
            print("\t" * 8, topping)
        print(f"You ordered a {size}'' pizza for ${size_price}")
        print(f"You had {n_of_toppings} topping(s) for ${toppings_price}")
        price = self.getPrice()
        print(f"Your total price is ${price} \n")



# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

pizzeria = Pizzeria()
while True:
    customer = input("Would you like to place an order? exit to exit\n")
    if customer == "exit":
        break
    
    pizzeria.placeOrder()
    pizzeria.getReceipt()
print(f"There were {pizzeria.orders} orders")
