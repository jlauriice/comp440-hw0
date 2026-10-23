"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all
import pandas as pd

def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):


    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    num_ratings = len(ratings_df)
    num_users = ratings_df["user_id"].nunique()
    num_movies = movies_df["movie_id"].nunique()
    print(num_ratings)
    print("== (b) ==")

    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    user_counts = ratings_df['user_id'].value_counts()
    print(f"Median ratings per user: {user_counts.median()}")
    print(f"Users with 100 or more ratings: {(user_counts >= 100).sum()}")

    print("== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?
    merged = ratings_df.merge(movies_df, on='movie_id')
    print("Top 10 movies by rating count:")
    print(merged['title'].value_counts().head(10))

    print("== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.
    stats = merged.groupby('title')['rating'].agg(['mean', 'count'])
    print("Top 10 highest-rated movies (min 20 ratings):")
    print(stats[stats['count'] >= 20].sort_values('mean', ascending=False).head(10))

if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
