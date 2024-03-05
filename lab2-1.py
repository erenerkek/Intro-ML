import matplotlib.pyplot as plt
import numpy as np

data= np.random.randn(1000)

plt.hist(data,bins=30)
plt.title("histogram")
plt.xlabel("Values")
plt.ylabel("Frequencies")
plt.show()

sizes=[]
plt.pie(sizes)
plt.title("Pie Chart")
plt.show()