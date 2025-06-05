
 # XOR Cipher GUI - Enkripsi & Dekripsi dengan Python

Proyek ini adalah aplikasi desktop GUI (Graphical User Interface) sederhana berbasis **Tkinter** yang memungkinkan pengguna untuk melakukan enkripsi dan dekripsi teks menggunakan algoritma **XOR Cipher**. Aplikasi ini juga menyertakan konversi teks ke biner dan sebaliknya.

## 🎯 Fitur Utama

- Konversi teks (plaintext) ke biner
- Enkripsi XOR berbasis biner
- Dekripsi XOR untuk mengembalikan plaintext
- Tampilan GUI minimalis dengan tema soft white
- Validasi input agar hanya menerima karakter biner

---

## 📦 Struktur File

- `xorkriptografi.py` - Seluruh kode aplikasi (fungsi, GUI, logika enkripsi & dekripsi)

---

## 🛠️ Cara Menjalankan

1. Pastikan Python 3 telah terinstal di sistem Anda.
2. Jalankan program dengan perintah:

   ```bash
   python xorkriptografi.py
   ```

3. Aplikasi GUI akan muncul dan siap digunakan.

---

## 🔐 Penjelasan Fungsionalitas

### Enkripsi XOR

1. Pengguna memasukkan teks (plaintext).
2. Aplikasi mengubah teks ke dalam bentuk biner (ASCII 8-bit per karakter).
3. Pengguna memasukkan kunci dalam bentuk biner.
4. XOR dilakukan antara plaintext biner dan kunci.
5. Hasil XOR ditampilkan sebagai ciphertext (dalam biner).

### Dekripsi XOR

1. Pengguna memasukkan ciphertext dalam bentuk biner.
2. Pengguna memasukkan kunci biner yang sama dengan yang digunakan untuk enkripsi.
3. XOR dilakukan ulang.
4. Hasil XOR dikonversi kembali ke teks asli.

---

## 💡 Contoh Penggunaan

Misalnya plaintext: `HALO`

- Teks ke biner:
  ```
  H = 01001000
  A = 01000001
  L = 01001100
  O = 01001111
  ```
- Jika kunci: `11001100` (akan diulang jika lebih pendek dari pesan)
- XOR akan dilakukan per bit dan menghasilkan ciphertext.

---

## 📋 Validasi Input

- Input biner (plaintext biner, kunci, ciphertext) hanya boleh terdiri dari karakter `0` dan `1`.
- Jika input tidak sesuai, aplikasi akan menampilkan peringatan.

---

## 🧩 Struktur GUI

- **Sidebar kiri**: Navigasi (Enkripsi / Dekripsi)
- **Konten utama**:
  - Untuk Enkripsi:
    - Input teks
    - Konversi ke biner
    - Input kunci
    - Hasil enkripsi biner
  - Untuk Dekripsi:
    - Input ciphertext biner
    - Input kunci
    - Output hasil dekripsi dalam teks

---

## 🧠 Catatan Teknis

- Fungsi utama:
  - `teks_ke_biner(teks)`: Mengonversi teks ke biner.
  - `biner_ke_teks(biner)`: Mengonversi biner ke teks.
  - `xor_cipher(pesan_biner, kunci_biner)`: XOR cipher logic.
- Antarmuka dibangun menggunakan widget Tkinter:
  - `Frame`, `Button`, `Label`, `Entry`, dan `messagebox`.

---

## 📌 Ketergantungan

- Python 3.x
- Modul standar Python: `tkinter`

---

## 📃 Lisensi

Proyek ini bersifat open-source dan dapat digunakan untuk keperluan pembelajaran dan pengembangan lebih lanjut.

---

## 🙋‍♂️ Kontribusi

Saran, perbaikan, dan kontribusi lain sangat diterima! Anda bisa menambahkan fitur seperti:
- Simpan/load file
- Dukungan karakter Unicode
- Mode gelap
