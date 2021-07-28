#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:01:24 2021

@author: carolyndavis
"""

import pandas as pd
data = pd.read_excel('telco_data.xlsx')

data.isna().sum()   #11 values for total_charges missing

data = data.dropna()   #Cleaned data with missing values in total_charges column

monthly_data = data[data['contract_type'] == 0]

data.info()



type(data['churn'])

# test = data["churn"] = data["churn"]['yes' == 1]

converted = data["churn"].copy()
# converted = pd.Series([1 for x if x == True else 0 for x in converted])

print(converted.unique())

conv = []
for x in converted:
    if x == "Yes":
        conv.append(1)
    else:
        conv.append(0)

conv = pd.Series(conv)

data.loc[:, "churn_num"] = conv


# data["payment_type"].unique()

# payments = []
# for x in data.loc[:, "payment_type"]:
#     if x == "Mailed check":
#         payments.append(0)
#     if x == "Electronic check":
#         payments.append(1)
#     if x == "Credit card (automatic)":
#         payments.append(2)
#     if x == "Bank transfer (automatic)":
#         payments.append(3)

# payment_num = pd.Series(payments)
# data.loc[:, "payment_num"] = payment_num


matrix = data.corr()

collector = {}

for col in data.columns:
    print(f"column name: {col}")
    if col != "customer_id":
        collector[col] = {}
        for unq in data[col].unique():
            print(unq)
            # x = data[col].groupby(unq)
