import matplotlib.pyplot as plt

names = ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan']
percentage = [75, 85, 90, 68, 80]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.pie(percentage, labels=names, autopct='%1.1f%%')
plt.title("Student Percentage - Pie Chart")

plt.subplot(1, 2, 2)
plt.bar(names, percentage, color='skyblue')
plt.title("Student Percentage - Bar Chart")
plt.xlabel("Student Names")
plt.ylabel("Percentage")
plt.ylim(0, 100)

plt.tight_layout()
plt.show()