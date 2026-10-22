import streamlit as st

# ==========================================
# 1. YOUR CORE FINANCIAL ENGINE
# ==========================================

def calculate_buying_cost(original_home_price, down_payment_pct, tax_rate, annual_interest_rate, loan_duration_years, target_year, appreciation_rate):
    down_payment = original_home_price * (down_payment_pct / 100.0)
    loan_amount = original_home_price - down_payment
    monthly_interest_rate = annual_interest_rate / 12.0
    total_payments = loan_duration_years * 12

    if monthly_interest_rate > 0:
        monthly_mortgage = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / (((1 + monthly_interest_rate)**total_payments) - 1)
    else:
        monthly_mortgage = loan_amount / total_payments

    remaining_balance = loan_amount
    for month in range(1, (target_year * 12) + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_mortgage - interest_payment
        remaining_balance -= principal_payment
        if remaining_balance < 0:
            remaining_balance = 0

    future_home_value = original_home_price * ((1 + appreciation_rate) ** target_year)
    equity = future_home_value - remaining_balance

    total_mortgage_paid = monthly_mortgage * 12 * target_year
    total_taxes_paid = (original_home_price * tax_rate) * target_year
    total_buyer_out_of_pocket = down_payment + total_mortgage_paid + total_taxes_paid

    return {
        "home_value": future_home_value,
        "remaining_loan": remaining_balance,
        "buyer_equity": equity,
        "total_out_of_pocket": total_buyer_out_of_pocket
    }

def calculate_renting_costs(initial_monthly_rent, rent_inflation_rate, target_year):
    total_rent_paid = 0
    current_rent = initial_monthly_rent
    for year in range(1, target_year + 1):
        total_rent_paid += current_rent * 12
        current_rent *= (1 + rent_inflation_rate)
    return total_rent_paid

def calculate_stock_growth(initial_investment, monthly_contribution, annual_return_rate, target_year):
    monthly_rate = annual_return_rate / 12.0
    total_months = target_year * 12
    portfolio_value = initial_investment

    for month in range(total_months):
        portfolio_value = (portfolio_value + monthly_contribution) * (1 + monthly_rate)

    return portfolio_value

def run_buy_vs_rent_analysis(original_home_price, down_payment_pct, tax_rate, annual_interest_rate, loan_duration_years, appreciation_rate, initial_monthly_rent, rent_inflation_rate, stock_return_rate, target_year):
    buying_data = calculate_buying_cost(original_home_price, down_payment_pct, tax_rate, annual_interest_rate, loan_duration_years, target_year, appreciation_rate)
    total_rent_paid = calculate_renting_costs(initial_monthly_rent, rent_inflation_rate, target_year)

    down_payment_dollars = original_home_price * (down_payment_pct / 100.0)
    monthly_mortgage = (original_home_price - down_payment_dollars) * ((annual_interest_rate / 12) * (1 + (annual_interest_rate / 12))**(loan_duration_years*12)) / (((1 + (annual_interest_rate / 12))**(loan_duration_years*12)) - 1)
    monthly_property_tax = (original_home_price * tax_rate) / 12.0
    total_monthly_buyer_cost = monthly_mortgage + monthly_property_tax

    initial_monthly_savings = total_monthly_buyer_cost - initial_monthly_rent
    if initial_monthly_savings < 0:
        initial_monthly_savings = 0

    renter_stock_value = calculate_stock_growth(down_payment_dollars, initial_monthly_savings, stock_return_rate, target_year)

    buyer_net_worth = buying_data["buyer_equity"]
    renter_net_worth = renter_stock_value

    if buyer_net_worth > renter_net_worth:
        winner = "Buying Wins!"
    elif renter_net_worth > buyer_net_worth:
        winner = "Renting Wins!"
    else:
        winner = "It's a Tie!"

    return {
        "buyer_net_worth": buyer_net_worth,
        "renter_net_worth": renter_net_worth,
        "winner": winner
    }


# ==========================================
# 2. STREAMLIT USER INTERFACE (WEB DISPLAY)
# ==========================================

st.set_page_config(page_title="Texas Buy vs. Rent Calculator", page_icon="🏠", layout="centered")

st.title("🏠 Texas Buy vs. Rent Calculator")
st.write("Compare long-term net worth outcomes for buying vs. renting real estate with localized Texas property taxes and opportunity-cost investing.")

st.markdown("---")

# Visual input sections using columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Homebuying Details")
    user_home_price = st.number_input("Home Price ($)", value=500000, step=10000)
    user_down_payment_pct = st.number_input("Down Payment (%)", value=20.0, step=1.0)
    user_tax_rate = st.number_input("Property Tax Rate (e.g. 0.02 for 2%)", value=0.02, step=0.001, format="%.3f")
    user_interest_rate = st.number_input("Mortgage Interest Rate (e.g. 0.065 for 6.5%)", value=0.065, step=0.005, format="%.3f")

with col2:
    st.subheader("Renting & Market Details")
    user_rent = st.number_input("Initial Monthly Rent ($)", value=2500, step=100)
    user_target_year = st.slider("Timeline (Years)", min_value=1, max_value=30, value=10)

st.markdown("---")

# Trigger button to run calculations
if st.button("Calculate Results", type="primary"):
    results = run_buy_vs_rent_analysis(
        original_home_price=user_home_price,
        down_payment_pct=user_down_payment_pct,
        tax_rate=user_tax_rate,
        annual_interest_rate=user_interest_rate,
        loan_duration_years=30,
        appreciation_rate=0.03,
        initial_monthly_rent=user_rent,
        rent_inflation_rate=0.035,
        stock_return_rate=0.08,
        target_year=user_target_year
    )

    st.header(f"Result: {results['winner']}")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label="Buyer Net Worth", value=f"${results['buyer_net_worth']:,.2f}")
    with res_col2:
        st.metric(label="Renter Net Worth", value=f"${results['renter_net_worth']:,.2f}")