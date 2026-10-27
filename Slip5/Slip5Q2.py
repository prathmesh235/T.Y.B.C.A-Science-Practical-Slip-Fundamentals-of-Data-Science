import matplotlib.pyplot as plt

names = ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan']
percentage = [75, 85, 90, 68, 80]

plt.subplot(1, 2, 1)
plt.pie(percentage, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.subplot(1, 2, 2)
plt.bar(names, percentage, color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Student Names")
plt.ylabel("Percentage")

plt.tight_layout()
plt.show()