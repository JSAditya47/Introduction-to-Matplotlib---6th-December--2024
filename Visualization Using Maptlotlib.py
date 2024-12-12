import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("company_sales_data.csv")
print(train)

profitList = train ["total_profit"].tolist()
monthList = train ["month_number"].tolist()

plt.plot(monthList, profitList, label= "Month-Wise Profit Data of Last Year")
plt.xlabel("Month Number")
plt.ylabel("Profit in Dollar")
plt.xticks(monthList)
plt.title("Company Profit Per Month")
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
