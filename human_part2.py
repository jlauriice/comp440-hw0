"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all
import pandas as pd

def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")
    # Merge ratings and movies to get titles
    merged = ratings_df.merge(movies_df, on='movie_id')
    
    # Calculate count, mean, and standard deviation (std) for each movie
    stats = merged.groupby(['movie_id', 'title'])['rating'].agg(['count', 'mean', 'std']).reset_index()
    
    # Filter for movies with at least 100 ratings to ensure popularity
    eligible = stats[stats['count'] >= 100].copy()
    
    # Apply consensus rule: Score = Mean - Standard Deviation
    eligible['consensus_score'] = eligible['mean'] - eligible['std']
    
    # Sort by the new consensus score
    top10 = eligible.sort_values(by='consensus_score', ascending=False).head(10)
    
    # Print the requested columns (plus std and score so you can see the math working!)
    print(top10[['movie_id', 'title', 'count', 'mean', 'std', 'consensus_score']].to_string(index=False))


def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
