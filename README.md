

### 📄 `README.md`

````markdown
# 🐠 Dashboard Penjualan Ikan Hias

Dashboard ini dibuat menggunakan **Streamlit** untuk menampilkan hasil analisis data penjualan ikan hias. Data yang digunakan telah melalui proses data wrangling dan exploratory data analysis (EDA), lalu divisualisasikan secara interaktif.

## 📁 Dataset

Dataset yang digunakan merupakan hasil gabungan dari data produk dan data penjualan ikan hias, dan telah disimpan dalam file: `all_df.csv`.

Struktur kolom utama:
- `product_id`, `product_name`, `category`, `price`, `supplier`, `rating`
- `transaction_id`, `customer_name`, `quantity`, `total_price`, `date`, `payment_method`, `location`

## 🚀 Fitur Dashboard

- Filter data berdasarkan kategori ikan dan kota
- Statistik penjualan (total transaksi, pendapatan, pelanggan unik)
- Visualisasi:
  - Produk terlaris
  - Pendapatan per kategori
  - Tren penjualan bulanan (berdasarkan kota)
- Preview data mentah

## 🛠️ Cara Menjalankan (Secara Lokal)

### 1. Clone repository

```bash
git clone https://github.com/username/dashboard-ikan-hias.git
cd dashboard-ikan-hias
````

### 2. Install dependencies (disarankan gunakan virtual environment)

```bash
pip install streamlit pandas matplotlib
```

### 3. Jalankan dashboard

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka di browser default di `http://localhost:8501`.

## 🌐 Jalankan di Streamlit Cloud (Opsional)

Jika kamu ingin menjalankannya online:

1. Fork atau clone repo ini ke akun GitHub kamu
2. Buka [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Klik “New app”, lalu arahkan ke `dashboard.py` dalam repo kamu

## 🌐 Akses Online

Kamu dapat mengakses dashboard secara langsung melalui link berikut:

👉 [Buka Dashboard](https://dashboard-ikan-hias-dilanurlaila.streamlit.app/)

## 👤 Author

Dibuat oleh \[Dila Nurlaila] sebagai bagian dari pembelajaran mata kuliah **Analisis Bisnis dan Big Data**.

```

---
