import pandas as pd

# Baca data
df = pd.read_csv('data/data_gabungan.csv')

# Semua kolom yang ingin dipertahankan (urutan sesuai keinginan)
kolom_dipertahankan = [
    'title',
    'address',
    'url',
    'reviewId',
    'stars',
    'name',
    'reviewUrl',
    'text',
    'publishedAtDate',
    'reviewDetailedRating/Layanan',
    'reviewDetailedRating/Makanan',
    'reviewDetailedRating/Suasana'
]

# Pastikan urutan kolom sesuai dengan list kolom_dipertahankan
df_bersih = df.loc[:, kolom_dipertahankan]

print(f"Jumlah kolom sebelum: {len(df.columns)}")
print(f"Jumlah kolom setelah: {len(df_bersih.columns)}")
print("Berhasil menghapus kolom yang tidak diperlukan.")

# Simpan hasil
df_bersih.to_csv('data/data_untuk_preprocessing.csv', index=False)
print("Data telah disimpan ke 'data/data_untuk_preprocessing.csv'")