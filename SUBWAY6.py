import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
reviews_df = pd.read_csv('C:/Users/Patrick/Downloads/reviews.csv')
restaurants_df = pd.read_csv('C:/Users/Patrick/Downloads/restaurants.csv')

# Merge the two datasets on the common column 'business_id'
merged_df = pd.merge(reviews_df, restaurants_df, on='business_id', how='inner')

# Calculate the number of reviews for each restaurant
num_reviews_per_restaurant = merged_df.groupby('business_id')['stars'].count()

# Calculate the average rating for each restaurant
avg_rating_per_restaurant = merged_df.groupby('business_id')['stars'].mean()

# Create a DataFrame with the number of reviews and average rating
data = pd.DataFrame({'num_reviews': num_reviews_per_restaurant, 'avg_rating': avg_rating_per_restaurant})

# Calculate correlation
correlation = data['num_reviews'].corr(data['avg_rating'])
print(f'Correlation between number of reviews and average rating: {correlation}')

# Scatter plot
plt.scatter(data['num_reviews'], data['avg_rating'])
plt.xlabel('Number of Reviews')
plt.ylabel('Average Rating')
plt.title('Scatter Plot: Number of Reviews vs Average Rating')

# Fit a linear regression line using numpy
x = data['num_reviews'].values
y = data['avg_rating'].values

# Calculate the coefficients (slope and intercept) of the line
slope, intercept = np.polyfit(x, y, 1)

# Plot the line of best fit
plt.plot(x, slope * x + intercept, color='red', linewidth=2)

plt.show()
