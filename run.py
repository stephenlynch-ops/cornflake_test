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


brands_analysis()