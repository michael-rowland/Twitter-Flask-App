from basilica import Connection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_KEY = getenv('BASILICA_API_KEY') 

connection = Connection(API_KEY)

if __name__ == "__main__":
        connection = connection