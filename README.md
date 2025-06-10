# Aplikasi XOR Cipher

**Enkripsi dan Dekripsi Teks Berbasis Operasi XOR dengan Antarmuka GUI**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)


## 📖 Tentang Proyek

Aplikasi **XOR Cipher** adalah alat sederhana untuk melakukan enkripsi dan dekripsi teks menggunakan operasi logika XOR (Exclusive OR). Dibangun dengan Python 3 dan pustaka Tkinter, aplikasi ini menyediakan antarmuka grafis (GUI) yang intuitif untuk mengenkripsi teks menjadi format biner dan mendekripsinya kembali. Proyek ini dikembangkan sebagai bagian dari tugas akhir semester mata kul kuliah Kriptografi di Universitas Bengkulu, dengan fokus pada kesederhanaan dan efisiensi untuk keperluan edukatif serta sistem ringan seperti validasi QR Code atau pengamanan teks sederhana.

### Tujuan
- Mengembangkan algoritma stream cipher XOR yang ringan dan efisien.
- Menyediakan solusi enkripsi simetris untuk data teks dan citra digital.
- Menganalisis performa dan keamanan dibandingkan algoritma seperti AES.

### Target Pengguna
- Mahasiswa yang mempelajari dasar-dasar kriptografi.
- Pengembang pemula yang ingin memahami implementasi stream cipher.
- Pengguna yang membutuhkan alat enkripsi ringan untuk sistem sederhana.

## ✨ Fitur Utama

- **Konversi Teks ke Biner**: Mengubah teks ASCII menjadi representasi biner 8-bit per karakter.
- **Enkripsi XOR**: Melakukan operasi XOR antara pesan biner dan kunci biner.
- **Dekripsi XOR**: Mengembalikan ciphertext biner ke teks asli menggunakan kunci yang sama.
- **Antarmuka GUI**: Navigasi mudah dengan mode enkripsi dan dekripsi terpisah, dibangun dengan Tkinter.
- **Validasi Input**: Memastikan input biner hanya berisi '0' dan '1', dengan pesan error yang informatif.
- **Pengukuran Waktu**: Menampilkan waktu eksekusi untuk proses konversi, enkripsi, dan dekripsi.

## 🛠️ Prasyarat

