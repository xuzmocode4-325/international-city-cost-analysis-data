class EstExpensesModel:
    def __init__(self):
        pass
    
    def calculate_total_expenses(self, rent, transport, food, utilities, clothing, leisure):
        total_expenses = rent + transport + food + utilities + clothing + leisure 
        return total_expenses
