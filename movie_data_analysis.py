import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

movie_data = pd.read_csv("movies.csv")

genre_counts = movie_data['Genre'].value_counts()

plt.figure(figsize=(12, 6))
genre_counts.plot(kind='bar', color='purple')
plt.title("Movie Genres Distribution")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

titles_text = " ".join(movie_data['Title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Movie Titles")
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(movie_data['Rating'], bins=10, kde=True, color='green')
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

top_rated_movies = movie_data.sort_values(by='Rating', ascending=False).head(10)
print("Top 10 Movies by Ratings:")
print(top_rated_movies[['Title', 'Rating']])
