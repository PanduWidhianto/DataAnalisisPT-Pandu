import matplotlib.pyplot as plt

# Data
produk = ["Produk A", "Produk B", "Produk C", "Produk D", "Produk E"]
jumlah_terjual = [100, 150, 200, 120, 80]
harga_satuan = [50000, 75000, 30000, 60000, 90000]
biaya_produksi = [3000000, 7500000, 4000000, 4800000, 5600000]

# Total Pendapatan
total_pendapatan = [a * b for a, b in zip(jumlah_terjual, harga_satuan)]

# Laba Kotor
laba_kotor = [a - b for a, b in zip(total_pendapatan, biaya_produksi)]

# Grafik Total Pendapatan Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, total_pendapatan, color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel('Produk')
plt.ylabel('Total Pendapatan (Rp)')
plt.title('Total Pendapatan Per Produk')
plt.show()

# Grafik Total Biaya Produksi Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, biaya_produksi, color=['cyan', 'magenta', 'yellow', 'lime', 'pink'])
plt.xlabel('Produk')
plt.ylabel('Total Biaya Produksi (Rp)')
plt.title('Total Biaya Produksi Per Produk')
plt.show()

# Grafik Laba Kotor Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, laba_kotor, color=['darkblue', 'darkred', 'darkgreen', 'darkorange', 'purple'])
plt.xlabel('Produk')
plt.ylabel('Laba Kotor (Rp)')
plt.title('Laba Kotor Per Produk')
plt.show()

# Laporan Keuangan dengan warna berbeda
pendapatan = sum(total_pendapatan)
total_biaya_produksi = sum(biaya_produksi)
laba_kotor_total = sum(laba_kotor)
biaya_operasional = 5000000
laba_bersih = laba_kotor_total - biaya_operasional

# Data untuk pie chart
labels = ['Pendapatan', 'Biaya Produksi', 'Laba Kotor', 'Biaya Operasional', 'Laba Bersih']
sizes = [pendapatan, total_biaya_produksi, laba_kotor_total, biaya_operasional, laba_bersih]
colors = ['blue', 'green', 'orange', 'red', 'purple']

# Grafik Pie Chart dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Laporan Keuangan')
plt.show()

import pandas as pd

# Data Tabel Pembelian
data_pembelian = {
    "No": [1, 2, 3, 4, 5],
    "Produk": ["Produk A", "Produk B", "Produk C", "Produk D", "Produk E"],
    "Jumlah Dibeli": [120, 180, 220, 150, 100],
    "Harga Pembelian Satuan": ["Rp 25.000", "Rp 50.000", "Rp 20.000", "Rp 40.000", "Rp 56.000"],
    "Total Biaya Pembelian": ["Rp 3.000.000", "Rp 9.000.000", "Rp 4.400.000", "Rp 6.000.000", "Rp 5.600.000"],
    "Tanggal Pembelian": ["25/04/2024", "25/04/2024", "26/04/2024", "27/04/2024", "27/04/2024"]
}

# Membuat DataFrame
df_pembelian = pd.DataFrame(data_pembelian)

# Menyimpan DataFrame ke file CSV
csv_file_path = 'tabel_pembelian.csv'
df_pembelian.to_csv(csv_file_path, index=False)

print(f'File CSV telah disimpan di: {csv_file_path}')
