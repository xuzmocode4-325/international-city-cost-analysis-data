import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from io import StringIO

from models.city_data_model import CityDataModel

class CityDataController:
    """
    Controller class for managing city data.
    """

    def __init__(self, city):
        """
        Initialize the controller with the given city.

        Args:
            city (str): The name of the city.
        """
        self.model = CityDataModel(city)
        self.titles = ["restaurants", "markets", "leisure", "rent", "transport", "utilities", "clothing"]

    def return_records(self):
        # Create a dictionary of dictionaries containing a dict version of each dataframe
        return {title: df.to_dict(orient='records') for title, df in zip(self.titles, self.model.clean_data)}

    def calculate_averages(self):
        """
        Calculates estimated monthly expenditure per cost categoru
        """
        # restaurant estimate
        restaurants = self.model.clean_data[0]
        est_restaurant = round(restaurants.iloc[0:1,1:5].sum().sum(), 2)

        #market estimate
        market = self.model.clean_data[1]
        est_market = round(market.iloc[0:1,1:].sum().sum() * 2, 2)
     
        #leisure estimate
        leisure = self.model.clean_data[2]
        est_leisure = round(leisure.iloc[0:1,1:].sum().sum(), 2)
    
        #rent estimate
        rent = self.model.clean_data[3]
        est_rent = round((rent.iloc[0:1,1:3].sum().mean() + rent.iloc[0:1,3:].sum().mean() / 3) / 2, 2)

        #transport estimate
        transport = self.model.clean_data[4]
        est_transport = round((
            transport.iloc[0:1,3:].sum().sum() + 
            transport.iloc[0:1,2:3].sum().sum() * 30 + 
            transport.iloc[0:1,1:2].sum().sum() * 44 ) / 3, 
        )
        
        #utilities estimate
        utilities = self.model.clean_data[5]
        est_utilities = round(utilities.iloc[0:1,1:].sum().sum() / 2, 2)

        #clothing estimate
        clothing = self.model.clean_data[6]
        est_clothing = round((clothing.iloc[0:1:,1:2].sum().sum() * 4 +
            clothing.iloc[0:1,2:3].sum().sum() * 12 +
            clothing.iloc[0:1,3:4].sum().sum() * 2 +
            clothing.iloc[0:1,4:].sum().sum() * 2
            ) / 12, 2
        )
        


        # Calculate total
        total = np.round(np.array(
            [est_restaurant, est_market, est_leisure, 
             est_rent, est_clothing, est_transport, est_utilities]).sum(), 2)

        return {
            "est_restaurant": est_restaurant,
            "est_market": est_market,
            "est_leisure": est_leisure,  
            "est_rent": est_rent,
            "est_transport": est_transport,
            "est_utilities": est_utilities,
            "est_clothing": est_clothing,
            "est_total": total
        }