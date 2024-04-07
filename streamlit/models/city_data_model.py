import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from io import StringIO

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
        reader_converter = lambda x: pd.DataFrame(pd.read_html(StringIO(str(x)))[0])
        df_list = [reader_converter(table) for table in self.tables]

        # Categorize different types of data
        restaurants = pd.concat([df_list[0], df_list[1]], axis=1).T.drop_duplicates().T
        markets = pd.concat([df_list[2], df_list[3], df_list[4]], axis=1).T.drop_duplicates().T
        transport = pd.concat([df_list[8], df_list[9]], axis=1).T.drop_duplicates().T
        rent_per_month = df_list[5]
        utilities = df_list[11]
        leisure = df_list[12]
        clothing = df_list[13]

        # Collect categorized frames into a list
        categorized_frames = [restaurants, markets, leisure, rent_per_month, transport, utilities, clothing]

        return categorized_frames

    def clean_data(self):
        """
        Clean the data by replacing '-' with NaN and converting to float.

        Returns:
            list: A list of cleaned data frames.
        """
        frames = self.categories
        new_frames = []
        for frame in frames:
            # Step 1: Identify columns to interpolate excluding 'Year'
            interpolate_columns = frame.columns[frame.columns != 'Year']

            # Step 2: Extract the subset of data to interpolate
            data_to_interpolate = frame[interpolate_columns].replace(to_replace="-", value=np.nan)

            # Step 3: Perform interpolation
            interpolated_data = data_to_interpolate.astype(float).interpolate(method='linear')

            # Step 4: Replace the original columns with interpolated data
            frame[interpolate_columns] = interpolated_data.fillna(0)

            # Step 5: Append the modified frame to the list of new frames
            new_frames.append(frame)

        return new_frames
