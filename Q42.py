import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
reviews_df = pd.read_csv('C:/Users/Patrick/Downloads/reviews.csv')

# Convert 'date' column to datetime format
reviews_df['date'] = pd.to_datetime(reviews_df['date'])

# Count the number of reviews for each rating
rating_counts = reviews_df['stars'].value_counts().sort_index()

# Plotting
plt.bar(rating_counts.index, rating_counts.values, color='skyblue')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.title('Distribution of Ratings (All Time)')
plt.show()
