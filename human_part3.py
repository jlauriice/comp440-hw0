"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all
import pandas as pd


def top5_my_definition(ratings, ratings_df, movies, movies_df, users, users_df):
    print("== My definition ==")

    # Merge ratings with users to get gender and the titles
    ratings_users = ratings_df.merge(users_df, on='user_id')
    merged = ratings_users.merge(movies_df, on='movie_id')
    
    # Group by movie and gender to calculate the count and mean rating
    stats = merged.groupby(['movie_id', 'title', 'gender'])['rating'].agg(['count', 'mean']).unstack()
    
    # Making column names easier to read
    stats.columns = [f'{col[0]}_{col[1]}' for col in stats.columns]
    stats = stats.reset_index()
    
    # making sample size of 30 or more
    eligible = stats[(stats['count_M'] >= 30) & (stats['count_F'] >= 30)].copy()
    
    # The "Bro-centric" score is how much higher men rated it than women
    eligible['bro_centric_score'] = eligible['mean_M'] - eligible['mean_F']
    
    # Sort by the biggest gap where men liked it more
    top5 = eligible.sort_values(by='bro_centric_score', ascending=False).head(5)
    
    # Results here
    print(top5[['movie_id', 'title', 'mean_M', 'mean_F', 'bro_centric_score']].to_string(index=False))


def human_part3(ratings, ratings_df, movies, movies_df, users, users_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df, users, users_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df, users, users_df)
