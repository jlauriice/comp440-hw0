"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import load_all


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()

    # ------------------------------------------------------------------
    # 1(a) Basic counts and the distribution of ratings across 1-5 stars.
    # ------------------------------------------------------------------
    print("=" * 70)
    print("1(a) Basic rating statistics")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = users_df["user_id"].nunique()
    n_movies = movies_df["movie_id"].nunique()
    print(f"{n_ratings:,} ratings, {n_users:,} users, {n_movies:,} movies")

    star_counts = ratings_df["rating"].value_counts().sort_index()
    print("\nRating distribution (1-5 stars):")
    for stars, count in star_counts.items():
        pct = 100 * count / n_ratings
        print(f"  {stars} stars: {count:>6,} ({pct:5.1f}%)")

    # ------------------------------------------------------------------
    # 1(b) Median ratings per user, and how many users have >= 100.
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    ratings_per_user = ratings_df.groupby("user_id").size()
    median_per_user = ratings_per_user.median()
    n_prolific = (ratings_per_user >= 100).sum()
    print(f"Median ratings per user: {median_per_user:.1f}")
    print(f"Users with >= 100 ratings: {n_prolific:,} (out of {n_users:,})")

    # ------------------------------------------------------------------
    # 1(c) Join ratings to titles; the 10 movies with the most ratings.
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("1(c) Top 10 most-rated movies")
    print("=" * 70)
    joined = ratings_df.merge(movies_df[["movie_id", "title"]], on="movie_id")
    most_rated = joined.groupby("title").size().sort_values(ascending=False).head(10)
    for title, count in most_rated.items():
        print(f"  {count:>4} ratings  -  {title}")

    # ------------------------------------------------------------------
    # 1(d) Among movies with >= 20 ratings, the 10 with the highest mean.
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("1(d) Top 10 highest-rated movies (>= 20 ratings)")
    print("=" * 70)
    stats = joined.groupby("title")["rating"].agg(mean="mean", count="count")
    top_mean = stats[stats["count"] >= 20].sort_values("mean", ascending=False).head(10)
    for title, row in top_mean.iterrows():
        print(f"  {row['mean']:.3f} avg  ({row['count']:>3} ratings)  -  {title}")

    # ------------------------------------------------------------------
    # 2. What is the best movie in this dataset?
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("2. Best movie in the dataset")
    print("=" * 70)
    print(
        "A raw mean over a handful of ratings is noisy (a single 5-star rating gives a\n"
        "'perfect' 5.0 average), so 'best' should reward movies that are both highly rated\n"
        "and rated by a lot of people. We use a Bayesian-adjusted average that shrinks each\n"
        "movie's mean toward the overall average rating, in proportion to how few ratings\n"
        "it has:\n"
        "\n"
        "    bayesian_mean = (count / (count + m)) * movie_mean + (m / (count + m)) * global_mean\n"
        "\n"
        "with m = 20 (roughly the point at which a movie's own ratings start to dominate\n"
        "the prior)."
    )
    global_mean = ratings_df["rating"].mean()
    m = 20
    stats_all = joined.groupby("title")["rating"].agg(mean="mean", count="count")
    stats_all["bayesian_mean"] = (
        stats_all["count"] / (stats_all["count"] + m) * stats_all["mean"]
        + m / (stats_all["count"] + m) * global_mean
    )
    best = stats_all.sort_values("bayesian_mean", ascending=False).head(10)
    print(f"\nGlobal mean rating: {global_mean:.3f}\n")
    print("Top 10 by Bayesian-adjusted mean:")
    for title, row in best.iterrows():
        print(
            f"  {row['bayesian_mean']:.3f} adjusted  "
            f"({row['mean']:.3f} raw, {row['count']:>3} ratings)  -  {title}"
        )
    best_title = best.index[0]
    print(f"\n==> Best movie: '{best_title}'")

    # ------------------------------------------------------------------
    # 3. Which movie is the most "Bro-centric"?
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("3. Most Bro-centric movie")
    print("=" * 70)
    print(
        "Definition: 'Bro-centric' = a movie whose audience, within this dataset, skews as\n"
        "heavily male as possible. For each movie with at least 50 ratings (to avoid a tiny\n"
        "sample of all-male raters winning by luck), we compute the percentage of its\n"
        "ratings that came from male users. Ties are broken by rating count, then by mean\n"
        "rating, so a bigger and better-loved 'bro movie' wins."
    )
    rated_by = ratings_df.merge(users_df[["user_id", "gender"]], on="user_id")
    rated_by = rated_by.merge(movies_df[["movie_id", "title"]], on="movie_id")

    bro = rated_by.groupby("title").agg(
        n_ratings=("rating", "count"),
        pct_male=("gender", lambda g: 100 * (g == "M").mean()),
        mean_rating=("rating", "mean"),
    )
    bro = bro[bro["n_ratings"] >= 50].sort_values(
        ["pct_male", "n_ratings", "mean_rating"], ascending=False
    )

    print("\nTop 10 most male-skewing movies (>= 50 ratings):")
    top_bro = bro.head(10)
    for title, row in top_bro.iterrows():
        print(
            f"  {row['pct_male']:.1f}% male  ({row['n_ratings']:>3} ratings, "
            f"{row['mean_rating']:.2f} avg)  -  {title}"
        )

    bro_title = top_bro.index[0]
    bro_row = top_bro.iloc[0]
    print(
        f"\n==> Most Bro-centric movie: '{bro_title}' "
        f"({bro_row['pct_male']:.1f}% of its {int(bro_row['n_ratings'])} raters are male)"
    )


if __name__ == "__main__":
    claude_answers()
