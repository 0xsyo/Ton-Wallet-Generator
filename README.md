# Ton Wallet Generator

Ton Wallet Generator adalah alat untuk menghasilkan dompet TON secara otomatis menggunakan Python. Alat ini memungkinkan Anda untuk membuat beberapa dompet TON dan menyimpan informasi penting seperti alamat, kunci privat, dan mnemonik ke dalam file teks.

## Fitur
- **Buat Dompet**: Menghasilkan dompet TON baru sesuai jumlah yang diinginkan.
- **Simpan Informasi**: Menyimpan alamat, kunci privat, dan mnemonik ke dalam file `wallets.txt`.
- **Progress Bar**: Menampilkan progress bar saat dompet sedang dibuat untuk memberikan umpan balik kepada pengguna.

## Persyaratan
- **Python 3.7+**
- **tqdm**
- **colorama**
- **tonsdk**

## Instalasi
1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/0xsyo/Ton-Wallet-Generator.git
   cd Ton-Wallet-Generator

2. **Instal semua dependensi yang diperlukan:**
   ```bash
   pip install tqdm colorama tonsdk

3. **Jalankan program :**
   ```bash
   python main.py

4. **Jalankan program :**
   ```bash
   python3 main.py

## Penggunaan
Setelah Anda menjalankan program, Anda akan diminta untuk memasukkan jumlah wallet yang ingin dibuat. Berikut adalah langkah-langkahnya:

**Masukkan jumlah wallet:** Ketika program meminta, masukkan angka sesuai jumlah wallet yang ingin Anda buat.

Informasi yang dihasilkan: Program akan menghasilkan wallet sesuai dengan jumlah yang Anda masukkan dan menyimpannya dalam file wallets.txt.

**File wallets.txt:** Buka file ini untuk melihat alamat, kunci privat, dan mnemonik dari wallet yang telah dibuat.

## Catatan
**Keamanan:** Jaga kerahasiaan informasi wallet Anda, terutama kunci privat dan mnemonik. Jangan membagikannya kepada orang lain.
Hentikan Program: Jika Anda ingin menghentikan program, gunakan Ctrl + C di terminal.   
