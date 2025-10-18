import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv('data/netflix_titles.csv')

# Clean data
df.drop_duplicates(inplace=True)
# Clean and convert date_added column
df['date_added'] = df['date_added'].str.strip()  # Remove leading/trailing spaces
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  # Convert to datetime, set invalid dates to NaT
df['year_added'] = df['date_added'].dt.year

# NumPy usage
movie_durations = df[df['type'] == 'Movie']['duration'].str.extract(r'(\d+)').dropna().astype(int)
average_duration = np.mean(movie_durations)

# Analysis
top_genres = df['listed_in'].str.split(',').explode().value_counts().head(10)
# Rating distribution
rating_counts = df['rating'].value_counts()

# Yearly additions
yearly_counts = df['year_added'].value_counts().sort_index()



# Visualizations
plt.figure(figsize=(10,6))
top_genres.plot(kind='bar', color='skyblue')
plt.title('Top 10 Netflix Genres')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/top_genres_bar_chart.png')
plt.close()

plt.figure(figsize=(10,6))
yearly_counts.plot(kind='line', marker='o', color='green')
plt.title('Netflix Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.savefig('images/yearly_additions_line_chart.png')
plt.close()

plt.figure(figsize=(8,8))
rating_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Rating Distribution')
plt.tight_layout()
plt.savefig('images/rating_distribution_pie_chart.png')
plt.close()

