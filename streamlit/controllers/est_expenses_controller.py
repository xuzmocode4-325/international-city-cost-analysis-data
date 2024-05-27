import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from models.est_expenses_model import EstExpensesModel
from views.est_expenses_view import EstExpensesView
from controllers.city_data_controller import CityDataController

from utils.utils import green_shades, orange_shades

plt.rc('xtick', labelsize=21)  
plt.rc('ytick', labelsize=21)

class EstExpensesController:
    """
    Controller class for managing estimated expenses.
    """

    def __init__(self):
        """
        Initialize the controller with default values.
        """
        self.model = EstExpensesModel()
        self.view = EstExpensesView()

    def calculate_estimated_expenses(self):
        """
        Calculate the total estimated expenses.
        """
        total_expenses = self.model.calculate_total_expenses(
            self.model.restaurant, self.model.rent, 
            self.model.transport, self.model.market, 
            self.model.utilities, self.model.clothing, 
            self.model.leisure
        )
        self.expenses = total_expenses

    def update_expenses(self):
        """
        Update the estimated expenses.
        """
        self.calculate_estimated_expenses()

    def plot_side_side_bar(self, city):
        """
        Plot a side-by-side horizontal bar chart of estimated expenses.

        Args:
            city (str): The name of the city to plot expenses for.
        """
        city_data_controller = CityDataController(city)
        city_estimates = city_data_controller.calculate_averages()

        # Extracting y1 and y2 data
        y1 = [
            city_estimates["est_restaurant"], 
            city_estimates["est_rent"],
            city_estimates["est_transport"],
            city_estimates["est_market"],
            city_estimates["est_utilities"], 
            city_estimates["est_clothing"], 
            city_estimates["est_leisure"],
        ]
        y2 = [self.model.restaurant, self.model.rent, self.model.transport, self.model.market,
              self.model.utilities, self.model.clothing, self.model.leisure]

        # Define x values
        x = np.arange(len(y1))

        # Define width of bars
        width = 0.4

        # Plotting the side-by-side horizontal bar chart
        fig, ax = plt.subplots(figsize=(15, 10))
        ax.margins(tight=True)
        ax.set_frame_on(False)

        # Plot the first set of bars (Estimated Costs)
        rects1 = ax.bar(x - width/2, y1, width, label='Estimated Costs', color=green_shades[0])
        # Plot the second set of bars (Personal Expenses)
        rects2 = ax.bar(x + width/2, y2, width, label='Personal Expenses', color=green_shades[4])

        # Adding labels, title, and legend
        ax.set_ylabel('Amount', fontdict={'fontsize': 24, 'fontweight': 'medium'})
        ax.set_xlabel('Categories',  fontdict={'fontsize': 24, 'fontweight': 'medium'})

        #ax.set_title('Estimated Costs vs. Your Expenses')
        ax.set_xticks(x)
        ax.set_xticklabels(['Restaurants', 'Rent', 'Transport', 'Market', 'Utilities', 'Clothing', 'Leisure'])
        ax.legend(loc='center right',  bbox_to_anchor=(1, 0, 0.5, 1), fontsize=24, frameon=False)

        plot = st.pyplot(fig)
        self.view.render_bar_chart(plot)

    def plot_pie_chart(self):
        """
        Plot a pie chart of estimated expenses.
        """

        x = np.char.array(['Restaurants', 'Rent', 'Transport', 'Market', 'Utilities', 'Clothing', 'Leisure'])
        y = np.array([self.model.restaurant, self.model.rent, self.model.transport, 
            self.model.market, self.model.utilities, self.model.clothing, 
            self.model.leisure])
        y = np.nan_to_num(y, nan=0)
        print(y)
        percent = y / y.sum() * 100 
        percent = np.nan_to_num(percent, nan=0)

        fig, ax = plt.subplots(figsize=(15, 9))
        ax.margins(tight=True)

        labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(x, percent)]
        patches, texts = ax.pie(np.round(percent), labels=labels, colors=orange_shades, startangle=90, radius=1.2)

        #ax.set_title('Distribution of Expenses', fontsize=9)
        ax.legend(patches, labels, loc='center right', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16, frameon=False)
        ax.axis('equal')

        plot = st.pyplot(fig)
        self.view.render_pie_chart(plot)