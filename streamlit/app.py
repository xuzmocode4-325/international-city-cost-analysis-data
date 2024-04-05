import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from utils.utils import countries, country_currency
from controllers.est_expenses_controller import EstExpensesController
from controllers.cities_controller import CitiesController
from controllers.city_data_controller import CityDataController

st.set_page_config(layout="centered")

# Header
st.markdown(
    f"<h1 style='text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 32px;'>💳 Personal Budget Planner</h1>", 
    unsafe_allow_html=True
)

# Initialize controller
expenses_controller = EstExpensesController()

# Sidebar selectboxes for country and city
selected_country = st.sidebar.selectbox("Select Country:", options=countries)

cities_model = CitiesController(selected_country)
selected_cities = sorted(cities_model.get_cities(selected_country))
currency_symbol = country_currency[selected_country]

selected_city = st.sidebar.selectbox("Select City:", selected_cities)


city_data_controller = CityDataController(selected_city)
totals = city_data_controller.calculate_averages()

st.markdown(
    f"""<p style='text-align: left; font-size: 24px; font-weight: 400; margin: 5px;'>
    Thinking of relocating cities but not sure if you will be able to afford the cost of living expenses? 
    Input your income and expenses to get a personal budget evaluation.
    </p>""", 
    unsafe_allow_html=True
)


user_form = st.form("user form")

# Input field for income

user_form.markdown(
        f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Income</h3>", 
        unsafe_allow_html=True
    )

user_income = user_form.number_input('Current or Projected Income:', format='%g', value=0)

# Input field for Expenses

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Expenses</h3>", 
    unsafe_allow_html=True
)


col1, col2 = user_form.columns([1, 1], gap="large")

with col1:

# Input fields for each expense category 
    
    expenses_controller.model.rent = col1.number_input('Rent:', format='%g', value=totals["Avg. Rent"])
    expenses_controller.model.transport = col1.number_input('Transport:', format='%g', value=totals["Avg. Transport"])
    expenses_controller.model.food = col1.number_input('Food:', format='%g', value=totals["Avg. Market"])

with col2:
    expenses_controller.model.utilities = col2.number_input('Utilities:', format='%g', value=totals["Avg. Utilities"])
    expenses_controller.model.clothing = col2.number_input('Clothing:', format='%g', value=totals["Avg. Clothing"])
    expenses_controller.model.leisure = col2.number_input('Leisure:', format='%g', value=totals["Avg. Leisure"])

user_form.form_submit_button(
    label="Calculate", 
    on_click=expenses_controller.update_expenses()
)

total = totals['Avg. Total']
income = user_income 
expenses = expenses_controller.expenses

st.write(f"""    
<p style='font-size: 24px;'>
    Analysis for {selected_city}, {selected_country}
</p>""", unsafe_allow_html=True
)

if (income > expenses):
    st.success('You are managing your finances well!', icon='🤑')
elif (income < expenses): 
    st.error('You need to cut out some expenses!', icon='😩')
elif income == expenses:
    st.warning('You are at risk of financial mismanagment', icon='😑')

if (expenses < total):
    st.info(f'Your total spend is below the estimated cost-of-living for {selected_city}.', icon='🧮')
elif (expenses > total): 
    st.info(f'Your total is above the estimated cost-of-living for {selected_city}.', icon='🧮')



# Define layout columns
col1, col2, col3 = st.columns([1, 1, 1], gap="small")

with col1:
    # Render average cost of living and input fields for expenses
    
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 2px 0px; padding: 5px; width:100%;'> 
            <p style='padding: 8px; font-size: 18px; font-weight: 600;'>Estimated Costs:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 21px;'>
                {currency_symbol}    
                {total}
            </p>
        </div>
    """, unsafe_allow_html=True
)


with col2:
    # Render user's expenses
    
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 2px 0px; padding: 5px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Expenses:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 21px;'>
                {currency_symbol}    
                {expenses}
            </p>
        </div>
    """, unsafe_allow_html=True
)

with col3:
    # Render user's income
    
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 2px 0px; padding: 5px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Income:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 21px;'>  
                {currency_symbol}    
                {income}
            </p>
        </div>
    """, unsafe_allow_html=True
)

st.write(f"""    
<p style='font-size: 18px; margin-top: 10px;'>
    Estimated Costs vs Personal Expenses
</p>""", unsafe_allow_html=True
)

# Render side-by-side horizontal bar chart
expenses_controller.plot_side_side_hbar(selected_city)

st.write(f"""    
<p style='font-size: 18px; margin-top: 10px;'>
    Distribution of Personal Expenses Across Cost Categories 
</p>""", unsafe_allow_html=True
)

# Render pie chart
expenses_controller.plot_pie_chart()
