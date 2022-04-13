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


def calc_market_share(value, no_people):
    """
    Function calculates a percentage of the market share - based
    on the survey size.
    """

    survey_coverage = no_people
    market_share = (value / survey_coverage) * 100

    return market_share


def brands_analysis():
    """
    Return analysis on favoured cereal brands. It calculates the estimated
    market share.
    The brands analysed were;
    - Kellogs
    - Nestle
    - Quaker
    - Other brands
    """

    headings = SHEET.worksheet('cereal_brands').row_values(1)
    choice = SHEET.worksheet('cereal_brands')

    buying_choice = {}

    columns = []
    for ind in range(1, 5):
        column = choice.col_values(ind)
        columns.append(column[-20:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = int_column.count(1)
        buying_choice.update({heading: most_popular})

    no_people = int_column.count(0) + int_column.count(1)
    # print(f"The survey covered a total of {no_people} people.")
    
    print("Question 1:")
    print("Which of the following brands do you buy?")
    print("The options were a)Kellogs b)Nestle c)Quaker d)Other \n")

    kellogs_value = buying_choice['Kellogs']
    nestle_value = buying_choice['Nestle']
    quaker_value = buying_choice['Quaker']
    other_value = buying_choice['Other']

    kellogs_perc = calc_market_share(kellogs_value, no_people)
    nestle_perc = calc_market_share(nestle_value, no_people)
    quaker_perc = calc_market_share(quaker_value, no_people)
    other_perc = calc_market_share(other_value, no_people)

    print("Their answers indicate the market share is divided as below;\n")
    print(f"Kellogs has a {kellogs_perc}% share ({kellogs_value} / {no_people} people surveyed)")
    print(f"Nestle has a {nestle_perc}% share ({nestle_value} / {no_people})")
    print(f"Quaker has a {quaker_perc}% share ({quaker_value} / {no_people})")
    print(f"Other brands have a {other_perc}% share ({other_value} / {no_people}) \n")

    return no_people


def buying_choice_anaylsis():
    """
    Returns analysis on how likely the customers are to buy the
    same cereal everytime they shop of cereals.
    """
    print("Question 2:")
    print("Would you consider changing to a different cereal in the future?")
    print("The options were a) Yes b) No \n")
    headings = SHEET.worksheet('always_buy_the_same').row_values(1)
    choice = SHEET.worksheet('always_buy_the_same')

    buying_choice = {}

    columns = []
    for ind in range(1, 3):
        column = choice.col_values(ind)
        columns.append(column[-20:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        long_average = sum(int_column) / len(int_column)
        average = int(long_average * 100)
        buying_choice.update({heading: average})

    yes = buying_choice["Yes"]
    no = buying_choice["No"]

    print(f"The results indicate {yes}% of people stick to the same brand.")
    print(f"Whereas {no}% of people will vary the cereals they buy.\n")


def new_cereal_considerations():
    """
    Shows analysis on the main considerations customers make when
    choosing a new cereal.
    The catagories they could choose from were;
    - Price
    - Packaging
    - Box Size
    - Healthier Choice
    """
    headings = SHEET.worksheet('considerations').row_values(1)
    choice = SHEET.worksheet('considerations')

    option_dict = {}

    columns = []
    for ind in range(1, 5):
        column = choice.col_values(ind)
        columns.append(column[-20:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = sum(int_column)
        option_dict.update({heading: most_popular})
    
    print("Question 3:")
    print("What do you consider when picking a new cereal?")
    print("The options were a)Price b)Packaging c)Box Size d)Healthier Choice \n")
    print("We asked the participants to indicate the most likely")
    print("consideration with a 3, the next most likely with a 2. The next ")
    print("most likely with a 1 and the lowest consideration with a 0.\n")

    price_value = option_dict['Price']
    packaging_value = option_dict['Packaging']
    box_size_value = option_dict['Box Size']
    healthier_option_value = option_dict['Healthier Choice']
    print("The scores were as follows;")
    print(f"Price: {price_value}pts (out of a possible maximum of 60)")
    print(f"Packaging: {packaging_value}pts")
    print(f"Box Size: {box_size_value}pts")
    print(f"Healthier Option: {healthier_option_value}pts \n")

    top_consideration = max(option_dict, key=option_dict.get)
    # print("Maximum value:", top_consideration)
    print(f"This indicates that customers consider {top_consideration} as the main")
    print("consideration when choosing a new cereal.\n")


def move_on():
    """
    Function that allows user to move onto the next question and
    analyse the data.
    """
    next_question = input("Press enter to continue \n")


def main():
    """
    Executes all program functions.
    """
    
    print("The survey has been carried out as requested.")
    print("we have the following results for you to view.\n")
    print("Getting results for you now... \n")
    brands_analysis()
    move_on()
    buying_choice_anaylsis()
    move_on()
    new_cereal_considerations()


main()
