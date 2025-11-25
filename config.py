from dotenv import load_dotenv
import os


def get_env_variable(name:str)->str:

    load_dotenv()

    try:
        return os.environ[name]
    except KeyError:
        raise EnvironmentError(f"Environment variable '{name}' not found.")

azure_key = get_env_variable('AZURE_KEY')
city = get_env_variable('CITY')
state = get_env_variable('STATE')
country_iso = get_env_variable('COUNTRY_ISO')

data_folder = 'data'