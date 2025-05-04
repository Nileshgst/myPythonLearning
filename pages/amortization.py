# This page is for loan calculator
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math


st.title("Loan Repayments Calculator",anchor=False)

st.write("### Input Data 1233")

# col1, col2 = st.columns(2)
# home_value = col1.number_input("Loan Value", min_value=0, value=500000)
# deposit = col1.number_input("Down Payment", min_value=0, value=100000)
# interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
# loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=20)


# # # Calculate the repayments.
# loan_amount = home_value - deposit
# monthly_interest_rate = (interest_rate / 100) / 12
# number_of_payments = loan_term * 12
# monthly_payment = (
#     loan_amount
#     * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
#     / ((1 + monthly_interest_rate) ** number_of_payments - 1)
# )

# # Display the repayments.
# total_payments = monthly_payment * number_of_payments
# total_interest = total_payments - loan_amount

# st.write("### Repayments",anchor=False)
# col1, col2, col3 = st.columns(3)
# col1.metric(label="Monthly Repayments", value=f"Rs:{monthly_payment:,.2f}")
# col2.metric(label="Total Repayments", value=f"Rs:{total_payments:,.0f}")
# col3.metric(label="Total Interest", value=f"Rs:{total_interest:,.0f}")


# # Create a data-frame with the payment schedule.
# schedule = []
# remaining_balance = loan_amount

# for i in range(1, number_of_payments + 1):
#     interest_payment = remaining_balance * monthly_interest_rate
#     principal_payment = monthly_payment - interest_payment
#     remaining_balance -= principal_payment
#     year = math.ceil(i / 12)  # Calculate the year into the loan
#     schedule.append(
#         [
#             i,
#             monthly_payment,
#             principal_payment,
#             interest_payment,
#             remaining_balance,
#             year,
#         ]
#     )

# df = pd.DataFrame(
#     schedule,
#     columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
# )

# # Display the data-frame as a chart.
# st.write("### Payment Schedule")
# payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
# #st.line_chart(payments_df)
# st.table(payments_df)



# def calculate_yearly_payments(loan_amount,loan_term,interest_rate):
#     output= (loan_amount*interest_rate)/(((1/(1+interest_rate)**loan_term))-1)  # formula calculated using sum of infinite GP series
#     return output


# def generate_amortization_schedule ()
#     yearly_payment = calculate_yearly_payments(loan_amount,loan_term,interest_rate)
#     schedule=[]
#     balance=loan_amount
#     for Year in range(1,n):
#         interest_payment = balance * r
#     principal_payment = yearly_payment - interest_payment
#     balance = principal_payment
#     schedule.append({
#             'Year' : Year,
#             'Payment' : yearly_payment,
#             'Principal' : principal_payment,
#             'Interest' : interest_payment,
#             'Balance' : balance     
#         })
#     return pd.DataFrame(schedule)   


# r = 0.04625 / 12
# P = 1100000
# n = 360

# common = (1 + r) ** n
# numerator = r * common
# denominator = common - 1
# monthly_total = round(P * (numerator / denominator), 2)
# print(monthly_total)

# curr_principal = round(P, 2)
# data = []
# for i in range(1, (n + 1), 1):
#     month_interest = curr_principal * r
#     month_principal = round(monthly_total - month_interest, 2)
#     curr_principal = curr_principal - month_principal
#     data.append([i, month_interest, month_principal, round(curr_principal, 2)])
    
# import pandas as pd
# pd.set_option('display.max_rows', None)
# df = pd.DataFrame(data, columns=["Period", "Interest", "Principal", "Remaining"], index= None)
# print(df.to_string(index=False))


#Import libraries
import streamlit as st
import plotly.express as px

import numpy as np
import pandas as pd
import datetime as dt
from dateutil.relativedelta import *

#Setting the page title name
st.set_page_config(
    page_title="Homeloan Amortisation Calculator")

st.title("Homeloan Amortisation Calculator")

#create the header 
st.header("**Inputs**")

#create a to place for the input fields 
colAnnualSal, colTax = st.beta_columns(2)
#create a to place for the input fields 
colAnnualSal, colTax = st.beta_columns(2)

#Creates a subheader for the bond price and an input box assigning the value to the variable bond_price
with colAnnualSal:
    st.subheader("Bond Price")
    bond_price = st.number_input("Enter your bond price: ", min_value=0.0, format='%f')

#Creates a subheader for the Repayment Value and an input box assigning the value to the variable monthly_repayment_value
with colAnnualSal:
    st.subheader("Repayment Value")
    monthly_repayment_value = st.number_input("Enter your monthly repayment value: ", min_value=0.0, format='%f')
    
with colAnnualSal:
    st.subheader("Extra Monthy Payment Amount")
    Extra_cont_payment_value = st.number_input("Enter the extra monthly payment value: ", min_value=0.0, format='%f')
    
with colAnnualSal:
    st.subheader("Start Date")
    start_date=st.date_input("Enter your bond start date")
    
with colAnnualSal:
    st.subheader("Interest Rate")
    interest_rate = st.number_input("Enter the interest rate (% annual)", min_value=0.0, format='%f')/100

#Init lists for the amort calcs
list_amounts = []
list_amounts.append(bond_price)
dates_list= []
dates_list.append(start_date)

#function for amortisation schedule, the value will start at the bond price at time 0 and reduce by the total repayment - interest 
# this will continue until the bond price is 0, each time it will add to the above lists.
# it assumes that interest is accrued and paid monthly and that the additional repayment is fixed.

def amort(bond_price,start_date,interest_rate=7,monthly_repayment_value=bond_price/30,Extra_cont_payment_value=0):
    while bond_price>0:
        
        #Calculates the amount owing on the bond and will append to the list
        bond_price=bond_price*(1+interest_rate/12)-monthly_repayment_value-Extra_cont_payment_value
        list_amounts.append([0 if bond_price < 0 else bond_price][0])
        
        #adds one month to the current date and then appends to the list
        start_date = start_date+ relativedelta(months=+1)#).strftime("%Y-%m-%d")
        dates_list.append(start_date)
        
    # converts the date and remaing bond into one dataframe  
    data=pd.DataFrame({'Amount_remaining':list_amounts,'repayment_date':dates_list},columns=['Amount_remaining','repayment_date'])
    return(data)
 
data= amort(bond_price,start_date,interest_rate,monthly_repayment_value,Extra_cont_payment_value)

st.header("**Home Loan Amount Owing **")
fig = px.line(data, x="repayment_date", y="Amount_remaining")

#creates a simple line chart showing the amortisation schedule over time
st.plotly_chart(fig, use_container_width=True)