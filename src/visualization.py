import matplotlib.pyplot as plt
import pandas as pd

def plot_review_distribution(data):
    plt.figure(figsize=(10, 6))
    data['rating'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title('Distribution of Restaurant Ratings')
    plt.xlabel('Ratings')
    plt.ylabel('Number of Reviews')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_average_rating_per_restaurant(data):
    avg_ratings = data.groupby('restaurant_name')['rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 8))
    avg_ratings.plot(kind='bar', color='lightgreen')
    plt.title('Average Rating per Restaurant')
    plt.xlabel('Restaurant Name')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_sentiment_analysis(sentiment_data):
    plt.figure(figsize=(10, 6))
    sentiment_data['sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Sentiment Analysis of Reviews')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()