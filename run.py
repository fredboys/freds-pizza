from datetime import datetime
import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('freds-pizza')



pizza_menu = {
    "1": {"name":"Margherita", "message":"lovely"},
    "2": {"name":"BBQ Chicken", "message":"amazing"},
    "3": {"name":"Pepperoni", "message":"scrumptious"},
    "4": {"name":"Hawaiian", "message":"delicious"},
    "5": {"name":"Veggie", "message":"tasty"},
    "6": {"name":"Meat Lover", "message":"unreal"},
}

size_price = {
    "S": {"size":"9 INCH", "price": 5, "label": "small"},
    "M": {"size":"11 INCH", "price": 8, "label": "medium"},
    "L": {"size":"13 INCH", "price": 11, "label": "large"},
}

def welcome():
    """
    Function to welcome the customer or 
    leave if they dont want to order
    """
    while True:
        print("Hola, Welcome to Fred's Pizzas!")
        print("Would you like to place and order? [Y]es or [N]o")
        user_choice = input("Enter: ")
        user_choice = user_choice.strip()
        if(user_choice == "Y" or user_choice == "y"):
            print("Lets get you the menu...\n")
            for index, pizza in pizza_menu.items():
                    print(index, pizza["name"])
            break
        elif(user_choice == "N" or user_choice == "n"):
                print("Hopefully see you next time!")
                sys.exit()
        else:
            print("That not quite right")
            print("Make sure you either enetered Y or N\n")
            return welcome()

def select_pizza():
    """
    Function to select the pizza
    """
    while True:
        print(
            "\nPlease pick the corresponding number"
            " to the pizza you wish to order.\n"
            "If you've changed your mind, dont worry"
            " press E to leave the shop.\n"
        )
        user_input = input("Enter number: ")
        user_input = user_input.strip().lower()
        if(user_input == "e"):
            print("We hope to see you another day!")
            sys.exit()
            break
        elif(user_input in pizza_menu):
            print("You have chosen our", pizza_menu[user_input]["message"], pizza_menu[user_input]["name"])
            break
        else:
            print(
                "Sorry this is invalid,"
                "Please enter number between 1-6 or E"
            )
        
    return user_input



def user_name():
    """
    Function collect user name
    """
    while True:
        print("Now... lets take your details")
        name = input("Enter your name: ")
        if(name.isdigit()):
            print(
                "Please make sure you entered your"
                "name correctly"
            )
            print("Try again")
        else:
            print(f"Hello {name}")
            return name

def user_number():
    """
    Function collect user number 
    """
    while True:
        print("Now... lets take your number")
        number = input("Enter your 11 digit number: ")
        if(number.isalpha() or len(number) != 11 ):
            print(
                "Please make sure you entered"
                " your number correctly"
            )
            print("Try again")
        else:
            print(f"We will use {number} to contact you if any problems")
            return number

def main():
    welcome()
    pizza = select_pizza()
    name = user_name()
    number = user_number()

main()