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
st.title("💳 Personal Budget Planner")

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

input_kwargs = {
    'format':'%g', 
    'min_value':0.0,
}

quantity_kwargs = {
    'format':'%d',
    'min_value':0, 
}

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
user_form.subheader("Monthly Income")

user_income = user_form.number_input('Current or Projected Income:', value=0.0, step=1000.0, **input_kwargs)

# Input Field For Rental Expenses
user_form.subheader("Monthly Rental Expenses")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_rent"]}</p>""", 
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
    rent_value = col2a.number_input('Rent Value', 
        value=totals["est_rent"], step=1000.00, **input_kwargs)

# Input Field For Market Expenses
user_form.subheader(f"""Monthly Market Expenses""")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_market"]}</p>""", 
    unsafe_allow_html=True
)

col1b, col2b = user_form.columns([2, 1], gap="large")

with col1b: 
    milk = col1b.number_input('Regular Milk, 1L',
        value=market_rec.get('Milk (regular), (1 liter)', 0.0), step=10.0, **input_kwargs)
    loaf = col1b.number_input('White Bread, Fresh Loaf', 
        value=market_rec.get('Loaf of Fresh White Bread (500g)', 0.0), step=10.0, **input_kwargs)
    eggs = col1b.number_input('A Dozen Regular Eggs', 
        value=market_rec.get('Eggs (regular) (12)', 0.0), step=10.0, **input_kwargs)
    water = col1b.number_input('Water, 1.5L bottle', 
        value=market_rec.get('Water (1.5 liter bottle)', 0.0), step=10.0, **input_kwargs)
    apples = col1b.number_input('Apples, 1kg', 
        value=market_rec.get('Apples (1kg)', 0.0), step=10.0, **input_kwargs)
    oranges = col1b.number_input('Oranges 1kg', 
        value=market_rec.get('Oranges (1kg)', 0.0), step=10.0, **input_kwargs)
    potato = col1b.number_input('Potato 1kg', 
        value=market_rec.get('Potato (1kg)', 0.0), step=10.0, **input_kwargs)
    lettuce = col1b.number_input('Lettuce, One Head', 
        value=market_rec.get('Lettuce (1 head)', 0.0), step=10.0, **input_kwargs)
    rice = col1b.number_input('Rice 1kh', 
        value=market_rec.get('Rice (white), (1kg)', 0.0), step=10.0, **input_kwargs)
    tomato = col1b.number_input('Tomato, 1kg', 
        value=market_rec.get('Tomato (1kg)', 0.0), step=10.0, **input_kwargs)
    banana = col1b.number_input('Banana, 1kg', 
        value=market_rec.get('Banana (1kg)', 0.0), step=10.0, **input_kwargs)
    onion = col1b.number_input('Onion, 1kg', 
        value=market_rec.get('Onion (1kg)', 0.0), step=10.0, **input_kwargs)
    cheese = col1b.number_input('Local Cheese, 1kg', 
        value=market_rec.get('Local Cheese (1kg)', 0.0), step=10.0, **input_kwargs)
    wine = col1b.number_input('Bottle of Wine, Mid-Range', 
        value=market_rec.get('Bottle of Wine (Mid-Range)', 0.0), step=10.0, **input_kwargs)
    chicken = col1b.number_input('Chicken Fillets, 1kg', 
        value=market_rec.get('Chicken Fillets (1kg)', 0.0), step=10.0, **input_kwargs)
    beef = col1b.number_input('Beef or Equivalent Red Meat, 1kg ', 
        value=market_rec.get('Beef Round (1kg) (or Equivalent Back Leg Red Meat)', 0.0), step=10.0, **input_kwargs)
    domestic_beer = col1b.number_input('Domestic Beer 500ml', 
        value=market_rec.get('Domestic Beer (0.5 liter bottle)', 0.0), step=10.0, **input_kwargs)
    import_beer = col1b.number_input('Imported Beer 330ml', 
        value=market_rec.get('Imported Beer (0.33 liter bottle)', 0.0), step=10.0, **input_kwargs)
    cigs = col1b.number_input('Cigarettes 20 Pack (Marlboro)', 
        value=market_rec.get('Cigarettes 20 Pack (Marlboro)', 0.0), step=10.0, **input_kwargs)

