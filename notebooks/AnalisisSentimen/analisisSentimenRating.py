import pandas as pd

# Load data hasil preprocessing
df = pd.read_csv('data/processed/data_untuk_analisis_sentimen.csv')

# Fungsi labeling sentimen berdasarkan rating_bintang
def label_sentimen(rating):
    if rating >= 4:
        return 'positif'
    elif rating == 3:
        return 'netral'
    else:
        return 'negatif'

# Terapkan fungsi ke kolom baru
df['sentimen'] = df['rating_bintang'].apply(label_sentimen)

# Cek hasil
print(df[['rating_bintang', 'isi_review', 'sentimen']].head())

# Simpan hasil ke file baru
df.to_csv('data/processed/data_analisis_sentimen_label_rating.csv', index=False)
print("Label sentimen berdasarkan rating selesai dan disimpan.")

# Ringkasan jumlah sentimen
print(df['sentimen'].value_counts())

# Ringkasan per restoran
sentimen_per_tempat = df.groupby('nama_tempat')['sentimen'].value_counts().unstack(fill_value=0)
print(sentimen_per_tempat)