import pandas as pd

# Baca data
df = pd.read_csv('data/data_gabungan.csv')

# Semua kolom yang ingin dipertahankan
kolom_dipertahankan = [
    # Kolom Identitas & Lokasi
    'address',
    'city',
    'state',
    'postalCode',
    'street',
    'location/lat',
    'location/lng',

    # Kolom Identitas Tempat
    'cid', 'fid', 'placeId',
    'name',
    'url',
    
    # Kolom Status Tempat
    'permanentlyClosed',
    'temporarilyClosed',
    
    # Kolom Review & Reviewer
    'reviewId',
    'reviewerId',
    'reviewerUrl',
    'reviewerNumberOfReviews',
    
    # Kolom Review Detail
    'text',
    'textTranslated',
    'language',
    'originalLanguage',
    'translatedLanguage',
    'rating',
    'totalScore',
    'likesCount',
    'visitedIn',
    'publishAt',
    'publishedAtDate',
    'scrapedAt',
    'responseFromOwnerText',
    'responseFromOwnerDate', 
    
    # Kolom Review Detailed Rating (Penilaian Detail)
    'reviewDetailedRating/Layanan',
    'reviewDetailedRating/Makanan',
    'reviewDetailedRating/Suasana',
]

# Filter dataframe hanya dengan kolom yang dipertahankan
df_bersih = df[kolom_dipertahankan]

print(f"Jumlah kolom sebelum: {len(df.columns)}")
print(f"Jumlah kolom setelah: {len(df_bersih.columns)}")
print("Berhasil menghapus kolom yang tidak diperlukan.")
# Simpan hasil
df_bersih.to_csv('data/data_untuk_preprocessing.csv', index=False)
print("Data telah disimpan ke 'data/data_untuk_preprocessing.csv'")