with col2b:
    milk_qty = col2b.number_input("Quantity", key='mlk', value=2, step=1, **quantity_kwargs)
    loaf_qty = col2b.number_input("Quantity", key='lwb', value=2, step=1, **quantity_kwargs)
    eggs_qty = col2b.number_input("Quantity", key='dre', value=2, step=1, **quantity_kwargs)
    water_qty = col2b.number_input("Quantity", key='wbb', value=2, step=1, **quantity_kwargs)
    apples_qty = col2b.number_input("Quantity", key='apk', value=2, step=1, **quantity_kwargs)
    oranges_qty = col2b.number_input("Quantity", key='ogk', value=2, step=1, **quantity_kwargs)
    potato_qty = col2b.number_input("Quantity", key='ptk', value=2, step=1, **quantity_kwargs)
    lettuce_qty = col2b.number_input("Quantity", key='lth', value=2, step=1, **quantity_kwargs)
    rice_qty = col2b.number_input("Quantity", key='wrk', value=2, step=1, **quantity_kwargs)
    tomato_qty = col2b.number_input("Quantity", key='tmk', value=2, step=1, **quantity_kwargs)
    banana_qty = col2b.number_input("Quantity", key='bnk', value=2, step=1, **quantity_kwargs)
    onion_qty = col2b.number_input("Quantity", key='nok', value=2, step=1, **quantity_kwargs)
    cheese_qty = col2b.number_input("Quantity", key='chk', value=2, step=1, **quantity_kwargs)
    wine_qty = col2b.number_input("Quantity", key='wbq', value=2, step=1, **quantity_kwargs)
    chicken_qty = col2b.number_input("Quantity", key='cfk', value=2, step=1, **quantity_kwargs)
    beef_qty = col2b.number_input("Quantity", key='bfk', value=2, step=1, **quantity_kwargs)
    domestic_qty = col2b.number_input("Quantity", key='dbf', value=2, step=1, **quantity_kwargs)
    import_qty = col2b.number_input("Quantity", key='ibf', value=2, step=1, **quantity_kwargs)
    cigs_qty = col2b.number_input("Quantity", key='c20', value=2, step=1, **quantity_kwargs)

market_total = np.round(np.array([
    milk * milk_qty, loaf * loaf_qty, eggs * eggs_qty, water * water_qty, 
    apples * apples_qty, oranges * oranges_qty, potato * potato_qty, lettuce * lettuce_qty,
    rice * rice_qty, tomato * tomato_qty, banana * banana_qty, onion * onion_qty, cheese * cheese_qty,
    wine * wine_qty, chicken *chicken_qty, beef * beef_qty, domestic_beer * domestic_qty, 
    import_beer * import_qty, cigs * cigs_qty]).sum(), 2)

# Input Field For Leisure Expenses
user_form.subheader(f"""Monthly Sports & Leisure Expenses""")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_leisure"]}</p>""", 
    unsafe_allow_html=True
)

fitness = user_form.number_input('Gym Membership, Monthly Fee', 
    value=leisure_rec.get('Fitness Club, Monthly Fee for 1 Adult', 0.0), step=100.0, **input_kwargs)


col1c, col2c = user_form.columns([2, 1], gap="large")

with col1c:
    sports = col1c.number_input('Sports Club, Weekly Fee', 
    value=leisure_rec.get('Tennis Court Rent (1 Hour on Weekend)', 0.0), step=100.0, **input_kwargs)
    movies = col1c.number_input('Cinema Theatre, 1 Seat', 
        value=leisure_rec.get('Cinema, International Release, 1 Seat', 0.0), step=100.0, **input_kwargs)

with col2c: 
    sports_freq = col2c.number_input("Visits Per Month", key='scv', value=1, step=1, **quantity_kwargs, max_value=4)
    movies_freq = col2c.number_input("Visits Per Month", key='cmv', value=1, step=1, **quantity_kwargs)

leisure_total = np.round(np.array([fitness, sports * sports_freq, movies * movies_freq]).sum(), 2)

# Input Field For Restaurant Expenses
user_form.subheader(f"""Monthly Restaurant Expenses""")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_restaurant"]}</p>""", 
    unsafe_allow_html=True
)

col1d, col2d = user_form.columns([2, 1], gap="large")

with col1d:
    one_meal = col1d.number_input('Inexpensive Restaurant Meal for One', 
        value=restaurant_rec.get('Meal, Inexpensive Restaurant', 0.0), step=100.0, **input_kwargs)
    duo_meal = col1d.number_input('Three Course Meal for Two at a Mid-range Restaurant', 
        value=restaurant_rec.get('Meal for 2 People, Mid-range Restaurant, Three-course', 0.0), step=100.0, **input_kwargs)
    combo = col1d.number_input('Fast Food Combo Meal', 
        value=restaurant_rec.get('McMeal at McDonalds (or Equivalent Combo Meal)', 0.0), step=50.0, **input_kwargs)
    fizzy_drink = col1d.number_input('Fizzy Drink 330ml', 
        value=restaurant_rec.get('Coke/Pepsi (0.33 liter bottle)', 0.0), step=10.0, **input_kwargs)
    bottled_water = col1d.number_input('Bottled Water 330ml', 
        value=restaurant_rec.get('Water (0.33 liter bottle)', 0.0), step=10.0, **input_kwargs)
    cappucino = col1d.number_input('Regular Cappuccino', 
        value=restaurant_rec.get('Cappuccino (regular)', 0.0), step=10.0, **input_kwargs)

with col2d:
    one_meal_freq = col2d.number_input("Visits Per Month", key='omf', value=1, step=1, **quantity_kwargs)
    duo_meal_freq = col2d.number_input("Visits Per Month", key='mf2', value=1, step=1, **quantity_kwargs)
    combo = col2d.number_input("Visits Per Month", key='ffc', value=1, step=1, **quantity_kwargs)
    fizzy_drink_qty = col2d.number_input("Purchases Per Month", key='fdf', value=1, step=1, **quantity_kwargs)
    bottled_water_qty = col2d.number_input("Purchases Per Month", key='bwf', value=1, step=1, **quantity_kwargs)
    cappucino_qty = col2d.number_input("Purchases Per Month", key='cpf', value=1, step=1, **quantity_kwargs)

