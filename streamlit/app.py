import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from utils.utils import countries, country_currency
from controllers.est_expenses_controller import EstExpensesController
from controllers.cities_controller import CitiesController
from controllers.city_data_controller import CityDataController

# Initialize Expenses Controller
expenses_controller = EstExpensesController()

st.set_page_config(layout="centered")

# Header
st.markdown(
    f"<h1 style='text-align: center; font-size: 32px; font-weight: 700; margin-bottom: 32px;'>💳 Personal Budget Planner</h1>", 
    unsafe_allow_html=True
)




# Sidebar Selectboxes for Country and City
selected_country = st.sidebar.selectbox("Select Country:", options=countries)

# Get City Options From Selected Country
cities_model = CitiesController(selected_country)
selected_cities = sorted(cities_model.get_cities(selected_country))

# Get Selected Countrie's Currency Symbol
currency_symbol = country_currency[selected_country]

# Set Selected City
selected_city = st.sidebar.selectbox("Select City:", selected_cities)

# Get Cost of Living Data For Selected City
city_data_controller = CityDataController(selected_city)

# Calculate Estimated Monthly Costs for Expense Categories from City Data
totals = city_data_controller.calculate_averages()

# Retrieve Individual Item Costs Per Category based on Selected City Data 
records = city_data_controller.return_records()

restaurant_rec = records["restaurants"][0]
market_rec = records["markets"][0]
rent_rec = records["rent"][0]
transport_rec = records["transport"][0]
utilities_rec = records["utilities"][0]
leisure_rec = records["leisure"][0]
clothing_rec = records["clothing"][0]

print(market_rec)

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

# Input Field For Income
user_form.markdown(
        f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Income</h3>", 
        unsafe_allow_html=True
    )

user_income = user_form.number_input('Current or Projected Income:', format='%g', value=0, step=1000)

# Input Field For Rental Expenses
user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Rental Expenses</h3>", 
    unsafe_allow_html=True
)

col1a, col2a = user_form.columns([2, 1], gap="large")

with col1a:
    accomodation_type = col1a.selectbox("Select Accomodation Option:",
        options=[
            'Apartment, 1 bedroom in City Centre',
            'Apartment, 1 bedroom Outside of Centre'
        ]
    )


with col2a: 
    rent_value = col2a.number_input('Rent Value', format='%g', 
        value=totals["est_rent"], step=1000.00)

# Input Field For Market Expenses
user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Market Expenses</h3>", 
    unsafe_allow_html=True
)

col1b, col2b = user_form.columns([2, 1], gap="large")

with col1b: 
    milk_1l = col1b.number_input('Regular Milk, 1L', format='%g', 
        value=market_rec.get('Milk (regular), (1 liter)', 0), step=10.0)
    loaf_white_500g = col1b.number_input('White Bread, Fresh Loaf', format='%g', 
        value=market_rec.get('Loaf of Fresh White Bread (500g)', 0), step=10.0)
    eggs_dozen = col1b.number_input('A Dozen Regular Eggs', format='%g', 
        value=market_rec.get('Eggs (regular) (12)', 0), step=10.0)
    water_1500ml = col1b.number_input('Water, 1.5L bottle', format='%g', 
        value=market_rec.get('Water (1.5 liter bottle)', 0), step=10.0)
    apples_1kg = col1b.number_input('Apples, 1kg', format='%g', 
        value=market_rec.get('Apples (1kg)', 0), step=10.0)
    oranges_1kg = col1b.number_input('Oranges 1kg', format='%g', 
        value=market_rec.get('Oranges (1kg)', 0), step=10.0)
    potato_1kg = col1b.number_input('Potato 1kg', format='%g', 
        value=market_rec.get('Potato (1kg)', 0), step=10.0)
    lettuce_head = col1b.number_input('Lettuce, One Head', format='%g', 
        value=market_rec.get('Lettuce (1 head)', 0), step=10.0)
    white_rice_1kg = col1b.number_input('Rice 1kh', format='%g', 
        value=market_rec.get('Rice (white), (1kg)', 0), step=10.0)
    tomato_1kg = col1b.number_input('Tomato, 1kg', format='%g', 
        value=market_rec.get('Tomato (1kg)', 0), step=10.0)
    banana_1kg = col1b.number_input('Banana, 1kg', format='%g', 
        value=market_rec.get('Banana (1kg)', 0), step=10.0)
    onion_1kg = col1b.number_input('Onion, 1kg', format='%g', 
        value=market_rec.get('Onion (1kg)', 0), step=10.0)
    cheese_1kg = col1b.number_input('Local Cheese, 1kg', format='%g', 
        value=market_rec.get('Local Cheese (1kg)', 0), step=10.0)
    wine_bottle = col1b.number_input('Bottle of Wine, Mid-Range', format='%g', 
        value=market_rec.get('Bottle of Wine (Mid-Range)',0), step=10.0)
    chiken_1kg = col1b.number_input('Chicken Fillets, 1kg', format='%g', 
        value=market_rec.get('Chicken Fillets (1kg)', 0), step=10.0)
    beef_1kg = col1b.number_input('Beef or Equivalent Red Meat, 1kg ', format='%g', 
        value=market_rec.get('Beef Round (1kg) (or Equivalent Back Leg Red Meat)', 0), step=10.0)
    domestic_beer = col1b.number_input('Domestic Beer 500ml', format='%g', 
        value=market_rec.get('Domestic Beer (0.5 liter bottle)', 0), step=10.0)
    imported_beer = col1b.number_input('Imported Beer 330ml', format='%g', 
        value=market_rec.get('Imported Beer (0.33 liter bottle)', 0), step=10.0)
    cigs_20pack = col1b.number_input('Cigarettes 20 Pack (Marlboro)', format='%g', 
        value=market_rec.get('Cigarettes 20 Pack (Marlboro)', 0), step=10.0)

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
    cigs_20pack = col2b.number_input("Quantity", key='c20', format="%d", value=0, step=1)

