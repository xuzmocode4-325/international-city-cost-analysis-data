import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from controllers.est_expenses_controller import EstExpensesController
from utils.utils import country_cities_mapping


st.set_page_config(layout="wide")

st.markdown(
    f"<p style='text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 32px;'>Cost of Living Analysis</p>", 
    unsafe_allow_html=True
)

expenses_controller = EstExpensesController()
sorted_countries = sorted(country_cities_mapping.keys())

#Sidebar selectboxes

selected_country = st.sidebar.selectbox(
    "Select Country:",
    sorted_countries
)

if selected_country:
    selected_cities = country_cities_mapping.get(selected_country, [])
    selected_city = st.sidebar.selectbox("Select City:", selected_cities)
else:
    st.sidebar.text("Please select a country.")


col1, col2 = st.columns([0.4, 0.6], gap="large")

with col1:
    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Average Cost of Living in {selected_city}</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 40px;'>R5000</p>
        </div>
    """, unsafe_allow_html=True)
    
    expenses_controller.rent = st.slider('Rent', 0, 20000, step=100, value=expenses_controller.rent)
    expenses_controller.transport = st.slider('Transport', 0, 5000, step=50, value=expenses_controller.transport)
    expenses_controller.food = st.slider('Food', 0, 5000, step=50, value=expenses_controller.food)
    expenses_controller.utilities = st.slider('Utilities', 0, 5000, step=50, value=expenses_controller.utilities)
    expenses_controller.clothing = st.slider('Clothing', 0, 5000, step=50, value=expenses_controller.clothing)
    expenses_controller.leisure = st.slider('Leisure', 0, 5000, step=50, value=expenses_controller.leisure)
    
    expenses_controller.update_expenses()  # Update the budget after sliders change


with col2:

    st.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Expenses:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 40px;'>R{expenses_controller.expenses}</p>
        </div>
    """, unsafe_allow_html=True)
   
col3, col4 = st.columns([0.4, 0.6], gap="large")

with col3:
    expenses_controller.plot_side_side_hbar()
with col4:
    expenses_controller.plot_pie_chart()
    # st.markdown("""
    #     <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%; height:290px;'>
    #         Your plot goes here.
    #     </div>
    # """, unsafe_allow_html=True)
        
    # st.markdown("""
    #     <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 10px; padding: 10px; width:100%; height:290px;'>
    #         Your plot goes here.
    #     </div>
    # """, unsafe_allow_html=True)
