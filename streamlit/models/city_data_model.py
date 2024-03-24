import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from utils.loaders.data_loader import DataLoader
from utils.utils import base_url

class CityDataModel:
    """
    Model class for managing city data.
    """

    def __init__(self, city, url=base_url):
        """
        Initialize the CityDataModel with the given city and base URL.

        Args:
            city (str): The name of the city.
            url (str): The base URL for fetching data.
        """
        self.df = DataLoader().load_data()
        self.city = city
        self.url = url
        self.tables = self.get_tables()
        self.categories = self.categorize_data()
        self.clean_data = self.clean_data()

    def get_tables(self):
        """
        Get tables containing city data from the website.

        Returns:
            list: A list of tables containing city data.
        """
        from io import StringIO
        page = requests.get(self.df.iloc[self.df.loc[self.df['City'] == self.city].index[0]]["Url"])
        one_city_soup = BeautifulSoup(page.content, "html.parser")
        inner_width = one_city_soup.find_all('div', class_='innerWidth')
        results = inner_width[2].find_all('table')
        return results

    def categorize_data(self):
        """
        Categorize the data extracted from tables.

        Returns:
            list: A list of categorized data frames.
        """
        from io import StringIO
        reader_converter = lambda x: pd.DataFrame(pd.read_html(StringIO(str(x)))[0])
        df_list = [reader_converter(table) for table in self.tables]
        market = pd.concat([df_list[2], df_list[3], df_list[4]], axis=1).T.drop_duplicates().T
        leisure = pd.concat([df_list[0], df_list[12]], axis=1).T.drop_duplicates().T
        rental = df_list[5]
        public_transport = df_list[9]
        utilities = df_list[11]
        clothing = df_list[13]
        category_frames = [market, leisure, rental, public_transport, utilities, clothing]
        return [frame.set_index("Year") for frame in category_frames]

    def clean_data(self):
        """
        Clean the data by replacing '-' with NaN and converting to float.

        Returns:
            list: A list of cleaned data frames.
        """
        frames = self.categories
        for frame in frames:
            frame.replace({'-': np.nan}, inplace=True)
            frame = frame.astype(float).infer_objects(copy=False)
        return frames
