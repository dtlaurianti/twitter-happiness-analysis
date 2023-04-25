import pandas as pd
import numpy as np


def getScore(tweet, wordHappinessDF):
    if type(tweet) != str or len(tweet) == 0:
        return np.nan

    tweet_words = pd.Series(list(set(tweet)))
    tweet_word_counts = tweet_words.apply(lambda x: tweet.count(x))

    word_scores = wordHappinessDF.merge(
        tweet_words.rename("word"), on="word", how="inner"
    ).set_index("word")["happiness_average"]
    scores = tweet_words.map(word_scores).fillna(0)

    sum_of_scores = (scores * tweet_word_counts).sum()
    total_words = len(tweet)

    return sum_of_scores / total_words
