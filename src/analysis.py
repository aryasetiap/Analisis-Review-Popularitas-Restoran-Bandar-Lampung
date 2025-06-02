def load_processed_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def analyze_reviews(data):
    # Example analysis: Calculate average rating
    average_rating = data['rating'].mean()
    return average_rating

def sentiment_analysis(data):
    from textblob import TextBlob
    data['sentiment'] = data['review'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data

def calculate_popularity(data):
    # Example metric: Count of reviews
    popularity = data['review'].count()
    return popularity

def main():
    # Load processed data
    processed_data = load_processed_data('../data/processed/processed_reviews.csv')
    
    # Analyze reviews
    avg_rating = analyze_reviews(processed_data)
    print(f'Average Rating: {avg_rating}')
    
    # Perform sentiment analysis
    processed_data = sentiment_analysis(processed_data)
    
    # Calculate popularity
    popularity = calculate_popularity(processed_data)
    print(f'Popularity (Number of Reviews): {popularity}')

if __name__ == "__main__":
    main()