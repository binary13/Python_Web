import matplotlib.pyplot as plt

labels=['Taxes', 'Overhead', "Entertainment"]
colors=['c', 'm', 'y']
sizes = [25, 32, 12]

plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=90)
plt.title('Expense Proportions')
plt.show()
