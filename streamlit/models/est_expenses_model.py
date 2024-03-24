class EstExpensesModel:
    """
    Model class for calculating total estimated expenses.
    """

    def __init__(self):
        """
        Initialize the EstExpensesModel.
        """
        self.budget = None
        self.rent = None
        self.transport = None
        self.food = None
        self.utilities = None
        self.clothing = None
        self.leisure = None

    def calculate_total_expenses(self, rent, transport, food, utilities, clothing, leisure):
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
        total_expenses = rent + transport + food + utilities + clothing + leisure
        return total_expenses
