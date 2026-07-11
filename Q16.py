import matplotlib.pyplot as plt

# LINE PLOT

# years=[2020,2021,2022,2023,2024]
# sales=[100,120,140,160,180]
# plt.plot(years,sales, label="Sales Trend",color="orange",linestyle="--",marker="o")
# plt.title("SALES OVER YEARS")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# BAR CHART

# categories=["Electronics","Clothing","Groceries"]
# revenue=[130,150, 110]
# plt.bar(categories,revenue,color="green")
# plt.title("REVENUE BY CATEGORY")
# plt.show()

# HISTOGRAM

# data=[1,2,2,3,3,3,3]
# plt.hist(data,bins=3,color="blue", edgecolor="black")
# plt.title("HISTOGRAM")
# plt.show()

# SCATTER PLOT

hours=[1,2,3,4,5]
marks=[50,60,70,80,90]
plt.scatter(hours,marks,color="red")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend(["PRECISION"])
plt.title("MARKS PER HOURS OF STUDY")
plt.show()