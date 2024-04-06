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
    f"""<p style='text-align: left; font-size: 18px; font-weight: 400; margin: 20px 0;'>
    Thinking of relocating cities? Want to be sure that you will be able to afford the cost of living expenses? 
    This is the app for you! 
    <br><br>
    Get accurate estimates on common expenses. 
    Simply input your income and expenses data in the form below for budget recommendations.  <br>
    </p>""", 
    unsafe_allow_html=True
)


user_form = st.form("user form")

# Input field for income

user_form.markdown(
        f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Income</h3>", 
        unsafe_allow_html=True
    )

user_income = user_form.number_input('Current or Projected Income:', format='%g', value=0, step=1000)

# Input field for Expenses

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Rental Expenses</h3>", 
    unsafe_allow_html=True
)

col1a, col2a = user_form.columns([2, 1], gap="large")

with col1a:
    accomodation_type = col1a.selectbox("Select Accomodation Option:",
        options=[
            'Apartment in City Centre, 1 bedroom ',
            'Apartment Outside of Centre, 1 bedroom'
        ]
    )

with col2a: 
    rent_value = col2a.number_input('Rent Value', format='%g', value=0, step=20)

    
user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Market Expenses</h3>", 
    unsafe_allow_html=True
)

col1b, col2b = user_form.columns([2, 1], gap="large")

with col1b: 
    milk_1l = col1b.number_input('Regular Milk, 1L', format='%g', value=0, step=20)
    loaf_white_500g = col1b.number_input('White Bread, Fresh Loaf', format='%g', value=0, step=20)
    eggs_dozen = col1b.number_input('A Dozen Regular Eggs', format='%g', value=0, step=20)
    water_1500ml = col1b.number_input('Water, 1.5L bottle', format='%g', value=0, step=20)
    apples_1kg = col1b.number_input('Apples, 1kg', format='%g', value=0, step=20)
    oranges_1kg = col1b.number_input('Oranges 1kg', format='%g', value=0, step=20)
    potato_1kg = col1b.number_input('Potato 1kg', format='%g', value=0, step=20)
    lettuce_head = col1b.number_input('Lettuce, One Head', format='%g', value=0, step=20)
    white_rice_1kg = col1b.number_input('Rice 1kh', format='%g', value=0, step=20)
    tomato_1kg = col1b.number_input('Tomato, 1kg', format='%g', value=0, step=20)
    banana_1kg = col1b.number_input('Banana, 1kg', format='%g', value=0, step=20)
    onion_1kg = col1b.number_input('Onion, 1kg', format='%g', value=0, step=20)
    cheese_1kg = col1b.number_input('Local Cheese, 1kg', format='%g', value=0, step=20)
    wine_bottle = col1b.number_input('Bottle of Wine, Mid-Range', format='%g', value=0, step=20)
    chiken_1kg = col1b.number_input('Chicken Fillets, 1kg', format='%g', value=0, step=20)
    beef_1kg = col1b.number_input('Beef or Equivalent Red Meat, 1kg ', format='%g', value=0, step=20)
    domestic_beer = col1b.number_input('Domestic Beer 500ml', format='%g', value=0, step=20)
    imported_beer = col1b.number_input('Imported Beer 330ml', format='%g', value=0, step=20)
    fizzy_drink = col1b.number_input('Fizzy Drink 330ml', format='%g', value=0, step=20)
    bottled_water = col1b.number_input('Bottled Water 330ml', format='%g', value=0, step=20)
    cappucino = col1b.number_input('Regular Cappuccino', format='%g', value=0, step=20)
    cigs_20pack = col1b.number_input('Cigarettes 20 Pack (Marlboro)', format='%g', value=0, step=20)

with col2b:
    milk_1l_qty = col2b.number_input("Quantity", key='mlk', format="%d", value=0, step=1)
    loaf_white_500g_qty = col2b.number_input("Quantity", key='lwb', format="%d", value=0, step=1)
    eggs_dozen_qty = col2b.number_input("Quantity", key='dre', format="%d", value=0, step=1)
    water_1500ml_qty = col2b.number_input("Quantity", key='wbb', format="%d", value=0, step=1)
    apples_1kg_qty = col2b.number_input("Quantity", key='apk', format="%d", value=0, step=1)
    oranges_1kg_qty = col2b.number_input("Quantity", key='ogk', format="%d", value=0, step=1)
    potato_1kg_qty = col2b.number_input("Quantity", key='ptk', format="%d", value=0, step=1)
    lettuce_head_qty = col2b.number_input("Quantity", key='lth', format="%d", value=0, step=1)
    white_rice_1kg_qty = col2b.number_input("Quantity", key='wrk', format="%d", value=0, step=1)
    tomato_1kg_qty = col2b.number_input("Quantity", key='tmk', format="%d", value=0, step=1)
    banana_1kg_qty = col2b.number_input("Quantity", key='bnk', format="%d", value=0, step=1)
    onion_1kg_qty = col2b.number_input("Quantity", key='nok', format="%d", value=0, step=1)
    cheese_1kg_qty = col2b.number_input("Quantity", key='chk', format="%d", value=0, step=1)
    wine_bottle_qty = col2b.number_input("Quantity", key='wbq', format="%d", value=0, step=1)
    chiken_1kg_qty = col2b.number_input("Quantity", key='cfk', format="%d", value=0, step=1)
    beef_1kg_qty = col2b.number_input("Quantity", key='bfk', format="%d", value=0, step=1)
    domestic_beer_qty = col2b.number_input("Quantity", key='dbf', format="%d", value=0, step=1)
    imported_beer_qty = col2b.number_input("Quantity", key='ibf', format="%d", value=0, step=1)
    fizzy_drink_qty = col2b.number_input("Quantity", key='fdf', format="%d", value=0, step=1)
    bottled_water_qty = col2b.number_input("Quantity", key='bwf', format="%d", value=0, step=1)
    cappucino_qty = col2b.number_input("Quantity", key='cpf', format="%d", value=0, step=1)
    cigs_20pack = col2b.number_input("Quantity", key='c20', format="%d", value=0, step=1)


