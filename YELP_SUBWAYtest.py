import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import datetime

# Read the CSV files
reviews_df = pd.read_csv('C:/Users/Patrick/Downloads/reviews.csv')
restaurants_df = pd.read_csv('C:/Users/Patrick/Downloads/restaurants.csv')

# Merge the two datasets on the common column 'business_id'
merged_df = pd.merge(reviews_df, restaurants_df, on='business_id', how='inner')

# Filter data to include only "Subway" restaurants
subway_df = merged_df[merged_df['name'] == 'Subway']

# Convert the 'date' column to datetime format
subway_df['date'] = pd.to_datetime(subway_df['date'])

# Extract the year from the date
subway_df['year'] = subway_df['date'].dt.year

# Calculate average rating per year
avg_rating_per_year = subway_df.groupby('year')['stars'].mean()

# Calculate the number of ratings per year
num_ratings_per_year = subway_df.groupby('year').size()

# Linear regression for average rating prediction
X_avg_rating = avg_rating_per_year.index.values.reshape(-1, 1)
y_avg_rating = avg_rating_per_year.values.reshape(-1, 1)

model_avg_rating = LinearRegression()
model_avg_rating.fit(X_avg_rating, y_avg_rating)

# Predicting next 2 years for average rating starting from 1/19/2022
start_date = datetime.datetime(2022, 1, 19)
future_years_avg_rating = pd.date_range(start=start_date, periods=2, freq='Y')
future_years_avg_rating = future_years_avg_rating.year.values.reshape(-1, 1)
predicted_avg_rating = model_avg_rating.predict(future_years_avg_rating)

# Linear regression for number of ratings prediction
X_num_ratings = num_ratings_per_year.index.values.reshape(-1, 1)
y_num_ratings = num_ratings_per_year.values.reshape(-1, 1)

model_num_ratings = LinearRegression()
model_num_ratings.fit(X_num_ratings, y_num_ratings)

# Predicting next 2 years for number of ratings starting from 1/19/2022
future_years_num_ratings = pd.date_range(start=start_date, periods=2, freq='Y')
future_years_num_ratings = future_years_num_ratings.year.values.reshape(-1, 1)
predicted_num_ratings = model_num_ratings.predict(future_years_num_ratings)

# Plotting the results
fig, ax1 = plt.subplots()

# Plotting actual data
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Rating', color=color)
ax1.plot(avg_rating_per_year.index, avg_rating_per_year, color=color)
ax1.plot(future_years_avg_rating, predicted_avg_rating, linestyle='dashed', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Creating a secondary y-axis for number of ratings
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Number of Ratings', color=color)
ax2.bar(num_ratings_per_year.index, num_ratings_per_year, alpha=0.5, color=color)
ax2.bar(future_years_num_ratings.flatten(), predicted_num_ratings.flatten(), alpha=0.5, color='orange')
ax2.tick_params(axis='y', labelcolor=color)

# Display the plot
plt.title('Average Rating and Number of Ratings for Subway Over the Years with Predictions')
plt.show()
