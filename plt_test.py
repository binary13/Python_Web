import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [4,3,1,7,10]
y2 = [5,6,9,21,76]
plt.plot(x, y1, label='Europe')
plt.plot(x, y2, label = "United States")
plt.title("Recent Rain of Terror")
plt.xlabel('Year since 1999')
plt.ylabel('Alien Abductions')
plt.legend()
plt.show()
print('Got here.')