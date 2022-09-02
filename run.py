from datetime import datetime
import uuid # Taken from webdev to generate random order number
import sys # Allows the user to exit the system
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
orders_worksheet = SHEET.worksheet("orders")



pizza_menu = {
    "1": {"name": "Margherita", "message": "lovely"},
    "2": {"name": "BBQ Chicken", "message": "amazing"},
    "3": {"name": "Pepperoni", "message": "scrumptious"},
    "4": {"name": "Hawaiian", "message": "delicious"},
    "5": {"name": "Veggie", "message": "tasty"},
    "6": {"name": "Meat Lover", "message": "unreal"},
}

size_price = {
    "S": {"pizza_size": "9 INCH", "price": 5, "label": "Small"},
    "M": {"pizza_size": "11 INCH", "price": 8, "label": "Medium"},
    "L": {"pizza_size": "13 INCH", "price": 11, "label": "Large"},
}

def welcome():
    """
    Function to welcome the customer or
    leave if they dont want to order
    """
    while True:
        print("Hola, Welcome to Fred's Pizzas!")
        print("Would you like to place and order? [Y]es or [N]o\n")
        user_choice = input("Enter: ")
        user_choice = user_choice.strip()
        if(user_choice == "Y" or user_choice == "y"):
            print("\nLets get you the menu...")
            break
        elif(user_choice == "N" or user_choice == "n"):
            print("Hopefully see you next time!")
            sys.exit()
        else:
            print("That's not quite right")
            print("Make sure you either enetered Y or N\n")
            return welcome()

def select_pizza():
    """
    Function to select the pizza
    """
    for index, pizza in pizza_menu.items():
        print(index, pizza["name"])
    while True:
        print(
            "\nPlease pick the corresponding number\n"
            "to the pizza you wish to order.\n"
            "If you've changed your mind,\n"
            "press E to leave the shop.\n"
        )
        user_input = input("Enter number: ")
        user_input = user_input.strip().lower()
        if(user_input == "e"):
            print("We hope to see you another day!")
            sys.exit()
            break
        elif(user_input in pizza_menu):
            print("You have chosen our", pizza_menu[user_input]["message"], pizza_menu[user_input]["name"], "\n")
            break
        else:
            print(
                "Sorry this is invalid,"
                "Please enter number between 1-6 or E"
            )
    return pizza_menu[user_input]

def select_size():
    """
    Function to select the size
    """
    for index, size in size_price.items():
        print(index, "-", size["label"], "-", size["pizza_size"], "-", "£", size["price"])
    while True:
        print(
            "\nPlease select what size pizza you want.\n"
            "Enter either S or M OR L\n"
            "Press E to leave the shop.\n"
        )
        user_size_input = input("Enter size: ")
        user_size_input = user_size_input.strip().upper()
        if(user_size_input == "E"):
            print("We hope to see you soon again!")
            sys.exit()
            break
        elif(user_size_input in size_price):
            print("You have chosen a size", size_price[user_size_input]["label"], size_price[user_size_input]["pizza_size"], "pizza\n")
            break
        else:
            print(
                "Sorry this is invalid\n"
            )

    return size_price[user_size_input]

def number_of_pizzas():
    """
    Function to select quantity of pizzas
    """
    print(
        "How many pizzas would you like?\n"
        "You can pick up to a quantity of 6 pizzas.\n"
        "Press E to leave the shop.\n"
    )
    while True:
        user_quantity_input = input("Enter quantity: \n")
        user_quantity_input = user_quantity_input.strip().lower()
        if(user_quantity_input == "e"):
            print("We hope to see you soon again!")
            sys.exit()
            break
        elif(user_quantity_input >= str(1) and user_quantity_input <= str(6)):
            print("You have selected a quantity of", user_quantity_input)
            break
        else:
            print(
                "Sorry this is invalid\n"
            )
    return user_quantity_input

def add_dip():
    """
    Function allows user to add garlic dip to their order
    """
    while True:
        print("\nWould you like to add a garlic dip for £1?")
        print("[Y]es or [N]o")
        print("Or press E to leave the shop\n")
        user_dip_input = input("Enter: ")
        user_dip_input = user_dip_input.strip().upper()
        if(user_dip_input == "Y"):
            print("\nLets add that to your order!")
            break
        elif(user_dip_input == "N"):
            print("\nNo problem!")
            break
        elif(user_dip_input == "E"):
            print("\nSo close to the best pizza in town. See you soon!")
            sys.exit()
            break
        else:
            print("That not quite right")
            print("Make sure you either enetered Y or N\n")

    return user_dip_input

def total_order(quantity, size, pizza, dip):
    """
    Function to display the order back to the customer
    """
    print("\nYour order is....\n")
    result = quantity + " x " + size["label"] + " " + size["pizza_size"] + " " + pizza["name"]
    if(quantity == str(1)):
        result += " pizza"
    else:
        result += " pizzas"
    if(dip.lower() == "y"):
        result += " with dip"
    print(result)
    return result

def total_cost(size, quantity, dip):
    """
    Function to calculate total cost
    """
    total = size["price"] * int(quantity)
    if(dip == "y" or dip == "Y"):
        total += 1
    print("Total cost: £", total)
    return total

def confirm_order():
    """
    Function to confirm order
    """
    print("\nTo confirm this order please select\n[Y]es or [N]o \n(No will restart the order)\n")
    while True:
        user_confirm = input("Enter: ")
        user_confirm = user_confirm.strip().upper()
        if(user_confirm == "Y"):
            print("\nConfirmed! ")
            break
        elif(user_confirm == "N"):
            print("\nLets try ordering again...\nRestarting process...")
            break
        else:
            print("That not quite right")
            print("Make sure you either enetered Y or N\n")

    return user_confirm

def user_name():
    """
    Function to collect user name
    """
    while True:
        print("\nNow... lets take your details")
        name = input("Enter your name: ").title()
        if(name.isalpha()):
            break
        else:
            print(
                "Please make sure you entered your "
                "name correctly"
            )
            print("Try again")

    return name

def user_number(name):
    """
    Function to collect user number
    """
    while True:
        number = input("Enter your 11 digit mobile number: ")
        if(number.isdigit() and len(number) == 11):
            print("\nThank you", name, "we will use", number, "to contact you \nif any problems\n")
            break
        else:
            print(
                "\nPlease make sure you entered your "
                "number correctly"
            )
            print("Try again\n")

    return number

def receipt(order, price):
    """
    Function to generate recipt
    """
    print(
        "Thank you from Fred's Pizzas\n"
        "Your order has been processed \n"
        "and will be ready for collection in 20 minutes!\n"
    )
    print("Here is your receipt")
    print("---------------------------------")
    print("123 Fred's Pizzas\nBig street\nLondon\n")
    identity = str(uuid.uuid4())
    print("Order #")
    print(identity)
    print(order)
    print("£" + str(price))
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(time)
    print("---------------------------------\n")

    return {"id": identity, "time": time}

def update_spreadsheet(row):
    """
    Function to update google worksheet with data obtained
    """
    orders_worksheet.append_row(row)

def main():
    welcome()
    while True:
        pizza = select_pizza()
        size = select_size()
        quantity = number_of_pizzas()
        dip = add_dip()
        order = total_order(quantity, size, pizza, dip)
        price = total_cost(size, quantity, dip)
        is_confirmed = confirm_order()
        if(is_confirmed.upper() == "Y"):
            break
    name = user_name()
    number = user_number(name)
    receipt_result = receipt(order, price)
    row = [name, number, pizza["name"], size["label"], quantity, dip, price, receipt_result["time"], receipt_result["id"]]
    update_spreadsheet(row)


main()
