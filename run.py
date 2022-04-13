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
    headings = SHEET.worksheet('cereal_brands').row_values(1)
    choice = SHEET.worksheet('cereal_brands')

    buying_choice = {}

    columns = []
    for ind in range(1, 5):
        column = choice.col_values(ind)
        columns.append(column[-9:])
    
    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = int_column.count(1)
        buying_choice.update({heading: most_popular})

    print(buying_choice)

    popu_choice = max(buying_choice, key=buying_choice.get)
    popu_value = max(buying_choice.values())

    least_popu = min(buying_choice, key=buying_choice.get)
    least_value = min(buying_choice.values())

    print(f"The most popular choice of cereal brand is {popu_choice},")
    print(f"with {popu_value} out of 10 people voting it there go to brand.\n")

    print(f"The least popular choice of cereal brand is {least_popu},")
    print(f"with {least_value} out of 10 people voting it there go to brand.\n")


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

    print(f"The results show that {yes}% of people will always buy the same cereal.\n")
    print(f"Whereas {no}% of people will vary the cereals they buy.\n")
    

def test_function():
    headings = SHEET.worksheet('cereal_brands').row_values(1)
    choice = SHEET.worksheet('cereal_brands')

    buying_choice = {}

    columns = []
    for ind in range(1, 5):
        column = choice.col_values(ind)
        columns.append(column[-9:])
    
    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = int_column.count(1)
        buying_choice.update({heading: most_popular})

    print(buying_choice)

    sorted_dict = dict(sorted(buying_choice.items(), key=lambda x: x[1]))
    print(sorted_dict)

    print(f"The most popular choice of cereal brand is {sorted_dict},")
    print(f"with {popu_value} out of 10 people voting it there go to brand.\n")

    print(f"The least popular choice of cereal brand is {least_popu},")
    print(f"with {least_value} out of 10 people voting it there go to brand.\n")


def main():
    """
    Executes all program functions.
    """
    print("Following the survey carried out on 10 cereal customers")
    print("we have the following results for you to view.\n")
    print("When asked for their favourite cereal brand the results were...")
    brands_analysis()


test_function()