# Input Field For Leisure Expenses
user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Sports & Leisure Expenses</h3>", 
    unsafe_allow_html=True
)

fitness_club = user_form.number_input('Gym Membership, Monthly Fee', format='%g', 
    value=leisure_rec.get('Fitness Club, Monthly Fee for 1 Adult', 0), step=100.0)


col1c, col2c = user_form.columns([2, 1], gap="large")

with col1c:
    sports_club = col1c.number_input('Sports Club, Weekly Fee', format='%g', 
    value=leisure_rec.get('Tennis Court Rent (1 Hour on Weekend)', 0), step=100.0)
    movies = col1c.number_input('Cinema Theatre, 1 Seat', format='%g', 
        value=leisure_rec.get('Cinema, International Release, 1 Seat', 0), step=100.0)

with col2c: 
    sports_club_freq = col2c.number_input("Visits Per Month", key='scv', format="%d", value=0, step=1, max_value=4)
    movies_freq = col2c.number_input("Visits Per Month", key='cmv', format="%d", value=0, step=1)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Restaurant Expenses</h3>", 
    unsafe_allow_html=True
)


col1d, col2d = user_form.columns([2, 1], gap="large")

with col1d:
    one_meal = col1d.number_input('Inexpensive Restaurant Meal for One', format='%g', 
        value=restaurant_rec.get('Meal, Inexpensive Restaurant', 0), step=100.0)
    meal_for_two = col1d.number_input('Three Course Meal for Two at a Mid-range Restaurant', format='%g', 
        value=restaurant_rec.get('Meal for 2 People, Mid-range Restaurant, Three-course', 0), step=100.0)
    fast_food_combo = col1d.number_input('Fast Food Combo Meal', format='%g', 
        value=restaurant_rec.get('McMeal at McDonalds (or Equivalent Combo Meal)', 0), step=50.0)
    fizzy_drink = col1d.number_input('Fizzy Drink 330ml', format='%g', 
        value=restaurant_rec.get('Coke/Pepsi (0.33 liter bottle)', 0), step=10.0)
    bottled_water = col1d.number_input('Bottled Water 330ml', format='%g', 
        value=restaurant_rec.get('Water (0.33 liter bottle)', 0), step=10.0)
    cappucino = col1d.number_input('Regular Cappuccino', format='%g', 
        value=restaurant_rec.get('Cappuccino (regular)', 0), step=10.0)

with col2d:
    one_meal_freq = col2d.number_input("Visits Per Month", key='omf', format="%d", value=0, step=1)
    meal_for_two_fred = col2d.number_input("Visits Per Month", key='mf2', format="%d", value=0, step=1)
    fast_food_combo = col2d.number_input("Visits Per Month", key='ffc', format='%d', value=0, step=1)
    fizzy_drink_qty = col2d.number_input("Purchases Per Month", key='fdf', format="%d", value=0, step=1)
    bottled_water_qty = col2d.number_input("Purchases Per Month", key='bwf', format="%d", value=0, step=1)
    cappucino_qty = col2d.number_input("Purchases Per Month", key='cpf', format="%d", value=0, step=1)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Transport Expenses</h3>", 
    unsafe_allow_html=True
)

