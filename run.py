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
        columns.append(column[1:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = int_column.count(1)
        buying_choice.update({heading: most_popular})

    no_people = int_column.count(0) + int_column.count(1)

    print("  Question 1: (recap)")
    print("  -------------------")
    print("  Which of the following brands do you buy?")
    print("  The options were a)Kellogs b)Nestle c)Quaker d)Other \n")

    kellogs_value = buying_choice['Kellogs']
    nestle_value = buying_choice['Nestle']
    quaker_value = buying_choice['Quaker']
    other_value = buying_choice['Other']

    kellogs_perc = calc_market_share(kellogs_value, no_people)
    nestle_perc = calc_market_share(nestle_value, no_people)
    quaker_perc = calc_market_share(quaker_value, no_people)
    other_perc = calc_market_share(other_value, no_people)
    print("  Results:")
    print("  --------")
    print("  Their answers indicate the market share is divided as below;\n")
    print("  The results show a brands market share (No votes / Total votes)")
    print(f"  Kellogs: {kellogs_perc}% share ({kellogs_value}/{no_people})")
    print(f"  Nestle: {nestle_perc}% share ({nestle_value}/{no_people})")
    print(f"  Quaker: {quaker_perc}% share ({quaker_value}/{no_people})")
    print(f"  Other brands: {other_perc}% share ({other_value}/{no_people})\n")

    top_brand = max(buying_choice, key=buying_choice.get)
    print(f"  This indicates that {top_brand} are the market leader.\n")

    return no_people


def buying_choice_anaylsis():
    """
    Returns analysis on how likely the customers are to buy the
    same cereal everytime they shop of cereals.
    """
    print("  Question 2: (recap)")
    print("  -------------------")
    print("  Would you consider changing to a different cereal in the future?")
    print("  The options were a) Yes b) No \n")
    headings = SHEET.worksheet('always_buy_the_same').row_values(1)
    choice = SHEET.worksheet('always_buy_the_same')

    buying_choice = {}

    columns = []
    for ind in range(1, 3):
        column = choice.col_values(ind)
        columns.append(column[1:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        long_average = sum(int_column) / len(int_column)
        average = int(long_average * 100)
        buying_choice.update({heading: average})

    yes = buying_choice["Yes"]
    no = buying_choice["No"]

    print("  Results:")
    print("  --------")
    print(f"  The results indicate {no}% of people stick to the same brand.")
    print(f"  Whereas {yes}% of people will vary the cereals they buy.\n")

    if yes == 0:
        print(f"  There is definetly no room for a new brand as {no}% of ")
        print("  people are unwilling to try a new brand. \n")
    elif no > yes:
        print("  There would be room for a new brand to enter this market")
        print(f"  Although with only {yes}% of customers who would ")
        print("  potentially be willing to try it. \n")
    elif no == 0:
        print("  The results suggest that there is definetly room for a new ")
        print(f"  brand to enter this market as {yes}% of customers were")
        print("  willing to change. \n")
    else:
        print("  There is definetly room for a new brand to enter the market")
        print(f"  in fact {yes}% were willing to try a new brand compared to ")
        print(f"  {no}% who would not be willing to try it. \n")


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
        columns.append(column[1:])

    for heading, column in zip(headings, columns):
        int_column = [int(num) for num in column]
        most_popular = sum(int_column)
        option_dict.update({heading: most_popular})

    print("  Question 3: (recap)")
    print("  -------------------")
    print("  What do you consider when picking a new cereal?")
    print("  The options were a)Price b)Packaging c)Box Size d)Healthier\n")
    print("  We asked the participants to indicate the most likely")
    print("  consideration with a 3, the next most likely with a 2. The next ")
    print("  most likely with a 1 and the lowest consideration with a 0.\n")

    price_value = option_dict['Price']
    packaging_value = option_dict['Packaging']
    box_size_value = option_dict['Box Size']
    healthier_option_value = option_dict['Healthier Choice']
    print("  Results:")
    print("  --------")
    print("  The results were as follows;")
    print(f"  Price: {price_value}pts (out of a possible maximum of 60)")
    print(f"  Packaging: {packaging_value}pts")
    print(f"  Box Size: {box_size_value}pts")
    print(f"  Healthier Option: {healthier_option_value}pts \n")

    top_consideration = max(option_dict, key=option_dict.get)

    print(f"  This indicates customers consider {top_consideration} as the")
    print("  main consideration when choosing a new cereal. This is ")
    print("  something a new brand would need to consider when entering the")
    print("  market or trying to maintain market share. \n")


def move_on():
    """
    Function that allows user to move onto the next question and
    analyse the data.
    """
    input("  Press enter to continue \n")


def main():
    """
    Executes all program functions.
    """
    print("  Survey on cereal buying customers to ascertain favoured")
    print("  brands, if they would change there current pattern and if")
    print("  so what considerations they would make in picking a new")
    print("  cereal. This is being done to see if there is market space")
    print("  for a new brand to move into this market. \n")
    print("  We have the following results for you to view.\n")
    move_on()
    print("  *************************")
    print("  Getting results for you now... \n")
    print("  *************************")
    brands_analysis()
    print("  *************************")
    move_on()
    buying_choice_anaylsis()
    print("  *************************")
    move_on()
    new_cereal_considerations()
    print("  ***** END OF REPORT *****")


main()

# def test_function():
#     print("  The options were a) Yes b) No \n")
#     headings = SHEET.worksheet('always_buy_the_same').row_values(1)
#     choice = SHEET.worksheet('always_buy_the_same')

#     buying_choice = {}

#     columns = []
#     for ind in range(1, 3):
#         column = choice.col_values(ind)
#         columns.append(column[1:])
#     print(columns)


# test_function()
