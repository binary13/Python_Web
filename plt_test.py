import matplotlib.pyplot as plt

test_scores = [55, 60, 75, 80, 93, 76, 92, 41, 17, 75, 95, 82, 76]
time_spent = [40, 45, 55, 60, 60, 54, 58, 22, 5, 36, 57, 50, 49]

plt.scatter(time_spent, test_scores, marker='v', color="r")
plt.xlabel('Time spent on test')
plt.ylabel('Test Scores')

plt.show()