# ==============================
# CUSTOMER CHURN ANALYSIS
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv("churn.csv")

print("\nFirst 5 rows:\n", df.head())

# ==============================
# DATA CLEANING
# ==============================

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Drop missing values
df = df.dropna()

# Convert Churn to numeric
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# ==============================
# BASIC METRICS
# ==============================

total_customers = len(df)
churn_rate = df["Churn"].mean() * 100
retention_rate = 100 - churn_rate
avg_tenure = df["Tenure"].mean()

print("\n===== KEY METRICS =====")
print("Total Customers:", total_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
print("Retention Rate:", round(retention_rate, 2), "%")
print("Average Customer Lifetime (Tenure):", round(avg_tenure, 2))

# ==============================
# CHURN BY CONTRACT
# ==============================

churn_contract = df.groupby("Contract")["Churn"].mean() * 100

print("\n===== CHURN BY CONTRACT =====")
print(churn_contract)

# Plot
plt.figure()
plt.bar(churn_contract.index, churn_contract.values)
plt.title("Churn by Contract Type")
plt.xlabel("Contract")
plt.ylabel("Churn Rate (%)")
plt.savefig("churn_by_contract.png")
plt.show()

# ==============================
# CHURN BY PAYMENT METHOD
# ==============================

churn_payment = df.groupby("PaymentMethod")["Churn"].mean() * 100

print("\n===== CHURN BY PAYMENT METHOD =====")
print(churn_payment)

plt.figure()
plt.bar(churn_payment.index, churn_payment.values)
plt.title("Churn by Payment Method")
plt.xticks(rotation=30)
plt.ylabel("Churn Rate (%)")
plt.savefig("churn_by_payment.png")
plt.show()

# ==============================
# CHURN BY INTERNET SERVICE
# ==============================

churn_internet = df.groupby("InternetService")["Churn"].mean() * 100

print("\n===== CHURN BY INTERNET SERVICE =====")
print(churn_internet)

plt.figure()
plt.bar(churn_internet.index, churn_internet.values)
plt.title("Churn by Internet Service")
plt.ylabel("Churn Rate (%)")
plt.savefig("churn_by_internet.png")
plt.show()

# ==============================
# TENURE GROUP (COHORT ANALYSIS)
# ==============================

df["TenureGroup"] = pd.cut(df["Tenure"],
                          bins=[0,6,12,24,60],
                          labels=["0-6 Months","6-12 Months","1-2 Years","2+ Years"])

cohort = df.groupby("TenureGroup")["Churn"].mean() * 100

print("\n===== CHURN BY TENURE GROUP =====")
print(cohort)

plt.figure()
plt.bar(cohort.index.astype(str), cohort.values)
plt.title("Churn by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.savefig("churn_by_tenure.png")
plt.show()

# ==============================
# HIGH vs LOW CHARGES ANALYSIS
# ==============================

avg_charge = df["MonthlyCharges"].mean()

high_charge = df[df["MonthlyCharges"] > avg_charge]
low_charge = df[df["MonthlyCharges"] <= avg_charge]

print("\n===== CHARGE ANALYSIS =====")
print("Average Monthly Charge:", round(avg_charge, 2))
print("High Charge Churn Rate:", round(high_charge["Churn"].mean()*100,2), "%")
print("Low Charge Churn Rate:", round(low_charge["Churn"].mean()*100,2), "%")

# ==============================
# REVENUE LOSS DUE TO CHURN
# ==============================

churned_customers = df[df["Churn"] == 1]
revenue_loss = churned_customers["MonthlyCharges"].sum()

print("\n===== REVENUE IMPACT =====")
print("Estimated Monthly Revenue Loss due to Churn:", round(revenue_loss, 2))

# ==============================
# FINAL INSIGHTS (AUTO PRINT)
# ==============================

print("\n===== KEY INSIGHTS =====")

print("- Month-to-month contracts show higher churn compared to long-term contracts.")
print("- Customers in early tenure (0-6 months) churn more frequently.")
print("- High monthly charges are associated with increased churn.")
print("- Fiber optic users tend to churn more than DSL users.")

print("\n===== RECOMMENDATIONS =====")

print("- Offer discounts for yearly or long-term subscriptions.")
print("- Improve onboarding experience for new customers.")
print("- Provide loyalty benefits for long-term users.")
print("- Optimize pricing strategies for high-cost plans.")

# ==============================
# END
# ==============================

print("\nAnalysis Completed Successfully ✅")