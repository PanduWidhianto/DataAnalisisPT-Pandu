import matplotlib.pyplot as plt

# Data untuk Tabel Pembelian
produk = ["Produk A", "Produk B", "Produk C", "Produk D", "Produk E"]
jumlah_dibeli = [120, 180, 220, 150, 100]
harga_pembelian_satuan = [25000, 50000, 20000, 40000, 56000]
total_biaya_pembelian = [jumlah_dibeli[i] * harga_pembelian_satuan[i] for i in range(len(produk))]

# Grafik Total Biaya Pembelian Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, total_biaya_pembelian, color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel('Produk')
plt.ylabel('Total Biaya Pembelian (Rp)')
plt.title('Total Biaya Pembelian Per Produk')
plt.show()

# Grafik Jumlah Dibeli Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, jumlah_dibeli, color=['cyan', 'magenta', 'yellow', 'lime', 'pink'])
plt.xlabel('Produk')
plt.ylabel('Jumlah Dibeli')
plt.title('Jumlah Dibeli Per Produk')
plt.show()

# Grafik Harga Pembelian Satuan Per Produk dengan warna berbeda
plt.figure(figsize=(10, 6))
plt.bar(produk, harga_pembelian_satuan, color=['darkblue', 'darkred', 'darkgreen', 'darkorange', 'purple'])
plt.xlabel('Produk')
plt.ylabel('Harga Pembelian Satuan (Rp)')
plt.title('Harga Pembelian Satuan Per Produk')
plt.show()
