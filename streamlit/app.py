import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from controllers.est_expenses_controller import EstExpensesController
from utils.utils import country_cities_mapping

st.set_page_config(layout="wide")

# Header
st.markdown(
    f"<p style='text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 32px;'>Cost of Living Analysis</p>", 
    unsafe_allow_html=True
)

# Initialize controller and get sorted countries
expenses_controller = EstExpensesController()
sorted_countries = sorted(country_cities_mapping.keys())

# Sidebar selectboxes for country and city
selected_country = st.sidebar.selectbox(
    "Select Country:",
    sorted_countries
)

if selected_country:
    selected_cities = country_cities_mapping.get(selected_country, [])
    selected_city = st.sidebar.selectbox("Select City:", selected_cities)
else:
    st.sidebar.text("Please select a country.")

# Define layout columns
col1, col2 = st.columns([0.4, 0.6], gap="large")

with col1:
    # Render average cost of living and sliders for expenses
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Average Cost of Living in {selected_city}</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 40px;'>R5000</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sliders for each expense category
    expenses_controller.rent = st.slider('Rent', 0, 20000, step=100, value=expenses_controller.rent)
    expenses_controller.transport = st.slider('Transport', 0, 5000, step=50, value=expenses_controller.transport)
    expenses_controller.food = st.slider('Food', 0, 5000, step=50, value=expenses_controller.food)
    expenses_controller.utilities = st.slider('Utilities', 0, 5000, step=50, value=expenses_controller.utilities)
    expenses_controller.clothing = st.slider('Clothing', 0, 5000, step=50, value=expenses_controller.clothing)
    expenses_controller.leisure = st.slider('Leisure', 0, 5000, step=50, value=expenses_controller.leisure)
    
    expenses_controller.update_expenses()  # Update the budget after sliders change

with col2:
    # Render user's expenses
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Expenses:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 40px;'>R{expenses_controller.expenses}</p>
        </div>
    """, unsafe_allow_html=True)
   
# Define layout columns for visualizations
col3, col4 = st.columns([0.4, 0.6], gap="large")

with col3:
    # Render side-by-side horizontal bar chart
    expenses_controller.plot_side_side_hbar()

with col4:
    # Render pie chart
    expenses_controller.plot_pie_chart()
