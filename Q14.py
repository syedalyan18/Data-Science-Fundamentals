import matplotlib.pyplot as plt

# LINE PLOT

# plt.plot([1,2,3],[10,20,30], label="trend",color="orange",linestyle="--",marker="o")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()

# BAR CHART

# categories=["A","B","C"]
# values=[15,8,10]
# plt.bar(categories,values,color="green")
# plt.title("BAR-CHART")
# plt.show()

# HISTOGRAM

# data=[1,2,2,3,3,3,3]
# plt.hist(data,bins=3,color="blue", edgecolor="black")
# plt.title("HISTOGRAM")
# plt.show()

# SCATTER PLOT

x=[1,2,3,4,5]
y=[10,12,23,29,35]
plt.scatter(x,y,color="red")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(["DATASET 1"])
plt.title("SCATTER PLOT")
plt.show()