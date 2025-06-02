import pandas as pd
import os

def load_raw_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df = df.fillna(method='ffill')
    
    # Convert data types if necessary
    # Example: df['rating'] = df['rating'].astype(float)
    
    return df

def save_processed_data(df, output_path):
    df.to_csv(output_path, index=False)

def preprocess_data(raw_file_path, processed_file_path):
    raw_data = load_raw_data(raw_file_path)
    cleaned_data = clean_data(raw_data)
    save_processed_data(cleaned_data, processed_file_path)