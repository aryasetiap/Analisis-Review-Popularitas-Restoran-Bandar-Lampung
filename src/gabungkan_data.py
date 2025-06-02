import pandas as pd
import glob
import os

folder_path = os.path.join('data', 'raw')
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

df_list = []
for f in all_files:
    try:
        df = pd.read_csv(f)
        df_list.append(df)
    except Exception as e:
        print(f"Gagal membaca {f}: {e}")

# Gabungkan semua file, kolom yang tidak ada akan otomatis diisi NaN
df = pd.concat(df_list, ignore_index=True, join='outer')

# Simpan hasil gabungan
output_path = os.path.join('data', 'data_gabungan.csv')
df.to_csv(output_path, index=False)

print(f"Berhasil menggabungkan {len(all_files)} file menjadi {output_path}")