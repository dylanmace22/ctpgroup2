# ctpgroup2
Overview
This program is designed to make grocery shopping easy and efficient. It is designed to specifically help with staying on budget by knowing the exact price of an item and the quantity left, as well as navigating store aisles to find exactly what one needs so as to avoid distractions from other unnecessary items. The program also helps with finding the store location for each item to save time.

Getting Started
An excel file was created with 50 common grocery items, the quantity of each item available, the price, specific aisle and store location. The file was imported into spyder and converted into a CSV. Data from the CSV file is converted into a dataframe, which is used to create a list that displays all items and categories in the console. The program begins by asking if the user the would like to use a shopping cart, an item finder, the total cost, or the quantity left.

Useful Examples
IS Function: item & price
IS(7,20,9)
item: Beef 8.99
item: Yogurt 1.33
item: Cucumbers 2.3

IF Function: Item, aisle, price, quantity, store address
IF("Milk")
item - Milk
aisle - Cooler Door 6
price - 3.3
quantity - 2
store - Acme 1709 OH-59, Kent, OH 44241

quantityfinder Function: How much is left of an item
quantityleft(40)
8

totalcost Function: Adds items of total cost together
totalcost(8,2,33)
Your Total Cost is
$ 20.99

Prerequisite
Create an excel file with grocery items, quantity, price, aisle, and store location.
Install the pandas package and import as pd in spyder.

Scope of functionalities
Print list containing 50 common grocery items, the price, aisle, and store location.
Display an item(s) name selected by the user and its price in the console
Display store and aisle location of each item(s) selected by the user
Display the quantity left of each item(s) selected by the user
Display the total cost of all items selected by the user

Authors
Dylan, Luke, Annie, Arjun, Christina, Lisa
