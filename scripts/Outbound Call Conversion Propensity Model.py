#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read customer file
df = pd.read_excel(r"C:\& Power BI\Outbound_Calling_Model.xlsx")

def conversion_score(row):
    score = 0

    # Maturity date close
    if row["days_to_maturity"] <= 30:
        score += 30
    elif row["days_to_maturity"] <= 90:
        score += 20

    # Active Direct Debit
    if row["active_dd"] == "Yes":
        score += 20

    # Failed Direct Debit
    if row["failed_dd"] == "Yes":
        score -= 15

    # High value customer
    if row["account_value"] >= 10000:
        score += 25
    elif row["account_value"] >= 5000:
        score += 15

    # Online engagement
    if row["online_login_days"] <= 30:
        score += 15

    # Complaints
    if row["complaints"] == 0:
        score += 10
    elif row["complaints"] >= 2:
        score -= 20

    return score


df["conversion_score"] = df.apply(conversion_score, axis=1)

def conversion_category(score):
    if score >= 70:
        return "High Conversion Potential"
    elif score >= 40:
        return "Medium Conversion Potential"
    else:
        return "Low Conversion Potential"

df["conversion_category"] = df["conversion_score"].apply(conversion_category)

# Sort best customers first
df = df.sort_values(by="conversion_score", ascending=False)

# Export call centre file
df.to_excel(r"C:\& Power BI\Outbound_Calling_Output.xlsx", index=False)

print(df.head())


# In[ ]:




