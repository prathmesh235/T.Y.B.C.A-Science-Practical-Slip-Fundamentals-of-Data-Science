import pandas as pd

# Create dictionary of books
data = {
    'Book Title': [
        'Wings of Fire', 'Atomic Habits', 'Rich Dad Poor Dad',
        'The Alchemist', 'Ikigai', 'Think and Grow Rich',
        'Deep Work', 'The Power of Habit'
    ],
    'Author': [
        'A.P.J. Abdul Kalam', 'James Clear', 'Robert Kiyosaki',
        'Paulo Coelho', 'Hector Garcia', 'Napoleon Hill',
        'Cal Newport', 'Charles Duhigg'
    ],
    'Category': [
        'Autobiography', 'Self-help', 'Finance', 'Fiction',
        'Self-help', 'Finance', 'Productivity', 'Psychology'
    ],
    'Rating': [4.8, 4.7, 4.5, 4.6, 4.4, 4.3, 4.6, 4.5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first 5 records
print(df.head(5))