restaurant_total = np.round(np.array([
    one_meal * one_meal_freq, duo_meal * duo_meal_freq, fizzy_drink * fizzy_drink_qty, 
    bottled_water * bottled_water_qty, cappucino * cappucino_qty]).sum(), 2)

user_form.subheader(f"""Monthly Transport Expenses""")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_transport"]}</p>""", 
    unsafe_allow_html=True
)

col1e, col2e = user_form.columns([2, 1], gap="large")

with col1e:
    one_way = col1e.number_input('One-Way Trip, Local Transport', 
        value=transport_rec.get('One-way Ticket (Local Transport)', 0.0), step=10.0, **input_kwargs)
    gasoline = col1e.number_input('Gasoline / Petrol, 1L', 
        value=transport_rec.get('Gasoline (1 liter)', 0.0), step=10.0, **input_kwargs)
    
with col2e:
    one_way_qty = col2e.number_input("Trips Per Month", key='owt', 
        value=0, **quantity_kwargs, step=1)
    gasoline_qty = col2e.number_input("Liters Per Month", key='gas', 
        value=0, **quantity_kwargs, step=1)

monthly_pass = user_form.number_input('Bus / Train, Monthly Pass', 
        value=transport_rec.get('Monthly Pass (Regular Price)', 0.0), step=10.0, **input_kwargs)

transport_total = np.round(np.array([one_way * one_way_qty, gasoline * gasoline_qty, monthly_pass]).sum(), 2)

user_form.subheader(f"""Monthly Utilities Expenses""")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_utilities"]}</p>""", 
    unsafe_allow_html=True
)

basics_utils = user_form.number_input('Basic Electricity, Water & Garbage', 
    value=utilities_rec.get('Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment', 0.0), step=100.0, **input_kwargs)
internet = user_form.number_input('Internet: 60 Mbps or More, Unlimited Data', 
    value=utilities_rec.get('Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)', 0.0), step=100.0, **input_kwargs)
mobile = user_form.number_input('Mobile Plan with Voice and Data 10GB+ ', 
    value=utilities_rec.get('Mobile Phone Monthly Plan with Calls and 10GB+ Data', 0.0), step=100.0, **input_kwargs)

utilities_total = np.round(np.array([basics_utils, internet, mobile]).sum(), 2)

user_form.subheader("Annual Clothing Expenses")

user_form.markdown(
    f"""<p style='text-align: left; font-size: 21px; font-weight: 400; margin-bottom: 5px;'>
    * Estimated average: {currency_symbol} {totals["est_clothing"]}</p>""", 
    unsafe_allow_html=True
)

col1g, col2g = user_form.columns([2, 1], gap="large")

with col1g:
    pants = col1g.number_input('Designer Jeans, 1 Pair', 
        value=clothing_rec.get('1 Pair of Jeans (Levis 501 Or Similar)', 0.0), step=100.0, **input_kwargs)
    tops = col1g.number_input('Top or Shirt (from Zara, H&M, etc...)', 
        value=clothing_rec.get('1 Summer Dress in a Chain Store (Zara, H&M, ...)', 0.0), step=100.0, **input_kwargs)
    running_shoes = col1g.number_input('Running Shoes or Sneakers', 
        value=clothing_rec.get('1 Pair of Nike Running Shoes (Mid-Range)', 0.0), step=100.0, **input_kwargs)
    formal_shoes = col1g.number_input('Formal Shoes', 
        value=clothing_rec.get( '1 Pair of Men Leather Business Shoes', 0.0), step=100.0, **input_kwargs)

with col2g:
    pants_qty = col2g.number_input("Purchases Per Year", key='djp', value=1, step=1, **quantity_kwargs)
    tops_qty = col2g.number_input("Purchases Per Year", key='cst', value=1, step=1, **quantity_kwargs)
    running_shoes_qty = col2g.number_input("Purchases Per Year", key='mrs', value=1, step=1, **quantity_kwargs)
    formal_shoes_qty = col2g.number_input("Purchases Per Year", key='fbs', value=1, step=1, **quantity_kwargs)

clothing_total = np.round(np.array(
    [pants * pants_qty, tops * tops_qty, 
    running_shoes * running_shoes_qty, formal_shoes * formal_shoes_qty]).sum() / 12, 2)

expenses_controller.model.restaurant = restaurant_total
expenses_controller.model.rent = rent_value
expenses_controller.model.transport = transport_total
expenses_controller.model.market = market_total
expenses_controller.model.utilities = utilities_total
expenses_controller.model.clothing = clothing_total
expenses_controller.model.leisure = leisure_total

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
expenses_controller.plot_side_side_bar(selected_city)

st.write(f"""    
<p style='font-size: 18px; margin-top: 10px;'>
    Distribution of Personal Expenses Across Cost Categories 
</p>""", unsafe_allow_html=True
)

# Render pie chart
expenses_controller.plot_pie_chart()
