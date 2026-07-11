import matplotlib.pyplot as plt

# plt.plot([1,2,3],[10,20,30], label="trend")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()

# categories=["A","B","C"]
# values=[15,8,10]
# plt.bar(categories,values,color="green")
# plt.title("BAR-CHART")
# plt.show()

data=[1,2,2,3,3,3,3]
plt.hist(data,bins=3,color="blue", edgecolor="black")
plt.title("HISTOGRAM")
plt.show()