import numpy as np
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
            self.model.rent, self.model.transport, self.model.food, self.model.utilities,
            self.model.clothing, self.model.leisure
        )
        self.expenses = total_expenses

    def update_expenses(self):
        """
        Update the estimated expenses.
        """
        self.calculate_estimated_expenses()

    def plot_side_side_hbar(self, city):
        """
        Plot a side-by-side horizontal bar chart of estimated expenses.

        Args:
            city (str): The name of the city to plot expenses for.
        """
        city_data_controller = CityDataController(city)
        city_averages = city_data_controller.calculate_averages()

        # Extracting y1 and y2 data
        y1 = [city_averages['Avg. Rent'], city_averages['Avg. Transport'],
              city_averages['Avg. Market'], city_averages['Avg. Utilities'],
              city_averages['Avg. Clothing'], city_averages['Avg. Leisure']]
        y2 = [self.model.rent, self.model.transport, self.model.food,
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
        rects2 = ax.bar(x + width/2, y2, width, label='Personal Expenses', color=green_shades[3])

        # Adding labels, title, and legend
        ax.set_ylabel('Amount', fontdict={'fontsize': 24, 'fontweight': 'medium'})
        ax.set_xlabel('Categories',  fontdict={'fontsize': 24, 'fontweight': 'medium'})

        #ax.set_title('Estimated Costs vs. Your Expenses')
        ax.set_xticks(x)
        ax.set_xticklabels(['Rent', 'Transport', 'Food',
                            'Utilities', 'Clothing', 'Leisure'])
        ax.legend(loc='center right',  bbox_to_anchor=(1, 0, 0.5, 1), fontsize=24, frameon=False)

        plot = st.pyplot(fig)
        self.view.render_horizontal_bar_chart(plot)

    def plot_pie_chart(self):
        """
        Plot a pie chart of estimated expenses.
        """

        x = np.char.array(['Rent', 'Transport', 'Food', 'Utilities', 'Clothing', 'Leisure'])
        y = np.array([self.model.rent, self.model.transport, self.model.food, self.model.utilities, self.model.clothing, self.model.leisure])

        percent = 100. * y / y.sum()

        fig, ax = plt.subplots(figsize=(15, 9))
        ax.margins(tight=True)

        patches, texts = ax.pie(y, colors=orange_shades, startangle=90, radius=1.2)

        labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(x, percent)]

        #ax.set_title('Distribution of Expenses', fontsize=9)
        ax.legend(patches, labels, loc='center right', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16, frameon=False)

        plot = st.pyplot(fig)
        self.view.render_pie_chart(plot)
