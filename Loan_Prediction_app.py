import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import pickle
from dateutil.relativedelta import relativedelta
from sklearn.preprocessing import LabelEncoder
# import the lib to Save/Load the model
import joblib 



st.set_page_config(page_title="Loan Interest Prediction App",page_icon="💲",layout="centered",initial_sidebar_state="expanded")

st.sidebar.header('Enter Client Parameters')
   
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:light blue;padding:13px"> 
    <h1 style ="color:pink;text-align:center;">Loan Interest Prediction App</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Manusree Banerjee')
      
# following lines create boxes in which user can enter data required to make prediction
custid=st.sidebar.text_input("Customer ID")
amt_reqstd = st.sidebar.number_input('Amount requested (in $)', min_value=0, max_value=50000, step=1)
amt_fund = st.sidebar.number_input('Amount funded by investors (in $)', min_value=0, max_value=50000, step=1)
loan_len = st.sidebar.slider('Loan length (in months)', min_value=0, max_value=30)
loan_purp = st.sidebar.selectbox('Loan purpose', ('Car', 'Credit card', 'Debt consolidation', 'Educational', 'Home improvement', 'House', 'Major purchase', 'Medical', 'Moving', 'Renewable energy', 'Small business', 'Vacation',  'Wedding',  'Other'))
debt_inc_ratio = st.sidebar.slider('Debt to income ratio', min_value=0, max_value=40)
hom_own = st.sidebar.selectbox('Home ownership', ('MORTGAGE', 'RENT', 'OWN', 'OTHER', 'NONE'))
mon_inc = st.sidebar.number_input('Monthly income (in $)')
fico = st.sidebar.slider('FICO score', min_value=350, max_value=850)
cred_line = st.sidebar.slider('Open credit lines', min_value=0, max_value=40)
cred_bal = st.sidebar.number_input('Revolving credit balance (in $)')
inq_6_mont = st.sidebar.slider('Inquiries in last 6 months', min_value=0, max_value=15)
emp_len = st.sidebar.selectbox('Employment length (in years)', ('<1', '2', '3', '4', '5', '6', '7', '8', '9', '>10', 'na'))



# Assign value to Loan Purpose
purp_dict = {'Car': 0, 'Credit card': 1, 'Debt consolidation': 2, 'Educational': 3, 'Home improvement': 4, 'House': 5, 'Major purchase': 6, 'Medical': 7, 'Moving': 8, 'Other': 9, 'Renewable energy': 10, 'Small business': 11, 'Vacation': 12, 'Wedding': 13}
# Get value from the dictionary
purpose = purp_dict.get(loan_purp)

# Assign value to  Home Ownership
homeown_dict = {'MORTGAGE': 0, 'NONE': 1, 'OTHER': 2, 'OWN': 3, 'RENT': 4}
# Get value from the dictionary
ownership = homeown_dict.get(hom_own)

# Convert Employment length to whole number
if emp_len =='<1':
  emp_len=1
elif emp_len == '>10':
  emp_len=10
else :
  emp_len=emp_len

if st.button("PREDICT"):
    user_input=[[amt_reqstd,amt_fund,loan_len,purpose,debt_inc_ratio,ownership,mon_inc,fico,cred_line,cred_bal,inq_6_mont,emp_len]]
    #load the model from disk
    loaded_model = joblib.load("gboost.pkl")
    int_rate = loaded_model.predict(user_input) 
    st.write("Interest Rate assigned is ",round(int_rate[0],2))
    


st.info("Don't forget to rate this app")
  
feedback = st.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)
  
if feedback:
    st.header("Thank you for rating the app!")


st.subheader("About App")

st.info("This web app helps you to calculate interest rate on loan based on a customer's background.")
st.info("Enter the required fields and click on the 'PREDICT' button to calculate interest rate.")


st.caption("Caution: This is just a prediction and may not be exact.")