col1e, col2e = user_form.columns([2, 1], gap="large")

with col1e:
    one_way = col1e.number_input('One-Way Trip, Local Transport', format='%g', 
        value=transport_rec.get('One-way Ticket (Local Transport)', 0), step=10.0)
    gasoline = col1e.number_input('Gasoline / Petrol, 1L', format='%g', 
        value=transport_rec.get('Gasoline (1 liter)', 0), step=10.0)
    
with col2e:
    one_way = col2e.number_input("Trips Per Month", key='owt', format="%d", 
        value=0, step=1)
    gasoline = col2e.number_input("Liters Per Month", key='gas', format="%d", 
        value=0, step=1)

monthly_pass = user_form.number_input('Bus / Train, Monthly Pass', format='%g', 
        value=transport_rec.get('Monthly Pass (Regular Price)', 0), step=10.0)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Monthly Utilities Expenses</h3>", 
    unsafe_allow_html=True
)

basics_utils = user_form.number_input('Basic Electricity, Water & Garbage', format='%g', 
    value=utilities_rec.get('Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment', 0), step=100.0)
internet = user_form.number_input('Internet: 60 Mbps or More, Unlimited Data', format='%g', 
    value=utilities_rec.get('Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)', 0), step=100.0)
mobile = user_form.number_input('Mobile Plan with Voice and Data 10GB+ ', format='%g', 
    value=utilities_rec.get('Mobile Phone Monthly Plan with Calls and 10GB+ Data', 0), step=100.0)

user_form.markdown(
    f"<h3 style='text-align: left; font-size: 18px; font-weight: 700; margin-bottom: 5px;'>Annual Clothing Expenses</h3>", 
    unsafe_allow_html=True
)

col1g, col2g = user_form.columns([2, 1], gap="large")

with col1g:
    pants = col1g.number_input('Designer Jeans, 1 Pair', format='%g', 
        value=clothing_rec.get('1 Pair of Jeans (Levis 501 Or Similar)', 0), step=100.0)
    tops = col1g.number_input('Top or Shirt (from Zara, H&M, etc...)', format='%g', 
        value=clothing_rec.get('1 Summer Dress in a Chain Store (Zara, H&M, ...)', 0), step=100.0)
    running_shoes = col1g.number_input('Running Shoes or Sneakers', format='%g', 
        value=clothing_rec.get('1 Pair of Nike Running Shoes (Mid-Range)', 0), step=100.0)
    formal_shoes = col1g.number_input('Formal Shoes', format='%g', 
        value=clothing_rec.get( '1 Pair of Men Leather Business Shoes', 0), step=100.0)

with col2g:
    pants_qty = col2g.number_input("Purchases Per Year", key='djp', format="%d", value=0, step=1)
    tops_qty = col2g.number_input("Purchases Per Year", key='cst', format="%d", value=0, step=1)
    running_shoes_qty = col2g.number_input("Purchases Per Year", key='mrs', format="%d", value=0, step=1)
    formal_shoes_qty = col2g.number_input("Purchases Per Year", key='fbs', format="%d", value=0, step=1)


expenses_controller.model.restaurant = 0
expenses_controller.model.rent = 0
expenses_controller.model.transport = 0
expenses_controller.model.market = 0
expenses_controller.model.utilities = 0
expenses_controller.model.clothing = 0
expenses_controller.model.leisure = 0 

user_form.form_submit_button(
    label="Calculate", 
    on_click=expenses_controller.update_expenses()
)

total = totals["est_total"]
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
col1h, col2h = st.columns([1, 1], gap="small")

with col1h:
    # Render user's expenses
    
    col1h.write(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 2px 0px; padding: 5px; width:100%;'>
            <p style='padding: 8px; font-size: 16px; font-weight: 600;'>Your Expenses:</p>
            <p style='padding: 8px;  padding-bottom: 0px;  font-size: 21px;'>
                {currency_symbol}    
                {expenses}
            </p>
        </div>
    """, unsafe_allow_html=True
)

with col2h:
    # Render user's income
    
    col2h.write(f"""
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
    <div style='border: 1px solid #e0e0e0; border-radius: 8px; margin: 2px 0px; padding: 5px; width:100%;'> 
        <p style='padding: 8px; font-size: 18px; font-weight: 600;'>Estimated Average Living Costs:</p>
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
