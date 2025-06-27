import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Penjualan Ikan Hias", layout="wide")

all_df = pd.read_csv('all_df.csv')

# ----------------------------
# Sidebar Filter
# ----------------------------
st.sidebar.header("🔎 Filter Data")

# Filter berdasarkan kategori
kategori = st.sidebar.multiselect(
    "Pilih Kategori Ikan",
    options=all_df['category'].unique(),
    default=all_df['category'].unique()
)

# Ganti filtered_df hanya berdasarkan kategori saja
filtered_df = all_df[all_df['category'].isin(kategori)]

# Tambahan: Pilih kota untuk tren
kota_list = all_df['location'].dropna().unique().tolist()
kota_list.sort()
kota_list.insert(0, 'All City')

selected_city = st.sidebar.selectbox("Pilih Kota untuk Melihat Tren Penjualan", kota_list)

if selected_city == 'All City':
    df_tren = filtered_df.copy()
    title = "Semua Kota"
else:
    df_tren = filtered_df[filtered_df['location'] == selected_city]
    title = selected_city

# ----------------------------
# Judul dan Ringkasan
# ----------------------------
st.title("🐠 Dashboard Penjualan Ikan Hias")

col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Transaksi", len(filtered_df))
col2.metric("💰 Total Pendapatan", f"Rp {int(filtered_df['total_price'].sum()):,}")
col3.metric("🧍 Jumlah Pelanggan", filtered_df['customer_name'].nunique())

# ----------------------------
# Produk Terlaris (Bar Chart)
# ----------------------------
st.subheader("🔥 Produk Terlaris")
top_products = (
    filtered_df.groupby('product_name')['quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig1, ax1 = plt.subplots()
top_products.plot(kind='barh', ax=ax1, color='salmon')
ax1.invert_yaxis()
ax1.set_title("Top 10 Produk Paling Laris")
st.pyplot(fig1)

# ----------------------------
# Pendapatan per Kategori
# ----------------------------
st.subheader("💸 Pendapatan per Kategori")
rev_by_cat = filtered_df.groupby('category')['total_price'].sum().sort_values(ascending=False)
st.bar_chart(rev_by_cat)

# ----------------------------
# Tren Penjualan per Bulan (jika ada kolom date)
# ----------------------------
# Buat kolom 'bulan' dari tanggal
df_tren['date'] = pd.to_datetime(df_tren['date'], errors='coerce')
df_tren['bulan'] = df_tren['date'].dt.to_period('M').astype(str)
trend = df_tren.groupby('bulan')['total_price'].sum()

# Visualisasi grafik
fig, ax = plt.subplots()
trend.plot(kind='line', marker='o', ax=ax)
ax.set_title(f"📈 Tren Penjualan Bulanan - {title}")
ax.set_ylabel("Pendapatan")
ax.set_xlabel("Bulan")
ax.grid(True)
st.pyplot(fig)

# ----------------------------
# Dataframe Preview
# ----------------------------
with st.expander("📄 Lihat Data Lengkap"):
    st.dataframe(filtered_df)

