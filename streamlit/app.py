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

# Test

city_data_controller = CityDataController(selected_city)
totals = city_data_controller.calculate_averages()

# 

st.write(f"""    
    <p style='font-size: 24px;'>
        Analysis for {selected_city}, {selected_country}
    </p>""", unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Inputs", "Estimates Vs. Expenses", "Expense Distribution"])

with tab1:

    # Input field for income
    st.markdown(
        f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Income</h3>", 
        unsafe_allow_html=True
    )
    user_income = st.number_input('Current or Desired Income:', format='%g', value=0)

    # Input field for income

    st.markdown(
        f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Expenses</h3>", 
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

    # Input fields for each expense category 
        
        expenses_controller.model.rent = st.number_input('Rent:', format='%g', value=totals["Avg. Rent"])
        expenses_controller.model.transport = st.number_input('Transport:', format='%g', value=totals["Avg. Transport"])
        expenses_controller.model.food = st.number_input('Food:', format='%g', value=totals["Avg. Market"])

    with col2:
        expenses_controller.model.utilities = st.number_input('Utilities:', format='%g', value=totals["Avg. Utilities"])
        expenses_controller.model.clothing = st.number_input('Clothing:', format='%g', value=totals["Avg. Clothing"])
        expenses_controller.model.leisure = st.number_input('Leisure:', format='%g', value=totals["Avg. Leisure"])

    st.button(
        label="Calculate", 
        key=None, 
        help=None, 
        on_click=expenses_controller.update_expenses()
    )
    
    income_formatted = '{:,.2f}'.format(user_income)
    expenses_formatted = '{:,.2f}'.format(expenses_controller.expenses)

    # Check budget status
    if income_formatted > expenses_controller.expenses:
        st.success('You are below budget! 🤑')
    elif expenses_formatted < expenses_controller.expenses:
        st.error('You are over budget! 😩')
    else:
        st.warning('Your expenses exactly equal your income 😑')

    # Define layout columns
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")

    with col1:
        # Render average cost of living and input fields for expenses
        
        st.write(f"""
            <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 5px 0px; padding: 10px; width:100%;'> 
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
            <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 5px 0px; padding: 10px; width:100%;'>
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
            <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 5px 0px; padding: 10px; width:100%;'>
                <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Income:</p>
                <p style='padding: 8px;  padding-bottom: 0px;  font-size: 21px;'>  
                    {currency_symbol}    
                    {income}
                </p>
            </div>
        """, unsafe_allow_html=True
    )
        
    

with tab2:
    st.write(f"""    
    <p style='font-size: 24px;'>
        Analysis for {selected_city}, {selected_country}
    </p>""", unsafe_allow_html=True
    )
    # Render side-by-side horizontal bar chart
    expenses_controller.plot_side_side_hbar(selected_city)

with tab3:
    st.write(f"""    
    <p style='font-size: 24px;'>
        Analysis for {selected_city}, {selected_country}
    </p>""", unsafe_allow_html=True
    )
    # Render pie chart
    expenses_controller.plot_pie_chart()
