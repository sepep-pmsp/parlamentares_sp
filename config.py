data_folder = 'data'

from dotenv import load_dotenv
import os


def get_env_variable(name:str)->str:

    load_dotenv()

    try:
        return os.environ[name]
    except KeyError:
        raise EnvironmentError(f"Environment variable '{name}' not found.")

AZURE_KEY = get_env_variable('AZURE_KEY')
CITY = get_env_variable('CITY')
STATE = get_env_variable('STATE')
COUNTRY_ISO = get_env_variable('COUNTRY_ISO')