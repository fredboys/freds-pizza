from datetime import datetime
import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_files('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET =GSPREAD_CLIENT.OPEN('freds-pizza')

pizza_menu = {
    "1": "Margherita"
    "2": "BBQ Chicken"
    "3": "Pepperoni"
    "4": "Hawaiian"
    "5": "Veggie"
    "6": "Meat Lover"
}

size_price = {
    "1": "Small - 9 INCH - £5"
    "2": "Medium - 11 INCH - £8"
    "3": "Large - 13 INCH - £12"
}

