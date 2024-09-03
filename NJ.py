import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
reviews_df = pd.read_csv('C:/Users/Patrick/Downloads/reviews.csv')
restaurants_df = pd.read_csv('C:/Users/Patrick/Downloads/restaurants.csv')

# Merge the two datasets on the common column 'business_id'
merged_df = pd.merge(reviews_df, restaurants_df, on='business_id', how='inner')

# Filter data to include only "Subway" restaurants in the state of NJ
subway_df_nj = merged_df[(merged_df['name'] == 'Subway') & (merged_df['state'] == 'NJ')]

# Convert the 'date' column to datetime format using pandas
subway_df_nj['date'] = pd.to_datetime(subway_df_nj['date'])

# Extract the year from the date using Pandas
subway_df_nj['year'] = subway_df_nj['date'].dt.year

# Calculate average rating and number of ratings per year
avg_rating_per_year = subway_df_nj.groupby('year')['stars'].mean()
num_ratings_per_year = subway_df_nj.groupby('year').size()

# Create a subplot with two y-axes
fig, ax1 = plt.subplots()

# Plot average rating on the primary y-axis
color = 'red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Rating', color=color)
ax1.plot(avg_rating_per_year.index, avg_rating_per_year, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a secondary y-axis to plot the number of ratings
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Number of Ratings', color=color)
ax2.bar(num_ratings_per_year.index, num_ratings_per_year, alpha=0.5, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Show the plot
plt.title('Average Rating and Number of Ratings for NJ Subway Over the Years')
plt.show()


