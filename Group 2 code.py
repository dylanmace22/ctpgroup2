#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:48:23 2019

@author: dylanmace
"""
import pandas as pd
#imports pandas module for use
items = pd.read_csv('/Users/dylanmace/Desktop/grocerydata01.csv')
#uses pandas to read the csv file of data and assigns it to the variable items
IL = pd.DataFrame(items, columns= ['item','aisle','price','quantity','store'])
#takes the data from the csv file and puts it into a dataframe
item = items['item'].tolist()
#takes the item names from the data and creates a list
price = items['price'].tolist()
#takes the prices from the data and creates a list
quantity = items['quantity'].tolist()
#takes the quantity left from the data and creates a list
price = list(map(float,price))
#reassigns the price data from a string to a floating point
print(IL.head(50))
#displays all of the items in the console
ask = input ("Would you like to use the shopping cart, the item finder, the total cost, or the quantity left?\n")
if ask == 'item finder'.lower():
    print("Please select the items you want to find with the IF() function with the item name in quotations")
if ask == 'shopping cart'.lower() :
    print("Please select your item numbers from the list above with the IS() function")
if ask == 'total cost'.lower() :
    print("Please select your item numbers from the list above with the totalcost() function")
if ask == 'quantity left'.lower() :
    print("Please select your item numbers from the list above with the quantityleft() function")
# the above lines (25-32) ask for user input on which goal they would like to accomplish and directs them to the correct function
def IS(arg, *argv):
    """
    name- IS
    accepts any amount of arguments
    displays the item name and price of an item in the console
    """
    print (item[arg],price[arg])
    for arg in argv:
        print ("item:",item[arg],price[arg])
        
def IF(x):
    """
    name- IF
    accepts one argument
    displays the location (store and aisle) of an item in the console
    """
    print(IL.loc[IL.item== x])
    
def quantityleft(x):
    """
    name- quantityleft
    accepts one argument
    displays the quantity left of an argument in the console
    """
    print(quantity[x])

costlist=[]
def totalcost(arg,*argv):
    """
    name- totalcost
    accepts any amount of arguments
    displays the total cost based on items selected by the user
    """
    print('\n', "Your Total Cost is")
    first=(price[arg])
    for arg in argv:
        costlist.append(price[arg])
    costlist.append(first)
    print("$",sum(costlist))