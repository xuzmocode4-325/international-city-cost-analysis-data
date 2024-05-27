import numpy as np
class EstExpensesModel:
    """
    Model class for calculating total estimated expenses.
    """
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
            restaurant (float): The amount spent on restaurant outings.
            transport (float): The amount spent on transportation.
            market (float): The amount spent on groceries.
            utilities (float): The amount spent on utilities.
            clothing (float): The amount spent on clothing.
            leisure (float): The amount spent on leisure activities.

        Returns:
            float: The total estimated expenses.
        """
        totals_array = np.array([restaurant, market, leisure, rent,  transport, utilities, clothing])
        totals_cleaned = totals_array[np.isnan(totals_array)] = 0
        total_expenses = np.round(totals_cleaned.sum(), 2)
        return total_expenses
