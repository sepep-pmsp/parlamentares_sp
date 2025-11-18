data_folder = 'data'


from dotenv import load_dotenv
import os

load_dotenv()

CITY = os.getenv("CITY")
STATE = os.getenv("STATE")
COUNTRY_ISO = os.getenv("COUNTRY_ISO")
AZURE_KEY = os.getenv("AZURE_KEY")