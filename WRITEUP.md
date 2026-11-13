# HW0 writeup

**Name:** Laurice Jimu
**Date:** 2026-09-17

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

There are 100,000 ratings, with 1,682 movies and 962 users. Across 1 to 5 stars, the ratings follow a bell curve shape that leans heavily towards higher ratings with 4 stars being most common followed by 3 stars then 5 stars. 

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

65 is the median, and there are 364 users who rated 100 or more. 

**(c) Which 10 movies have the most ratings?**

Star Wars (1977)                 583
Contact (1997)                   509
Fargo (1996)                     508
Return of the Jedi (1983)        507
Liar Liar (1997)                 485
English Patient, The (1996)      481
Scream (1996)                    478
Toy Story (1995)                 452
Air Force One (1997)             431
Independence Day (ID4) (1996)    429

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

Top 10 highest-rated movies (min 20 ratings):
                                                        mean  count
title                                                              
Close Shave, A (1995)                               4.491071    112
Schindler's List (1993)                             4.466443    298
Wrong Trousers, The (1993)                          4.466102    118
Casablanca (1942)                                   4.456790    243
Wallace & Gromit: The Best of Aardman Animation...  4.447761     67
Shawshank Redemption, The (1994)                    4.445230    283
Rear Window (1954)                                  4.387560    209
Usual Suspects, The (1995)                          4.385768    267
Star Wars (1977)                                    4.358491    583
12 Angry Men (1957)                                 4.344000    125

**Anything you got stuck on (what you tried, where it broke), or "none":**

None

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** A movie must have at least 100 ratings to prove some level of broad popularity firstly. Then among those that remain, a consensus score is calculated by subtracting the ratings' standard deviation from it's mean. 

**One rule I considered and rejected, and why:** Pure highest rating, I rejected this because it results in a top 10 list filled with unkown movies that have exactly one 5-star rating. 

**Top 10 under my rule:**

1. Casablanca (1942)

2. Close Shave, A (1995)

3. Shawshank Redemption, The (1994)

4. Rear Window (1954)

5. Wrong Trousers, The (1993)

6. Schindler's List (1993)

7. 12 Angry Men (1957)

8. North by Northwest (1959)

9. Vertigo (1958)

10. Usual Suspects, The (1995)

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

I chose this rule because a truly great movie shouldn't just have a high average but it needs to be widely seen and consistently loved by everyone who watches it, without dividing its audience.

What it gains: It finds movies that are both universally acclaimed and universally agreed upon. By subtracting the standard deviation, the rule actively penalizes polarizing "love it or hate it" films. A movie only reaches the top if a large audience watched it and consistently agreed that it was excellent, removing controversial outliers.

What it costs: Standard deviation penalizes any spread in the data. A movie with a mix of 4-star and 5-star ratings has a higher variance than a movie where everyone gave it exactly 4 stars. This means our rule might unfairly rank a universally "good" movie slightly above a "great but occasionally just good" movie. The 100-rating threshold also still ignores universally loved hidden gems.

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** Bro-Centric

**My definition** (one sentence, precise enough that a classmate could code it)**:** Among movies rated by at least 30 men and 30 women, it is the movie with the largest positive difference between the average rating given by men and the average rating given by women.

**One definition I considered and rejected, and why:** I considered defining it as the movie with the highest overall percentage of male raters. I rejected this because it heavily skews toward obscure movies that only have one or two total ratings (which just happen to be from men), rather than capturing culturally relevant movies that specifically appeal to men significantly more than women.

**Top 5 under my definition:**

1. Reservoir Dogs
2. Bridge on the River Kwai, The
3. 2001: A Space Odyssey
4. Ben-Hur
5. Clockwork Orange, A

**What your definition captures, what it misses, and where "Bro-centric-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

This definition is able to capture the demographic divide: it identifies movies that resonate deeply with male audiences but actively fail to connect with female viewers. However, it misses universally acclaimed "guy movies." If men rate a classic action movie a 5, but women also enjoy it and rate it a 4, the gap is small. So my rule penalizes these universally liked films in favor of divisive ones.

In this dataset, "bro-centric-ness" lives entirely in what the crowd did,specifically, the statistical gap between demographic cohorts. It isn't found just by looking at genre tags like "Action" or "War," because many action movies have broad, universal appeal. Instead, the true measure of a bro-centric film here is found in polarization: it requires male passion and female indifference happening simultaneously.

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

Yes, they match perfectly.

## Part 5. Comparing the best movie

**Claude's rule:**

A Bayesian-adjusted average that shrinks each movie's raw mean toward the global mean (3.530) in proportion to how few ratings it has, using a weight factor of m = 20.

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

Claude does not admit this was a subjective choice; it presents its methodology as an objective or rather factual definition of quality. The sentence that decides this is: "A raw mean over a handful of ratings is noisy (a single 5-star rating gives a 'perfect' 5.0 average), so 'best' should reward movies that are both highly rated and rated by a lot of people." It uses the word "should" to state its opinion as an absolute rule.

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

They differ because we penalize different things. Claude’s Bayesian rule penalizes a lack of ratings. For example, Claude ranks Schindler’s List as #1 because its massive rating count (298) easily overcomes the Bayesian penalty, while it pushes A Close Shave down to #4 because it only has 112 ratings. My rule (Consensus Score) penalizes polarization (standard deviation). My rule pushes Casablanca and A Close Shave to the very top because their low standard deviations prove universal agreement, regardless of whether they have 100 ratings or 300.

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

My rule would be better if say I was organizing a movie night with a diverse friend group because it actively filters out polarizing movies and only picks the universally agreed upon gems. 

Claude’s Bayesian rule is better for a global recommendation engine like IMDb's top list. They probably want high statistical confidence that a movie is historically great before recommending it to millions.

Ultimately, neither is objectively better. They just serve different purposes: mine minimizes risk, while Claude's maximizes statistical confidence.

## Part 6. Comparing the most Bro-Centric movie

**Claude's definition:**

A movie with at least 50 total ratings that has the highest percentage of male raters.

**Is Claude's film in your top 5?**

No, and its actually mathematically impossible for Claude's #1 film (Kids in the Hall: Brain Candy) to be in my top 5 because it had only 7 female raters (89.2% of its 65 raters are male based off the output) . My rule at least 30 ratings from men and 30 ratings from women to calculate a fair comparison. 

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

Claude’s definition captures audience composition. It sees movies that naturally attract a male demographic while failing to attract a female audience which is exactly the rule I considered and rejected in Part 3. However, its blind spot is reception: a movie might be watched by 90% men, but the few women who do watch it might rate it just as highly as the men do.

My definition captures gendered reception. It sees movies where both men and women watched the film, but men loved it while women disliked it. My blind spot is extreme demographic skew: because I require at least 30 female ratings for a reliable baseline, that filters out hyper-niche "bro-centric" movies that almost no women watched in the first place.

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

I mostly asked about where I was in comparison to what I was supposed to be doing. And asked questions to help orient me on how to go about the exercise.

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

None really, it told me I hadn't completed some of the tasks because there were still some placeholder texts in the writeup and that was correct. 

**What you would do differently next time, in 3–5 sentences:**

I would read the READ.Me more thoroughly. I would also ask Claude for an overall bird's eye view of what's required of me. This is to help my orientation of the task as a whole.

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

Just the switching between where I need to code and where I need to write but once I got the hang of that it became easy.

**Hours spent:** 7 to 8

**Anyone who helped you, or "no one":** Shilad by allowing me to hand this in late, giving me the space and time to actually put energy and effort into it. Thank you so much!