user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Sports & Leisure Expenses</h3>", 
    unsafe_allow_html=True
)

fitness_club = user_form.number_input('Gym Membership, Monthly Fee', format='%g', value=0, step=100)
sports_club = user_form.number_input('Sports Club, Monthly Fee', format='%g', value=0, step=100)
movies = user_form.number_input('Cinema Theatre, 1 Seat', format='%g', value=0, step=100)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Restaurant Expenses</h3>", 
    unsafe_allow_html=True
)


col1d, col2d = user_form.columns([2, 1], gap="large")

with col1d:
    one_meal = col1d.number_input('Inexpensive Restaurant Meal for One', format='%g', value=0, step=100)
    meal_for_two = col1d.number_input('Three Course Meal for Two at a Mid-range Restaurant', format='%g', value=0, step=100)
    fast_food_combo = col1d.number_input('Fast Food Combo Meal', format='%g', value=0, step=50)
   
with col2d:
    one_meal_freq = col2d.number_input("Visits Per Month", key='omf', format="%d", value=0, step=1)
    meal_for_two_fred = col2d.number_input("Visits Per Month", key='mf2', format="%d", value=0, step=1)
    fast_food_combo = col2d.number_input("Visits Per Month", key='ffc', format='%d', value=0, step=1)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Transport Expenses</h3>", 
    unsafe_allow_html=True
)

col1e, col2e = user_form.columns([2, 1], gap="large")

with col1e:

    one_way = col1e.number_input('One-Way Trip, Local Transport', format='%g', value=0, step=10)
    gasoline = col1e.number_input('Gasoline / Petrol, 1L', format='%g', value=0, step=10)
    
with col2e:
    one_way = col2e.number_input("Trips Per Month", key='owt', format="%d", value=0, step=1)
    gasoline = col2e.number_input("Liters Per Month", key='gas', format="%d", value=0, step=1)

monthly_pass = user_form.number_input('Monthly Pass', format='%g', value=0, step=10)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Utilities Expenses</h3>", 
    unsafe_allow_html=True
)

basics_utils = user_form.number_input('Basic Electricity, Water & Garbage) ', format='%g', value=0, step=100)
internet = user_form.number_input('Internet: 60 Mbps or More, Unlimited Data', format='%g', value=0, step=100)
mobile = user_form.number_input('Mobile Plan with Voice and Data 10GB+ ', format='%g', value=0, step=100)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Annual Clothing Expenses</h3>", 
    unsafe_allow_html=True
)

col1g, col2g = user_form.columns([2, 1], gap="large")

with col1g:
    pants = col1g.number_input('Designer Jeans, 1 Pair', format='%g', value=0, step=100)
    tops = col1g.number_input('Top,  (from Zara, H&M, etc...)', format='%g', value=0, step=100)
    running_shoes = col1g.number_input('Mid-Range Running Shoes', format='%g', value=0, step=100)
    formal_shoes = col1g.number_input('Formal Shoes', format='%g', value=0, step=100)

with col2g:
    pants_qty = col2g.number_input("Purchases Per Year", key='djp', format="%d", value=0, step=1)
    tops_qty = col2g.number_input("Purchases Per Year", key='cst', format="%d", value=0, step=1)
    running_shoes_qty = col2g.number_input("Purchases Per Year", key='mrs', format="%d", value=0, step=1)
    formal_shoes_qty = col2g.number_input("Purchases Per Year", key='fbs', format="%d", value=0, step=1)


#expenses_controller.model.rent = col1.number_input('Rent:', format='%g', value=totals["Avg. Rent"])
#expenses_controller.model.rent = col1.number_input('Restaurants:', format='%g', value=totals["Avg. Rent"])
#expenses_controller.model.transport = col1.number_input('Transport:', format='%g', value=totals["Avg. Transport"])
#expenses_controller.model.food = col1.number_input('Market:', format='%g', value=totals["Avg. Market"])
#expenses_controller.model.utilities = col2.number_input('Utilities:', format='%g', value=totals["Avg. Utilities"])
#expenses_controller.model.clothing = col2.number_input('Clothing:', format='%g', value=totals["Avg. Clothing"])
#expenses_controller.model.leisure = col2.number_input('Leisure:', format='%g', value=totals["Avg. Leisure"])

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
col1, col2 = st.columns([1, 1], gap="small")

with col1:
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

with col2:
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
