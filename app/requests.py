import requests
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function to receive http request and return an instance of Quote class
    """
    response = requests.get(url).json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote