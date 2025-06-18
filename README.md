# 🍽️✨ Analisis Sentimen & Popularitas Restoran Bandar Lampung dengan NLP & Data Science

Selamat datang di proyek eksplorasi data dan sentimen review restoran-restoran populer di Bandar Lampung!  
Proyek ini menggabungkan kekuatan data science, NLP, dan visualisasi untuk mengungkap insight menarik dari ribuan ulasan pelanggan Google Maps.  
Temukan restoran terfavorit, tren sentimen, hingga kata-kata yang sering muncul dalam review pelanggan! 🚀

---

## 🚦 Alur Project

1. **📥 Pengumpulan Data**  
   Scraping review Google Maps dari berbagai restoran di Bandar Lampung.

2. **🧹 Preprocessing Data**  
   Gabung, bersihkan, dan siapkan data untuk analisis lebih lanjut.

3. **📈 Analisis Popularitas**  
   Hitung dan visualisasikan restoran terpopuler berdasarkan jumlah review.

4. **🤖 Analisis Sentimen Otomatis**

   - Berdasarkan rating bintang ⭐
   - Berdasarkan isi ulasan dengan NLP (transformers IndoBERT)

5. **📊 Visualisasi & Insight**  
   Visualisasi data di Tableau untuk menemukan insight bisnis dan tren sentimen.

---

## 🗂️ Struktur Folder

```
├── data/
│   ├── raw/
│   ├── processed/
├── notebooks/
│   ├── Pre_Processing_Data.ipynb
│   ├── AnalisisSentimen/
│   ├── AnalisisPopularitas/
├── src/
├── requirements.txt
├── README.md
```

---

## 🛠️ Cara Menjalankan

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
2. **Preprocessing Data**
   - Jalankan script di folder `src/` dan notebook preprocessing.
3. **Analisis Sentimen**
   - Jalankan script di `notebooks/AnalisisSentimen/`.
4. **Visualisasi**
   - Import hasil analisis ke Tableau atau tools lain untuk eksplorasi insight.

---

## 🌟 Output & Insight

- **Restoran terpopuler** di Bandar Lampung berdasarkan jumlah review.
- **Distribusi sentimen** (positif, netral, negatif) per restoran.
- **Tren sentimen** dari waktu ke waktu.
- **Kata kunci** yang sering muncul di review positif/negatif.
- **Perbandingan rating layanan, makanan, suasana** antar restoran.

---

## 💡 Contoh Pertanyaan yang Bisa Dijawab

- Restoran mana yang paling banyak mendapat review positif?
- Apa keluhan utama pelanggan di restoran tertentu?
- Bagaimana tren sentimen pelanggan selama setahun terakhir?
- Apa kata-kata yang sering muncul di review negatif?

---

## 📄 Lisensi

Project ini untuk keperluan edukasi dan riset. Data review diambil dari Google Maps.

---

## 🙋‍♂️ Identitas

**Nama:** Arya Setia Pratama  
**Email:** aryasetiap.code@gmail.com  
**WhatsApp:** 0856-6964-4533  
**Universitas:** Universitas Lampung  
**Tahun:** 2025

---

Terima kasih telah mengunjungi proyek ini! 🎉  
Jangan ragu untuk menghubungi saya untuk diskusi atau kolaborasi lebih lanjut!
