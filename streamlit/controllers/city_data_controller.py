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


    def calculate_averages(self):
        # Calculate market average
        market = self.model.clean_data[0].astype(float).interpolate().fillna(0)
        p_mark =  round(market.iloc[0].sum() * 2, 2)

        # Calculate leisure average
        leisure = self.model.clean_data[1].astype(float).interpolate().fillna(0)
        p_leis = round((leisure.iloc[0,:3].mean() + 
            (leisure.iloc[0,3] + leisure.iloc[0,4] * 4) / 2 +
            leisure.iloc[0,5]), 2)

        # Calculate rental average
        rental = self.model.clean_data[2].astype(float).interpolate().fillna(0)
        p_rent = round(((rental.iloc[0,2:] / 3).mean() + rental.iloc[0,:2].mean()) / 2, 2)

        # Calculate public transport average
        transport = self.model.clean_data[3].astype(float).interpolate().fillna(0)
        p_trans = round(transport.iloc[0].sum() * 1.5, 2)

        # Calculate utilities average
        utilities = self.model.clean_data[4].astype(float).interpolate().fillna(0)
        p_utils = round(utilities.iloc[0].mean(), 2)

        # Calculate clothing average
        clothing = self.model.clean_data[5].astype(float).interpolate().fillna(0)
        p_cloth = round((clothing.iloc[0,:2].sum() +
        clothing.iloc[0,2:].mean() / 4), 2)

        # Calculate total
        total = np.round(np.array([p_cloth, p_utils, p_trans, p_rent, p_leis, p_mark]).sum(), 2)

        return {
            "Avg. Market": p_mark,
            "Avg. Leisure": p_leis,  
            "Avg. Rent": p_rent,
            "Avg. Transport": p_trans,
            "Avg. Utilities": p_utils,
            "Avg. Clothing": p_cloth,
            "Avg. Total": total
        }