import matplotlib.pyplot as plt

# Create two lists
subjects = ['Java', 'Python', 'DBMS', 'FDS', 'CN']
marks = [85, 90, 75, 80, 70]

# Pie Chart
plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject Marks - Pie Chart")
plt.show()

# Bar Chart
plt.figure()
plt.bar(subjects, marks, edgecolor='black')
plt.title("Subject Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()