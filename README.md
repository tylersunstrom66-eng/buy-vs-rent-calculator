# 🏠 Texas Buy vs. Rent & True Cost Calculator

An interactive, web-based financial modeling tool built with Python and Streamlit. This application helps users evaluate the long-term wealth outcomes of **buying a home versus renting and investing the difference**, specifically tailored for the Texas real estate market with localized property tax calculations and opportunity-cost compounding.

🚀 **Live Demo:** https://YOUR_APP_LINK_HERE.streamlit.app

---

## 📌 Overview

Deciding whether to buy a home or rent is one of the most critical financial choices a consumer can make. In states like Texas—where property taxes average around 1.8% to 2.2%—the "true cost" of homeownership extends far beyond principal and interest payments.

This application models the full financial trajectory of both scenarios over a flexible 1-to-30-year timeline, giving users clear, data-driven insights into which strategy builds greater net worth.

---

## ✨ Key Features

* **Texas-Specific Property Tax Scaling:** Incorporates localized annual property tax estimates directly into monthly cash flow and total cost calculations.
* **Mortgage Amortization Logic:** Accurately tracks principal reduction, remaining loan balance, and home equity growth over time.
* **Opportunity Cost & Stock Compounding:** Simulates the renter investing both the initial down payment money AND any monthly savings (if rent is cheaper than the mortgage + tax burden) into standard market returns (e.g., S&P 500 at 8% CAGR).
* **Interactive UI:** Dynamic sliders and numerical inputs allow real-time scenario testing with immediate visual output via Streamlit metrics.

---

## 🧮 Financial Engine & Formulas

### 1. Homeownership Model
* **Monthly Mortgage Payment (M):** Calculated using the standard loan amortization formula:
  $$M = P \cdot \frac{r(1 + r)^n}{(1 + r)^n - 1}$$
  *(where P = Loan Principal, r = Monthly Interest Rate, n = Total Payments)*
* **Property Taxes:** Calculated as `(Home Price * Annual Tax Rate) / 12` added to monthly outlay.
* **Buyer Net Worth:** Defined as ending **Home Equity** (`Future Home Value - Remaining Loan Balance`).

### 2. Renting & Opportunity Cost Model
* **Rent Growth:** Rent escalates annually based on user-selected inflation rates.
* **Compound Investment Portfolio:**
  $$V_t = (V_{t-1} + C) \cdot (1 + r_{monthly})$$
  *(where C = Monthly savings difference between buying and renting, r_{monthly} = Monthly stock return rate)*
* **Renter Net Worth:** Defined as ending **Stock Portfolio Value**.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **Framework:** [Streamlit](https://streamlit.io/) (Web UI & Rendering)
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Community Cloud

---

## 📁 Repository Structure

```text
├── app.py              # Main application entry point containing UI & financial engine
├── requirements.txt    # Production dependencies (streamlit)
└── README.md           # Project documentation
🔄 GitHub Workflow & Continuous Deployment
This repository uses a continuous delivery pipeline connected directly to Streamlit Community Cloud:

Development & Version Control: Code updates are pushed to the main branch via Git.

Bash
git add .
git commit -m "Update application features"
git push origin main
Automated Cloud Build: Streamlit Community Cloud monitors the repository, automatically building and deploying new code commits in real-time.

💻 Local Setup & Installation
To run this application locally on your machine:

Clone the repository:

Bash
git clone [https://github.com/tylersunstrom66-eng/buy-vs-rent-calculator.git](https://github.com/tylersunstrom66-eng/buy-vs-rent-calculator.git)
cd buy-vs-rent-calculator
Install dependencies:

Bash
pip install -r requirements.txt
Launch the Streamlit app:

Bash
streamlit run app.py
🚀 Future Roadmap & Enhancements
[ ] Add downloadable PDF / CSV financial summary reports.

[ ] Implement maintenance/HOA fee input fields for deeper accuracy.

[ ] Add interactive chart visualizations for net worth progression over time.

Author: tylersunstrom66-eng

License: MIT
