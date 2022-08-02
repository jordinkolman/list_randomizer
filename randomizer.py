#Purpose: randomly assign colors to partygoers
#Author: Jordin Kolman
#Date: 08/02/2022

#imports
import random

#greeting, retrieve list input from user, variable declaration
print("Let's get ready to party.")
list_input = input("Enter the list of names seperated by spaces: ")
party_list = list_input.split(" ")
color_list = [ 'pink', 'bright red', 'orange', 'green', 'sky blue', 'black', 'white', 'maroon', 'navy', 'gray']
#set list
def random_color() :
    #assign random color to each partygoer
    for partygoer in party_list:
        color_choice = random.choice(color_list)
        color_list.remove(color_choice)
        print('The color for', partygoer, 'is', color_choice)


random_color()