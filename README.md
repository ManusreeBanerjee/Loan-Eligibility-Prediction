# Loan-Eligibility-Prediction

Problem Statement : Predicting whether or not a customer is eligible for a loan is a very important problem for banks and other financial institutes. Ideally, a loan should only be approved for those customers who are likely to pay the money back, and should not be approved for the customers that are likely to default.



Overview : In the banking system, banks have a variety of products to provide, but credit lines are their primary source of revenue. As a result, they will profit from the interest earned on the loans they make. Loans, or whether customers repay or default on their loans, affect a bank's profit or loss. The bank's Non-Performing Assets will be reduced by forecasting loan defaulters. As a result, further investigation into this occurrence is essential. Because precise forecasts are essential for benefit maximisation, it's crucial to analyse and compare the various methodologies. 

Different Machine Learning Classification Algorithms have been used to determine under which interest slab the customer falls whether low, medium or high. In order to assess and forecast, data from Kaggle is acquired. 
Decision tree, SVM, KNN, Naiv Bayes Classification models were used to predict the multiclass output. The models are compared using Matthews correlation coefficient (MCC) which is an improvement over F1 score and accuracy in multiclass classification evaluation. In addition to checking account details (which indicate a customer's wealth), the model is significantly better because it includes variables (customer personal attributes such as Loan Amount, Interest.Rate, Loan Period, Loan Purpose, 
Debt To Income Ratio, Home Ownership, Monthly Income, FICO Range, Open CREDIT Lines, Revolving CREDIT Balance, Inquiries in the Last 6 Months, Employment Length) that should be considered when correctly calculating the Interest Rate on loan. As a result, using ML algorithms, the accurate Interest Slab into which clients can be classified for loan issuance can be easily identified and evaluated. 
