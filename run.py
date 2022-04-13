import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("cereal_survey_results")


def brands_analysis():
    """
    Returns analysis on the brands question.
    """
    brands = SHEET.worksheet('cereal_brands')
    data = brands.get_all_values()

    print(data)


def types_analysis():
    """
    Returns analysis on the favoured types of cereal question.
    """


def considerations_analysis():
    """
    Returns analysis on the customer considerations questions.
    """


def buying_choice_anaylsis():
    """
    Returns analysis on customer buying regularity question.
    """
    headings = SHEET.worksheet('always_buy_the_same').row_values(1)
    choice = SHEET.worksheet('always_buy_the_same')

    buying_choice = {}

    columns = []
    for ind in range(1, 3):
        column = choice.col_values(ind)
        columns.append(column[-9:])
    
    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        long_average = sum(int_column) / len(int_column)
        average = int(long_average * 100)
        buying_choice.update({heading: average})

    print(buying_choice)
    yes = buying_choice["Yes"]
    no = buying_choice["No"]

    print(yes)
    print(no)

    print(f"The results show that {yes}% of people will always buy the same cereal.")
    print(f"Whereas {no}% of people will vary the cereals they buy.")
    

buying_choice_anaylsis()
