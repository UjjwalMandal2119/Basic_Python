import matplotlib.pyplot as plt
x=['Thur', 'Fri', 'Sat', 'Sun']
y=[170,120,250,190]

plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("total Bill")
plt.show()


plt.hist(x, bins=10, color='steelblue')
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

plt.title("Liner Regression")