Untuk menjalankan aplikasi ini, Anda memerlukan:
- **Python 3.8+**: Pastikan Python terinstal di sistem Anda. Unduh dari [python.org](https://www.python.org/downloads/).
- **Tkinter**: Pustaka GUI bawaan Python (biasanya sudah terinstal). Jika tidak, instal dengan:
  ```bash
  pip install tk
  ```
- **Sistem Operasi**: Windows, Linux, atau macOS.
- **Editor Kode**: Disarankan menggunakan Visual Studio Code, PyCharm, atau IDLE.

## 🚀 Cara Instalasi

1. **Clone atau Unduh Repositori**:
   ```bash
   git clone <https://github.com/AchmadAzza44/Uas-Kripto>
   cd <uas kripto>
   ```

2. **Pastikan Python Terinstal**:
   Periksa versi Python dengan:
   ```bash
   python --version
   ```

3. **Jalankan Aplikasi**:
   Jalankan file `XOR_cipher.pyther.py`:
   ```bash
   python XOR_cipher.py
   ```

4. **Catatan**: Tidak diperlukan pustaka eksternal tambahan karena Tkinter sudah terintegrasi dengan Python.

## 📋 Cara Penggunaan

Aplikasi memiliki dua mode utama: **Enkripsi** dan **Dekripsi**. Berikut langkah-langkah penggunaannya:

### Mode Enkripsi
1. Buka aplikasi dan pilih tab **Enkripsi** di sidebar kiri.
2. Masukkan teks (plaintext) pada kolom "Plaintext".
3. Klik tombol **Konversi ke Biner** untuk mengubah teks menjadi format biner.
4. Masukkan kunci biner (hanya '0' dan '1') pada kolom "Kunci Biner".
5. Klik tombol **Enkripsi XOR** untuk menghasilkan ciphertext dalam format biner.
6. Waktu proses akan ditampilkan dalam messagebox.

### Mode Dekripsi
1. Pilih tab **Dekripsi** di sidebar kiri.
2. Masukkan ciphertext biner pada kolom "Ciphertext (biner)".
3. Masukkan kunci biner yang sama yang digunakan saat enkripsi.
4. Klik tombol **Dekripsi** untuk mendapatkan teks asli.
5. Hasil dekripsi akan ditampilkan pada kolom "Hasil Dekripsi (teks)".

### Contoh Penggunaan
| Fungsi           | Input                              | Output                                                                 |
|-------------------|------------------------------------|-----------------------------------------------------------------------|
| Teks ke Biner    | "Informatika"                     | 0100100101101110011001100110111101110010011011010110000101110100... |
| Enkripsi XOR     | Plaintext: "Informatika", Kunci: "1010" | 11100011110001001100110011001110110110001100011111001011110111... |
| Dekripsi XOR     | Ciphertext: (hasil di atas), Kunci: "1010" | "Informatika"                                                     |

## 💻 Cuplikan Kode

Berikut adalah potongan kode inti dari aplikasi yang menunjukkan logika enkripsi dan dekripsi, serta sebagian setup GUI:

```python
def teks_ke_biner(teks):
    return ''.join(format(ord(char), '08b') for char in teks)

def biner_ke_teks(biner):
    try:
        chars = [biner[i:i+8] for i in range(0, len(biner), 8)]
        return ''.join(chr(int(char, 2)) for char in chars)
    except:
        return "[Format biner tidak valid]"

def xor_cipher(pesan_biner, kunci_biner):
    hasil = ''
    for i in range(len(pesan_biner)):
        bit_pesan = int(pesan_biner[i])
        bit_kunci = int(kunci_biner[i % len(kunci_biner)])
        hasil += str(bit_pesan ^ bit_kunci)
    return hasil

# GUI Setup
root = tk.Tk()
root.title("XOR Cipher - Enkripsi & Dekripsi (Soft White Theme)")
root.geometry("880x580")
root.configure(bg="#f9f9f9")

# Frame untuk menu navigasi
frame_menu = tk.Frame(root, bg="#adadad", width=150)
frame_menu.pack(side="left", fill="y")

# Frame konten utama
frame_konten = tk.Frame(root, bg="#ffffff")
frame_konten.pack(side="left", fill="both", expand=True)

# Tombol navigasi
btn_enkripsi_menu = tk.Button(frame_menu, text="Enkripsi", command=tampilkan_enkripsi)
btn_dekripsi_menu = tk.Button(frame_menu, text="Dekripsi", command=tampilkan_dekripsi)
```

**Penjelasan**:
- `teks_ke_biner`: Mengubah teks menjadi biner 8-bit per karakter berdasarkan nilai ASCII.
- `biner_ke_teks`: Mengonversi string biner kembali ke teks, dengan penanganan error.
- `xor_cipher`: Melakukan operasi XOR bit per bit antara pesan dan kunci, dengan pengulangan kunci jika lebih pendek.
- Bagian GUI menunjukkan struktur dasar antarmuka dengan frame menu dan tombol navigasi.

## 📊 Performa dan Analisis

Berdasarkan pengujian, aplikasi ini memiliki performa yang sangat cepat:
- **Konversi Teks ke Biner**: ~0.000015 detik untuk teks "halo".
- **Enkripsi/Deskripsi XOR**: ~0.000024–0.000032 detik untuk teks pendek.
- **Keunggulan dibandingkan AES**:
  - Waktu proses lebih cepat (di bawah 0.00003 detik vs. >0.0001 detik untuk AES).
  - Ukuran output sama dengan input, tanpa padding.
- **Keterbatasan**:
  - Keamanan lemah untuk penggunaan profesional karena kerentanan terhadap serangan kunci berulang.
  - Belum mendukung karakter Unicode penuh.
  - Hanya tersedia untuk platform desktop.

## 💡 Kelebihan dan Keterbatasan

### Kelebihan
- **Cepat dan Ringan**: Cocok untuk sistem dengan sumber daya terbatas.
- **Antarmuka Intuitif**: Mudah digunakan oleh pemula.
- **Edukasi**: Ideal untuk mempelajari konsep dasar kriptografi.
- **Validasi Input**: Mencegah kesalahan dengan pesan error yang jelas.

### Keterbatasan
- **Keamanan Terbatas**: Tidak cocok untuk aplikasi yang membutuhkan keamanan tinggi.
- **Fitur Terbatas**: Belum mendukung impor/ekspor file atau versi mobile/web.
- **Karakter Terbatas**: Hanya mendukung karakter ASCII dasar.

## 📝 Saran Pengembangan

- **Validasi Lebih Ketat**: Tambahkan pemeriksaan panjang kunci minimum untuk keamanan.
- **Fitur Impor/Ekspor**: Dukung input/output dari file teks.
- **Tema Visual**: Tambahkan opsi tema terang/gelap untuk kenyamanan pengguna.
- **Dukungan Unicode**: Perluas kompatibilitas untuk karakter non-ASCII.
- **Versi Web/Mobile**: Konversi ke framework seperti Flask atau Kivy untuk portabilitas.

## 👥 Kontributor

- **Pebi Heriansyah** (G1A023003)
- **Arriqoh Firzatullah** (G1A023033)
- **Achmad Azza Al Haqi** (G1A023037)
- **Reffki Andrea Pratama** (G1A023039)
- **Muhammad Farhan Dzakki** (G1A023041)

**Dosen Pengampu**: Ir. Kurnia Anggraini, S.T., M.T., Ph.D  
**Program Studi**: Informatika, Fakultas Teknik, Universitas Bengkulu  
**Tahun**: 2025

## 📚 Referensi

- Dewi, S. K. (2024). *Perbandingan Cryptography Klasik Vigenere Cipher Dengan Cryptography Modern RC4*.
- Erdriani, D., et al. (2023). *Penggunaan Operasi Biner X-or Dan N-or Pada Kriptografi Hill Cipher*. EDUSAINTEK.
- Fitria Lubis, A. F. L. (2024). *Modifikasi Metode Cipher Block Chaining (CBC) Dengan Pembangkit Kunci Mid Square*. Jurnal Ilmu Komputer.
- Harahap, L., et al. (2014). *Implementasi Metode Kriptografi Stream Cipher Gifford*. Jurnal Sains Dan Teknologi ISTP.
- Rahim, F., & Nasution, Y. R. (2024). *Implementasi Algoritma ChaCha20 Pada Pengamanan File Citra Bitmap*.
- Situmeang, Y., et al. (2023). *Implementasi Algoritma AES Rijndael Pada QR Code*.


---

⭐ **Jangan lupa berikan bintang di repositori jika proyek ini bermanfaat!**  
Untuk pertanyaan atau kontribusi, hubungi kami melalui email atau buka isu di repositori.
