import matplotlib.pyplot as plt
import numpy as np
import seaborn as snc

data=np.random.rand(5,5)
snc.heatmap(data,annot=True,cmap="coolwarm")
plt.title("HEATMAP")
plt.show()