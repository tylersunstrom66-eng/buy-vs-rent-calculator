#Module 1
def calculate_buying_cost(original_home_price, down_payment_pct, tax_rate, annual_interest_rate, loan_duration_years, appreciation_rate, target_year):
    # Homeownership Cost Engine
    down_payment_price = original_home_price * (down_payment_pct / 100)
    closing_cost = original_home_price * 0.03
    initial_total_out_of_pocket = down_payment_price + closing_cost

    # Monthly Debt Service
    loan_amount = original_home_price - down_payment_price
    r = annual_interest_rate / 12
    n = loan_duration_years * 12
    monthly_pi = loan_amount * (r * (1 + r) ** n) / (((1 + r) ** n) - 1)

    # Monthly Recurring Operating Expenses
    current_home_value = original_home_price * ((1 + appreciation_rate) ** target_year)
    property_taxes = (current_home_value * tax_rate) / 12
    homeowner_insurance = (current_home_value * 0.0075) / 12
    maintenance_reserve = (current_home_value * 0.01) / 12
    pmi = (loan_amount * 0.01) / 12 if down_payment_pct < 20 else 0

    # Home Appreciation & Selling Costs
    future_home_value = current_home_value
    p = target_year * 12
    future_loan_balance = loan_amount * (((1 + r) ** n - (1 + r) ** p) / (((1 + r) ** n) - 1))
    gross_home_equity = future_home_value - future_loan_balance

    return {
        "monthly_PI": monthly_pi,
        "total_monthly_expense": monthly_pi + property_taxes + homeowner_insurance + maintenance_reserve + pmi,
        "future_home_value": future_home_value,
        "remaining_loan_balance": future_loan_balance,
        "gross_home_equity": gross_home_equity
    }


#Module 2
def calculate_renting_costs(initial_monthly_rent, rent_inflation_rate, target_year, security_deposit_months=1):
    # Upfront Renting Costs
    security_deposit = initial_monthly_rent * security_deposit_months
    initial_rent_out_of_pocket = security_deposit
    
    # Monthly Running Costs & Inflation Loop
    current_monthly_rent = initial_monthly_rent
    renter_insurance_monthly = 25.0  # standard monthly estimate
    total_rent_paid = 0
    
    # Track monthly expenses year by year
    for year in range(1, target_year + 1):
        for month in range(1, 13):
            monthly_total = current_monthly_rent + renter_insurance_monthly
            total_rent_paid += monthly_total
            
        # After each full year, increase rent by the inflation rate
        if year < target_year:
            current_monthly_rent *= (1 + rent_inflation_rate)
            
    return {
        "initial_rent_out_of_pocket": initial_rent_out_of_pocket,
        "final_monthly_rent": current_monthly_rent,
        "total_cumulative_rent_paid": total_rent_paid
    }


#Module 3
def calculate_stock_growth(initial_amount, annual_return, target_year):
    future_value = initial_amount * (1 + annual_return) ** target_year
    return future_value


#Module 4 (Master Function)
def run_buy_vs_rent_analysis(
        original_home_price,
        down_payment_pct,
        tax_rate,
        annual_interest_rate,
        loan_duration_years,
        appreciation_rate,
        initial_monthly_rent,
        rent_inflation_rate,
        stock_return_rate,
        target_year
):
    # Run Module 1 (Buying) dynamically using passed arguments
    buy_results = calculate_buying_cost(
        original_home_price, down_payment_pct, tax_rate, 
        annual_interest_rate, loan_duration_years, appreciation_rate, target_year
    )

    # Run Module 2 (Renting) dynamically using passed arguments
    rent_results = calculate_renting_costs(
        initial_monthly_rent, rent_inflation_rate, target_year
    )

    # Calculate initial cash difference for opportunity cost
    down_payment_price = original_home_price * (down_payment_pct / 100)
    closing_cost = original_home_price * 0.03
    buyer_initial_cash = down_payment_price + closing_cost

    renter_security_deposit = initial_monthly_rent * 1
    renter_initial_cash = renter_security_deposit

    # The cash the renter saved upfront that goes straight into the stock market
    cash_invested_by_renter = buyer_initial_cash - renter_initial_cash

    # Run Module 3: Stock Market growth on that initial difference
    stock_portfolio_value = calculate_stock_growth(
        initial_amount=cash_invested_by_renter, 
        annual_return=stock_return_rate, 
        target_year=target_year
    )

    # Final Net Worth comparison (accounting for 7% realtor selling fees if selling the house)
    selling_costs = buy_results["future_home_value"] * 0.07
    buyer_net_worth = buy_results["gross_home_equity"] - selling_costs
    renter_net_worth = stock_portfolio_value

    # Determine the winner (fixed format specifier to :,.2f)
    net_difference = abs(buyer_net_worth - renter_net_worth)
    if buyer_net_worth > renter_net_worth:
        winner = f"Buying wins by ${net_difference:,.2f}"
    else:
        winner = f"Renting wins by ${net_difference:,.2f}"

    return {
        "buyer_net_worth": buyer_net_worth,
        "renter_net_worth": renter_net_worth,
        "winner": winner,
        "details": {
            "home_equity": buy_results["gross_home_equity"],
            "stock_portfolio": stock_portfolio_value,
            "total_rent_paid": rent_results["total_cumulative_rent_paid"]
        }
    }


# Execute the Analysis
# A helper function that forces the user to type a valid number
def get_valid_float(prompt_message):
    while True:
        try:
            # Try to get input and convert to float
            return float(input(prompt_message))
        except ValueError:
            # If it fails (e.g. they typed letters), catch the error and repeat
            print("⚠️ Invalid input! Please enter a valid number (e.g., 500000). Try again.\n")

print("=== TEXAS BUY VS. RENT CALCULATOR ===")
print("Please enter your financial details below:\n")

# Use our new safety net function for inputs
user_home_price = get_valid_float("Enter home price (e.g., 500000): ")
user_down_payment_pct = get_valid_float("Enter down payment percentage (e.g., 20 for 20%): ")
user_tax_rate = get_valid_float("Enter annual property tax rate as a decimal (e.g., 0.02 for 2%): ")
user_interest_rate = get_valid_float("Enter mortgage interest rate as a decimal (e.g., 0.065 for 6.5%): ")
user_rent = get_valid_float("Enter initial monthly rent (e.g., 2500): ")

# For timeline, we want an integer instead of a float
while True:
    try:
        user_target_year = int(input("Enter timeline in years (e.g., 5 or 15): "))
        break
    except ValueError:
        print("⚠️ Invalid input! Please enter a whole number for years.\n")

# Pass those validated inputs into your master function
final_analysis = run_buy_vs_rent_analysis(
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

# Print out the results dynamically
print("\n=== CALCULATOR RESULTS ===")
print(f"Timeline:          {user_target_year} Years")
print(f"Buyer Net Worth:   ${final_analysis['buyer_net_worth']:,.2f}")
print(f"Renter Net Worth:  ${final_analysis['renter_net_worth']:,.2f}")
print(f"Result:            {final_analysis['winner']}")