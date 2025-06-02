# Analisis Review dan Popularitas Restoran/Kuliner di Bandar Lampung

## Overview
Proyek ini bertujuan untuk menganalisis ulasan dan popularitas restoran serta kuliner di Bandar Lampung menggunakan data yang diambil dari Google Maps. Dengan menggunakan teknik analisis data dan visualisasi, proyek ini bertujuan untuk memberikan wawasan yang lebih baik tentang preferensi konsumen dan tren dalam industri kuliner di daerah tersebut.

## Struktur Proyek
- **data/raw**: Berisi file data mentah yang dikumpulkan dari Google Maps, termasuk ulasan, penilaian, dan informasi relevan lainnya tentang restoran di Bandar Lampung.
- **data/processed**: Berisi file data yang telah diproses dan dibersihkan untuk analisis lebih lanjut.
- **notebooks/exploratory_analysis.ipynb**: Jupyter notebook untuk analisis eksploratori data, termasuk kode dan visualisasi untuk memahami data dan mengidentifikasi tren.
- **src/data_preprocessing.py**: File ini berisi fungsi dan kelas untuk preprocessing data, termasuk metode untuk memuat data mentah, membersihkannya, dan menyimpan data yang telah diproses.
- **src/analysis.py**: File ini berisi fungsi untuk menganalisis data yang telah diproses, termasuk analisis statistik, analisis sentimen dari ulasan, dan metode untuk menghitung metrik popularitas.
- **src/visualization.py**: File ini berisi fungsi untuk memvisualisasikan hasil analisis, termasuk plot dan grafik untuk merepresentasikan temuan dari analisis.
- **requirements.txt**: File ini mencantumkan ketergantungan Python yang diperlukan untuk proyek, termasuk pustaka seperti pandas, numpy, matplotlib, dan paket lainnya yang diperlukan.

## Setup
1. Clone repositori ini ke mesin lokal Anda.
2. Install semua ketergantungan yang diperlukan dengan menjalankan:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan Jupyter Notebook untuk melakukan analisis eksploratori:
   ```
   jupyter notebook notebooks/exploratory_analysis.ipynb
   ```

## Penggunaan
Setelah semua ketergantungan terinstal, Anda dapat menggunakan skrip di folder `src` untuk melakukan preprocessing data, analisis, dan visualisasi. Pastikan untuk menyesuaikan jalur file sesuai dengan struktur data Anda.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork repositori ini dan kirim pull request dengan perubahan Anda.