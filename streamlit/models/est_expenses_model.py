import numpy as np
class EstExpensesModel:
    """
    Model class for calculating total estimated expenses.
    """
    ["restaurants", "markets", "leisure", "rent_per_month", "transport", "utilities", "clothing"]
    def __init__(self):
        """
        Initialize the EstExpensesModel.
        """
        self.budget = None
        self.restaurant = None
        self.market = None
        self.leisure = None
        self.rent = None
        self.transport = None
        self.utilities = None
        self.clothing = None
      

    def calculate_total_expenses(self, restaurant, market, leisure, rent,  transport, utilities, clothing):
        """
        Calculate the total estimated expenses.

        Args:
            rent (float): The amount spent on rent.
            transport (float): The amount spent on transportation.
            food (float): The amount spent on food.
            utilities (float): The amount spent on utilities.
            clothing (float): The amount spent on clothing.
            leisure (float): The amount spent on leisure activities.

        Returns:
            float: The total estimated expenses.
        """
        total_expenses = np.round(np.array([restaurant, market, leisure, rent,  transport, utilities, clothing]).sum(), 2)
        return total_expenses
