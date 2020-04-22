# Twiklin
Make Twitter Clean

Twiklin is a program to determine whether a tweet considered as a positive, negative, or neutral tweet.
We use Python programming language with Tweepy API to gather data (tweets from Twitter).
The dataset and tweets are in Bahasa Indonesia and were tweeted between March and April of 2017 (Pemilu Gubernur DKI Jakarta).
Dataset consists of 454 positive tweets and 260 negative tweets.

How it works?
1. Make a classifier using Naive Bayes
2. Gather tweets from Tweepy
3. Clean tweets using NLTK and Sastrawi (such as removing username, symbols, and stopwords)
4. Classify tweets using classifier (by calculating score and applying threshold)
