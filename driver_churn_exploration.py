# =============================================================================
# Imports
# =============================================================================
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
# =============================================================================
# Paths
# =============================================================================
file_path = "/Users/carolyndavis/Desktop/Project_data/"
file_name = "telco_data.xlsx"
# =============================================================================
# Loading
# =============================================================================
def data_loading(path, data_name):
    data = pd.read_excel(path+data_name)
    return data.dropna()

data = data_loading(file_path, file_name)
    
def churn_replacer(df):
    churn = []
    
    for x in df["churn"]:
        if x == "Yes": 
            churn.append(1)
        if x == "No": 
            churn.append(0)
    
    churn = pd.Series(churn)
    
    df.loc[:, "churn_num"] = churn
    
    return df

data = churn_replacer(data)

def monthly_only(df):
    monthly = df[df["contract_type"] == 0]
    return monthly

monthly_data = monthly_only(data)


def dollar_cat(df):
    df2 = df.copy()
    # based off monthly, and find mean monthly, and max, to figure out the ranges of our 3 cats
    print(df2['monthly_charges'].describe())
    # print(df2['total_charges'].describe())
    
    
    cats = {"Low": [i for i in np.arange(0, 40, 0.01)],
            "Med": [i for i in np.arange(40, 80, 0.01)],
            "High": [i for i in np.arange(80, 121, 0.01)]}
    
    month_charg = []
    for amount in df2["monthly_charges"]:
        for key, value in cats.items():
            if amount >= value[0] and amount <= value[-1]:
                print(f"amount: {amount} key: {key} value1: {value[0]} value2: {value[-1]}")
                month_charg.append(key)
                
    # filter into new dfs that have monthly charges in ranges A, B, C etc. 
    # find the length for category analysis later. 
    
    month_charg = pd.DataFrame(month_charg).set_index(df2.index)
    
    df2['contract_length'] = df2["total_charges"] / df2["monthly_charges"]
    
    print(df2['contract_length'].describe())
    
    contract_rubric = {"short": [0, 12],
                       "medium": [12.01, 36],
                       "long": [36.01, 72]}
    
    contract_len = []
    for length in df2["contract_length"]:
        for key, value in contract_rubric.items():
            if length > value[0] and length <= value[-1]:
                print(f"length: {length} key: {key} value1: {value[0]} value2: {value[-1]}")
                contract_len.append(key)
    contract_len = pd.DataFrame(contract_len).set_index(df2.index)
    
    
    
    
    df2['monthly_cat'] = month_charg
    df2['contract_length'] = contract_len
    
    return df2

 # = dollar_cat(monthly_data)
monthly_data = dollar_cat(monthly_data)


def cat_only(df):
    df2 = df.copy()
    df2 = df2.drop(["monthly_charges", "total_charges"], axis=1)
    return df2

categorical_only = cat_only(monthly_data)

def renamer(df):
    
    df2 = df.copy()
    
    seniors = []
    for value in df2["is_senior_citizen"]:
        if value == 0:
            seniors.append("Not_Senior")
        if value == 1:
            seniors.append("Senior")
            
    seniors = pd.DataFrame(seniors).set_index(df2.index)
    
    phone_service = []
    for value in df2["phone_service"]:
        if value == 0:
            phone_service.append("No_phone_service")
        if value == 1:
            phone_service.append("One_phone_line")
        if value == 2:
            phone_service.append("Two_plus_lines")
            
    phone_service = pd.DataFrame(phone_service).set_index(df2.index)
    
    internet_service = []
    for value in df2["internet_service"]:
        if value == 0:
            internet_service.append("No internet")
        if value == 1:
            internet_service.append("DSL internet")
        if value == 2:
            internet_service.append("Fiber optic")
    
    internet_service = pd.DataFrame(internet_service).set_index(df2.index)
    
    df2["is_senior_citizen"] = seniors 
    df2["phone_service"] = phone_service
    df2["internet_service"] = internet_service
    
    return df2.set_index("customer_id")

categorical_only = renamer(categorical_only)

def fiber_only(df):
    df2 = df.copy()
    df2 = df2[df2["internet_service"] == "Fiber optic"]
    return df2

fiber_only = fiber_only(categorical_only)
        
def cat_grouper(df):
    collector = {}
    for col in df.columns:
        if "churn" not in col:
            collector[col] = {}
            for unq in df[col].unique():
                print(f"{col} {unq}")
                churn_count = df[df[col] == unq]
                churn_count = churn_count["churn_num"].sum()
                collector[col][str(unq)] = churn_count
                
    return collector

cat_groups = cat_grouper(categorical_only)

# cat_description = pd.DataFrame.from_dict(cat_groups)

fib_description = cat_grouper(fiber_only)

# cat_description.plot.bar()

def plotter(df, tag):
    for key, value in df.items():
        value = pd.DataFrame.from_dict(value, orient="index")
        value.plot.bar(edgecolor='black')
        plt.title(f"{key} {tag}")
        plt.legend()
        # plt.savefig(PATH+key+tag+".png")
        plt.show()
        plt.close()
    
plotter(cat_groups, "") # all monthly
plotter(fib_description, "Fiber Optic Only") # fiberoptic only

