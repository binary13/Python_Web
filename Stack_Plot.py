import matplotlib.pyplot as plt

year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Expenses, in thousands
taxes = [17, 19, 44, 43, 9, 8, 12, 51, 23, 40]
overhead = [18, 7, 12, 48, 23, 34, 64, 31, 12, 8]
entertainment = [20, 14, 32, 17, 31, 21, 22, 35, 24, 6]

plt.plot([], [], color='m', label='Taxes')
plt.plot([], [], color='y', label='Overhead')
plt.plot([], [], color='c', label='Entertainment')

plt.title('Company Expenses')
plt.xlabel('Years since 2004')
plt.ylabel('Thousands of dollars')
plt.legend()

plt.stackplot(year, taxes, overhead, entertainment, colors=['m','y','c'])
plt.show()