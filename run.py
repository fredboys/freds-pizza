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
    "1": "Margherita",
    "2": "BBQ Chicken",
    "3": "Pepperoni",
    "4": "Hawaiian",
    "5": "Veggie",
    "6": "Meat Lover",
}

size_price = {
    "1": "Small - 9 INCH - £5",
    "2": "Medium - 11 INCH - £8",
    "3": "Large - 13 INCH - £12",
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
                    print(index, pizza)
            break
        elif(user_choice == "N" or user_choice == "n"):
                print("Hopefully see you next time!")
                sys.exit()
        else:
            print("That not quite right")
            print("Make sure you either enetered Y or N\n")
            return welcome()

def pizza_select():
    """
    Function to select the pizza
    """
    while True:
        print(
            "Please pick the corresponding number"
            "to the pizza you wish to order.\n"
            "If you've changed your mind, dont worry"
            "press E to leave the shop.\n"
        )
    select_pizza = input("Enter number or E: ")
    select_pizza = select_pizza.strip()
    if(select_pizza == "1"):
        print("You have chosen our delicious Margherita")
        break
    elif(select_pizza == "2"):
        print("You have chosen our lovely BBQ Chicken")
        break
    elif(select_pizza == "3"):
        print("You have chosen our amazing Pepperoni")
        break
    elif(select_pizza == "4"):
        print("You have chosen our award winning Hawaiian")
        break
    elif(select_pizza == "5"):
        print("You have chosen our stupendous Veggie")
        break
    elif(select_pizza == "6"):
        print("You have chosen our unreal Meat Lover")
        break
    elif(select_pizza == "E" or select_pizza == "e"):
        print("Hope to see you another time!")
        sys.exit()
        break
    else:
        print("Sorry that was an invalid input")
        print("Please enter a number from 1-6 of E")

    return select_book

welcome()
select_pizza()