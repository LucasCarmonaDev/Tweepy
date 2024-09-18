import os
from auth import authenticate_twitter_app
from data_collection import fetch_tweets, tweets_to_dataframe
from processing import plot_tweet_frequency, generate_report


def main():
    # Autenticação
    api = authenticate_twitter_app()

    # Coleta de dados
    query = "Python"
    tweets = fetch_tweets(api, query)

    # Processamento de dados
    df = tweets_to_dataframe(tweets)
    plot_tweet_frequency(df)
    report = generate_report(df)

    print("Report:", report)


if __name__ == "__main__":
    main()
