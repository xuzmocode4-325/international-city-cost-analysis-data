import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

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
        market = self.model.clean_data[0].astype(float).interpolate()
        p_mark = round(market.loc[2023].sum() * 2, 2)

        # Calculate leisure average
        leisure = self.model.clean_data[1].astype(float).interpolate()
        p_leis = round(leisure.loc[2023].sum() / 3, 2)

        # Calculate rental average
        rental = self.model.clean_data[2].astype(float).interpolate()
        p_rent = round(rental.loc[2023].mean(), 2)

        # Calculate public transport average
        public_transport = self.model.clean_data[3].astype(float).interpolate()
        p_trans = public_transport.loc[2023].sum()

        # Calculate utilities average
        utilities = self.model.clean_data[4].astype(float).interpolate()
        p_utils = round(utilities.loc[2023].astype(float).sum() / 4, 2)

        # Calculate clothing average
        clothing = self.model.clean_data[5].astype(float).interpolate()
        p_cloth = round(clothing.loc[2023].sum() / 2, 2)

        # Calculate total
        total = p_cloth + p_utils + p_trans + p_rent + p_leis + p_mark

        return {
            "Avg. Market": p_mark,
            "Avg. Leisure": p_leis,
            "Avg. Rent": p_rent,
            "Avg. Transport": p_trans,
            "Avg. Utilities": p_utils,
            "Avg. Clothing": p_cloth,
            "Avg. Total": '{:,.2f}'.format(total)
        }