import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_tweet_frequency(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date
    plt.figure(figsize=(10, 6))
    sns.countplot(x='date', data=df)
    plt.xticks(rotation=45)
    plt.title('Tweet Frequency Over Time')
    plt.show()


def generate_report(df):
    report = {
        'Total Tweet': len(df),
        'Most Frequent User': df['user'].value_counts().idxmax(),
        'Most Frequent Words': pd.Series(' '.join(df['text']).split()).value_counts().head(10)
    }
    return report
