import pandas as pd
import numpy as np

# Load the dataset using a raw string to handle Windows file path
df = pd.read_csv(r"netflix_data.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['type', 'country', 'release_year'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 1. Total Movies and TV Shows
type_counts = df['type'].value_counts()
print("\n🎬 Content Type Distribution:\n", type_counts)

# 2. Top 5 Countries by Content
top_countries = df['country'].value_counts().head(5)
print("\n🌍 Top Countries by Content:\n", top_countries)

# 3. Most Common Genres
genres = df['listed_in'].str.split(',', expand=True).stack().str.strip().value_counts().head(5)
print("\n📚 Top Genres:\n", genres)

# 4. Yearly Content Count
content_per_year = df.groupby('release_year')['show_id'].count().tail(10)
print("\n📅 Content Released per Year (last 10 years):\n", content_per_year)

# 5. Average Duration (Movies only)
movies = df[df['type'] == 'Movie']
movies['duration_min'] = movies['duration'].str.extract('(\d+)').astype(float)
avg_duration = np.mean(movies['duration_min'])
print(f"\n⏱️ Average Movie Duration: {avg_duration:.2f} minutes")
