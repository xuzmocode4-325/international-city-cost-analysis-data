import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils.utils import base_url

class DataLoader:
    def __init__(self, base_url=base_url):
    	self.base_url = base_url
     
    def load_data(self):
        """Load data from the URL."""

        try:
            page = requests.get(self.base_url)
            numbeo_city_soup = BeautifulSoup(page.content, "html.parser")
            results = numbeo_city_soup.find('table', class_='related_links')
            list_cities = results.find_all('a')
            city_name = lambda x: f"({x[0]}) {x[1]}" if len(x) > 2 else x[0]
            city_dict = lambda x: {'City':city_name(x.text.split(",")), 'Country':x.text.split(",")[-1].strip(), 'Url':x["href"]}
            city_pages = [city_dict(city) for city in list_cities]
            df = pd.DataFrame(city_pages)
            return df
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None
