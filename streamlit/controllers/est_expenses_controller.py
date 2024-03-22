from models.est_expenses_model import EstExpensesModel
from views.est_expenses_view import EstExpensesView

class EstExpensesController:
    def __init__(self):
        self.model = EstExpensesModel()
        self.view = EstExpensesView()
        self.budget = 5000
        self.rent = 4000
        self.transport = 500
        self.food = 500
        self.utilities = 500
        self.clothing = 500
        self.leisure = 500
        self.calculate_estimated_expenses() 

    def calculate_estimated_expenses(self):
        total_expenses = self.model.calculate_total_expenses(self.rent, self.transport, self.food, self.utilities, self.clothing, self.leisure)
        self.expenses = total_expenses

    def update_expenses(self):
        self.calculate_estimated_expenses()

    def plot_side_side_hbar(self):
        # Dummy data for visualization (replace with actual data)
        horizontal_bar_chart_data = {
            'Rent': self.rent,
            'Transport': self.transport,
            'Food': self.food,
            'Utilities': self.utilities,
            'Clothing': self.clothing,
            'Leasuire': self.leisure
        }

        self.view.render_horizontal_bar_chart(horizontal_bar_chart_data)

    def plot_pie_chart(self):
        # Dummy data for visualization (replace with actual data)
        pie_chart_data = {
            'Rent': self.rent,
            'Transport': self.transport,
            'Food': self.food,
            'Utilities': self.utilities,
            'Clothing': self.clothing,
            'Leasuire': self.leisure
        }
        self.view.render_pie_chart(pie_chart_data)
