import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("movies.csv")
    print("CSV file loaded successfully ✅")
except Exception as e:
    print("Reason:", e)
    print("Using sample dataset instead ✅")

    data = {
        "Movie": ["Inception", "Titanic", "Avatar", "Interstellar", "Joker",
                  "Avengers", "Gladiator", "Up", "Coco", "Parasite"],
        "Genre": ["Sci-Fi", "Romance", "Sci-Fi", "Sci-Fi", "Drama",
                  "Action", "Action", "Animation", "Animation", "Thriller"],
        "Rating": [8.8, 7.8, 7.9, 8.6, 8.5, 8.0, 8.5, 8.3, 8.4, 8.6]
    }
    df = pd.DataFrame(data)

print("\n----- DATASET (First 10 Rows) -----")
print(df.head(10))

print("\n----- DATASET INFO -----")
df.info()

df.drop_duplicates(inplace=True)

print("\n----- MISSING VALUES BEFORE CLEANING -----")
print(df.isnull().sum())

if "Rating" in df.columns:
    df["Rating"].fillna(df["Rating"].mean(), inplace=True)

if "Movie" in df.columns and "Genre" in df.columns:
    df.dropna(subset=["Movie", "Genre"], inplace=True)

print("\n----- MISSING VALUES AFTER CLEANING -----")
print(df.isnull().sum())

mean_rating = df["Rating"].mean()
median_rating = df["Rating"].median()
mode_rating = df["Rating"].mode()[0]

print("\n----- SUMMARY STATISTICS -----")
print("Mean Rating   :", round(mean_rating, 2))
print("Median Rating :", median_rating)
print("Mode Rating   :", mode_rating)

plt.figure(figsize=(7, 5))
plt.hist(df["Rating"], bins=10)
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Rating"])
plt.title("Box Plot of Movie Ratings")
plt.show()

top_movies = df.sort_values(by="Rating", ascending=False).head(10)

print("\n----- TOP 10 RATED MOVIES -----")
print(top_movies[["Movie", "Genre", "Rating"]])

genre_ratings = df.groupby("Genre")["Rating"].mean().sort_values(ascending=False)
print("\n----- TOP RATED GENRES -----")
print(genre_ratings)

plt.figure(figsize=(8, 5))
genre_ratings.head(10).plot(kind="bar")
plt.title("Top Rated Genres")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(df["Rating"], bins=10)
plt.title("Rating Distribution")

plt.subplot(2, 2, 2)
sns.boxplot(x=df["Rating"])
plt.title("Rating Spread")

plt.subplot(2, 2, 3)
genre_ratings.head(5).plot(kind="bar")
plt.title("Top Genres")

plt.subplot(2, 2, 4)
df["Genre"].value_counts().head(5).plot(kind="bar")
plt.title("Most Common Genres")

plt.tight_layout()
plt.show()
