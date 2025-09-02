import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data_AI = pd.read_csv('ai_financial_market_daily_realistic_synthetic.csv')

# 1- summary of datafraame:
print(data_AI.info())

# 2- what is the columns of dataframe?
print(data_AI.columns)

# 3- check for empty values:
print(data_AI.isnull().sum())

# 4- how much amount spended for R&D?
total_RD_spending = data_AI['R&D_Spending_USD_Mn'].sum()
print("total spending for R&D: ",total_RD_spending)

# 5- what is the average of R&D spending?
average_RD_spending = data_AI['R&D_Spending_USD_Mn'].mean()
print("average spending for R&D: ",average_RD_spending)

# 6- what is the maximum and minimum R&D spending?
max_RD_spending = data_AI['R&D_Spending_USD_Mn'].max()
min_RD_spending = data_AI['R&D_Spending_USD_Mn'].min()
print("maximum R&D spending: ",max_RD_spending, "\nminimum R&D spending: ", min_RD_spending)

# 7- revenue earned by the companies?
total_revenue = data_AI.groupby("Company")["AI_Revenue_USD_Mn"].sum()
print("total revenue earned by the companies: ", total_revenue)

average_revenue = data_AI.groupby("Company")["AI_Revenue_USD_Mn"].mean()
print("average revenue earned by the companies: ", average_revenue)

# 8- how date impact on stock? Create a graph.

plt.figure(figsize=(12,6))
plt.plot(data_AI['Date'], data_AI['Stock_Impact_%'], label='Stock Impact %')
plt.xlabel('Date')
plt.ylabel('Stock Impact (%)')
plt.title('Stock Impact % Over Time')
plt.legend()
plt.tight_layout()
plt.show()

# 9- AI Revenue growth of companies? Create a graph.
revenue_growth = data_AI.groupby(["Company","R&D_Spending_USD_Mn"])["AI_Revenue_Growth_%"].mean().reset_index()
print(revenue_growth)

plt.figure(figsize=(12,6))
sns.barplot(x="R&D_Spending_USD_Mn", y="AI_Revenue_Growth_%", hue="Company", data=revenue_growth)
plt.title("AI Revenue Growth % by Company")
plt.xlabel("R&D_Spending_USD_Mn")
plt.ylabel("AI Revenue Growth (%)")
plt.legend(title="Company")
plt.tight_layout()
plt.show()












