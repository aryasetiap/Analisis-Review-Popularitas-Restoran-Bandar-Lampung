from transformers import pipeline
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('data/processed/data_untuk_analisis_sentimen.csv')

model_name = "w11wo/indonesian-roberta-base-sentiment-classifier"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

label_map = {
    "negative": "negatif",
    "neutral": "netral",
    "positive": "positif"
}

texts = df['isi_review'].fillna("").astype(str).tolist()
results = []
batch_size = 16

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i+batch_size]
    # Tidak perlu tokenisasi manual!
    batch_results = sentiment_pipeline(batch, batch_size=batch_size, truncation=True, max_length=512)
    for res in batch_results:
        results.append(label_map.get(res['label'], "netral"))

df['sentimen_nlp'] = results
df.to_csv('data/processed/data_analisis_sentimen_label_ulasan.csv', index=False)
print("Label sentimen Ulasan selesai dan disimpan.")
print(df['sentimen_nlp'].value_counts())