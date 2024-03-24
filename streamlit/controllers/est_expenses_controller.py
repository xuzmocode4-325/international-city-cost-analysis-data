from models.est_expenses_model import EstExpensesModel
from views.est_expenses_view import EstExpensesView
from controllers.city_data_controller import CityDataController

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

        horizontal_bar_chart_data = {
            'Avg. Rent': city_averages['Avg. Rent'],
            'Avg. Transport': city_averages['Avg. Transport'],
            'Avg. Market': city_averages['Avg. Market'],
            'Avg. Utilities': city_averages['Avg. Utilities'],
            'Avg. Clothing': city_averages['Avg. Clothing'],
            'Avg. Leisure': city_averages['Avg. Leisure'],
            'Rent': self.model.rent,
            'Transport': self.model.transport,
            'Market': self.model.food,
            'Utilities': self.model.utilities,
            'Clothing': self.model.clothing,
            'Leisure': self.model.leisure 
        }
        
        self.view.render_horizontal_bar_chart(horizontal_bar_chart_data)

    def plot_pie_chart(self):
        """
        Plot a pie chart of estimated expenses.
        """
        pie_chart_data = {
            'Rent': self.model.rent,
            'Transport': self.model.transport,
            'Market': self.model.food,
            'Utilities': self.model.utilities,
            'Clothing': self.model.clothing,
            'Leisure': self.model.leisure
        }
        self.view.render_pie_chart(pie_chart_data)
