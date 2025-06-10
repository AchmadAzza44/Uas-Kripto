# === BAGIAN 1: IMPOR DAN FUNGSI LOGIKA ===
# Bagian ini mengimpor pustaka yang diperlukan dan mendefinisikan fungsi-fungsi inti untuk operasi enkripsi/dekripsi.

import tkinter as tk
from tkinter import messagebox
import time

def teks_ke_biner(teks):
    """Mengubah teks menjadi biner 8-bit per karakter."""
    return ''.join(format(ord(char), '08b') for char in teks)

def biner_ke_teks(biner):
    """Mengubah biner menjadi teks. Memeriksa apakah panjang biner valid (kelipatan 8)."""
    if len(biner) % 8 != 0:
        return "[Biner tidak valid: panjang harus kelipatan 8]"
    try:
        chars = [biner[i:i+8] for i in range(0, len(biner), 8)]
        return ''.join(chr(int(char, 2)) for char in chars)
    except:
        return "[Format biner tidak valid]"

def xor_cipher(pesan_biner, kunci_biner):
    """Melakukan operasi XOR antara pesan biner dan kunci biner."""
    hasil = ''
    for i in range(len(pesan_biner)):
        bit_pesan = int(pesan_biner[i])
        bit_kunci = int(kunci_biner[i % len(kunci_biner)])
        hasil += str(bit_pesan ^ bit_kunci)
    return hasil

# === BAGIAN 2: FUNGSI UTILITAS GUI ===
# Bagian ini berisi fungsi untuk menangani clipboard dan pembersihan input.

def copy_to_clipboard(entry):
    """Menyalin isi field entry ke clipboard dan menampilkan pesan konfirmasi."""
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    messagebox.showinfo("Sukses", "Teks disalin ke clipboard!")

def clear_enkripsi():
    """Membersihkan semua field dan label waktu di frame enkripsi."""
    for e in [entry_plaintext, entry_plain_biner, entry_kunci_enkripsi, entry_cipher_biner]:
        e.delete(0, tk.END)
    time_label_biner.config(text="")
    time_label_enkripsi.config(text="")

def clear_dekripsi():
    """Membersihkan semua field dan label waktu di frame dekripsi."""
    for e in [entry_cipher_input, entry_kunci_dekripsi, entry_hasil_teks]:
        e.delete(0, tk.END)
    time_label_dekripsi.config(text="")

# Fungsi untuk menyimpan riwayat operasi
def log_operation(operation_type, input_data, result, time_taken):
    """Menyimpan riwayat operasi ke dalam daftar untuk ditampilkan di halaman rangkuman."""
    history.append(f"{operation_type}: Input = {input_data}, Hasil = {result}, Waktu = {time_taken:.6f} detik")
    update_summary()

# Fungsi untuk memperbarui tampilan rangkuman
def update_summary():
    """Memperbarui label rangkuman dengan riwayat operasi."""
    summary_text.delete(1.0, tk.END)
    for entry in history:
        summary_text.insert(tk.END, entry + "\n")

# === BAGIAN 3: SETUP GUI DAN STYLING ===
# Bagian ini mengatur jendela utama dan mendefinisikan fungsi untuk styling elemen GUI.

root = tk.Tk()
root.title("XOR Cipher - Enkripsi & Dekripsi (Soft White Theme)")
root.geometry("880x580")
root.configure(bg="#f9f9f9")

# Definisi font untuk konsistensi tampilan
font_title = ("Courier New", 20, "bold")
font_label = ("Courier New", 12, "bold")
font_entry = ("Courier New", 12)
font_button = ("Courier New", 11, "bold")
font_time = ("Courier New", 10)

# Fungsi styling untuk elemen GUI
def style_entry(e):
    """Mengatur gaya untuk field entry."""
    e.config(
        bg="#f0f0f0",
        fg="#333333",
        insertbackground="#333333",
        relief="solid",
        bd=2,
        font=font_entry,
        highlightthickness=0,
    )

def style_button(b, bg="#dcdcdc", fg="#000000"):
    """Mengatur gaya untuk tombol."""
    b.config(
        bg=bg,
        fg=fg,
        activebackground="#c0c0c0",
        activeforeground="#000000",
        relief="raised",
        bd=3,
        padx=12,
        pady=6,
        font=font_button,
        cursor="hand2",
    )

def style_label(l, fg="#5A5A5A"):
    """Mengatur gaya untuk label."""
    l.config(fg=fg, bg="#ffffff", font=font_label)

def style_time_label(l):
    """Mengatur gaya untuk label waktu."""
    l.config(fg="#666666", bg="#ffffff", font=font_time)

# Frame untuk menu samping, konten, dan keluar
frame_menu = tk.Frame(root, bg="#adadad", width=150)
frame_menu.pack(side="left", fill="y")

frame_konten = tk.Frame(root, bg="#ffffff")
frame_konten.pack(side="left", fill="both", expand=True)

frame_exit = tk.Frame(root, bg="#e0e0e0", width=150)
frame_exit.pack(side="right", fill="y")

# Fungsi untuk beralih antar frame
def tampilkan_petunjuk():
    """Menampilkan frame petunjuk dan menyembunyikan frame lain."""
    for frame in [frame_enkripsi, frame_dekripsi, frame_rangkuman]:
        frame.pack_forget()
    frame_petunjuk.pack(fill="both", expand=True, padx=25, pady=25)

def tampilkan_enkripsi():
    """Menampilkan frame enkripsi dan menyembunyikan frame lain."""
    for frame in [frame_petunjuk, frame_dekripsi, frame_rangkuman]:
        frame.pack_forget()
    frame_enkripsi.pack(fill="both", expand=True, padx=25, pady=25)

def tampilkan_dekripsi():
    """Menampilkan frame dekripsi dan menyembunyikan frame lain."""
    for frame in [frame_petunjuk, frame_enkripsi, frame_rangkuman]:
        frame.pack_forget()
    frame_dekripsi.pack(fill="both", expand=True, padx=25, pady=25)

def tampilkan_rangkuman():
    """Menampilkan frame rangkuman dan menyembunyikan frame lain."""
    for frame in [frame_petunjuk, frame_enkripsi, frame_dekripsi]:
        frame.pack_forget()
    frame_rangkuman.pack(fill="both", expand=True, padx=25, pady=25)

# Sidebar menu
history = []  # Daftar untuk menyimpan riwayat operasi
btn_petunjuk_menu = tk.Button(frame_menu, text="Petunjuk", command=tampilkan_petunjuk)
style_button(btn_petunjuk_menu, bg="#ffffff", fg="#000000")
btn_petunjuk_menu.pack(pady=20, padx=10, fill="x")

btn_enkripsi_menu = tk.Button(frame_menu, text="Enkripsi", command=tampilkan_enkripsi)
style_button(btn_enkripsi_menu, bg="#ffffff", fg="#000000")
btn_enkripsi_menu.pack(pady=10, padx=10, fill="x")

btn_dekripsi_menu = tk.Button(frame_menu, text="Dekripsi", command=tampilkan_dekripsi)
style_button(btn_dekripsi_menu, bg="#ffffff", fg="#000000")
btn_dekripsi_menu.pack(pady=10, padx=10, fill="x")

btn_rangkuman_menu = tk.Button(frame_menu, text="Rangkuman", command=tampilkan_rangkuman)
style_button(btn_rangkuman_menu, bg="#ffffff", fg="#000000")
btn_rangkuman_menu.pack(pady=10, padx=10, fill="x")

# === BAGIAN 4: FRAME PETUNJUK ===
# Bagian ini mengatur tata letak untuk halaman petunjuk.

frame_petunjuk = tk.Frame(frame_konten, bg="#ffffff")

tk.Label(frame_petunjuk, text="PETUNJUK PENGGUNAAN", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)
tk.Label(frame_petunjuk, text="1. Pilih 'Enkripsi' untuk mengenkripsi teks.\n"
                             "   - Masukkan plaintext, konversi ke biner, lalu gunakan kunci biner untuk enkripsi.\n"
                             "2. Pilih 'Dekripsi' untuk mendekripsi teks.\n"
                             "   - Masukkan ciphertext dan kunci biner untuk mendapatkan teks asli.\n"
                             "3. Gunakan tombol 'Salin ke Clipboard' untuk menyalin hasil.\n"
                             "4. Lihat 'Rangkuman' untuk riwayat operasi.\n"
                             "Catatan: Pastikan input biner hanya berisi 0 dan 1, dan panjang ciphertext kelipatan 8 bit.",
        font=font_label, fg="#333333", bg="#ffffff", justify="left").pack(pady=20, padx=20)

# === BAGIAN 5: FRAME ENKRIPSI ===
# Bagian ini mengatur tata letak dan logika untuk frame enkripsi.

frame_enkripsi = tk.Frame(frame_konten, bg="#ffffff")

tk.Label(frame_enkripsi, text="ENKRIPSI", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)

entry_plaintext = tk.Entry(frame_enkripsi, width=80)
entry_plain_biner = tk.Entry(frame_enkripsi, width=80)
entry_kunci_enkripsi = tk.Entry(frame_enkripsi, width=80)
entry_cipher_biner = tk.Entry(frame_enkripsi, width=80)

for e in [entry_plaintext, entry_plain_biner, entry_kunci_enkripsi, entry_cipher_biner]:
    style_entry(e)

time_label_biner = tk.Label(frame_enkripsi, text="", bg="#ffffff")
style_time_label(time_label_biner)

time_label_enkripsi = tk.Label(frame_enkripsi, text="", bg="#ffffff")
style_time_label(time_label_enkripsi)

def konversi_ke_biner():
    """Mengonversi plaintext ke biner dan menampilkan waktu proses."""
    teks = entry_plaintext.get()
    if not teks:
        messagebox.showwarning("Peringatan", "Masukkan plaintext.")
        return
    start_time = time.perf_counter()
    biner = teks_ke_biner(teks)
    end_time = time.perf_counter()
    
    entry_plain_biner.delete(0, tk.END)
    entry_plain_biner.insert(0, biner)
    time_label_biner.config(text=f"Waktu konversi ke biner: {end_time - start_time:.6f} detik")
    log_operation("Konversi", teks, biner, end_time - start_time)

def enkripsi():
    """Melakukan enkripsi XOR dan menampilkan waktu proses."""
    pesan_biner = entry_plain_biner.get()
    kunci = entry_kunci_enkripsi.get()
    if not pesan_biner or not kunci:
        messagebox.showwarning("Peringatan", "Isi biner plaintext dan kunci!")
        return
    if any(c not in '01' for c in pesan_biner + kunci):
        messagebox.showerror("Error", "Hanya 0 dan 1 diperbolehkan!")
        return
    start_time = time.perf_counter()
    cipher = xor_cipher(pesan_biner, kunci)
    end_time = time.perf_counter()
    
    entry_cipher_biner.delete(0, tk.END)
    entry_cipher_biner.insert(0, cipher)
    time_label_enkripsi.config(text=f"Waktu enkripsi: {end_time - start_time:.6f} detik")
    log_operation("Enkripsi", pesan_biner, cipher, end_time - start_time)

tk.Label(frame_enkripsi, text="Plaintext:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_plaintext.pack(pady=3)

btn_konversi = tk.Button(frame_enkripsi, text="Konversi ke Biner", command=konversi_ke_biner)
style_button(btn_konversi)
btn_konversi.pack(pady=8)

tk.Label(frame_enkripsi, text="Biner Plaintext:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_plain_biner.pack(pady=3)
time_label_biner.pack(anchor="w", pady=2)

tk.Label(frame_enkripsi, text="Kunci Biner:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_kunci_enkripsi.pack(pady=3)

btn_enkripsi = tk.Button(frame_enkripsi, text="Enkripsi XOR", command=enkripsi)
style_button(btn_enkripsi)
btn_enkripsi.pack(pady=10)

tk.Label(frame_enkripsi, text="Ciphertext (biner):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_cipher_biner.pack(pady=3)
btn_copy_cipher = tk.Button(frame_enkripsi, text="Salin ke Clipboard", command=lambda: copy_to_clipboard(entry_cipher_biner))
style_button(btn_copy_cipher)
btn_copy_cipher.pack(pady=5)
time_label_enkripsi.pack(anchor="w", pady=2)

btn_clear_enkripsi = tk.Button(frame_enkripsi, text="Bersihkan Semua", command=clear_enkripsi)
style_button(btn_clear_enkripsi, bg="#ffcccc", fg="#000000")
btn_clear_enkripsi.pack(pady=10)

# === BAGIAN 6: FRAME DEKRIPSI ===
# Bagian ini mengatur tata letak dan logika untuk frame dekripsi.

frame_dekripsi = tk.Frame(frame_konten, bg="#ffffff")

tk.Label(frame_dekripsi, text="DEKRIPSI", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)

entry_cipher_input = tk.Entry(frame_dekripsi, width=80)
entry_kunci_dekripsi = tk.Entry(frame_dekripsi, width=80)
entry_hasil_teks = tk.Entry(frame_dekripsi, width=80)

for e in [entry_cipher_input, entry_kunci_dekripsi, entry_hasil_teks]:
    style_entry(e)

time_label_dekripsi = tk.Label(frame_dekripsi, text="", bg="#ffffff")
style_time_label(time_label_dekripsi)

def dekripsi():
    """Melakukan dekripsi XOR dan menampilkan waktu proses."""
    cipher_biner = entry_cipher_input.get()
    kunci = entry_kunci_dekripsi.get()
    if not cipher_biner or not kunci:
        messagebox.showwarning("Peringatan", "Isi ciphertext dan kunci!")
        return
    if any(c not in '01' for c in cipher_biner + kunci):
        messagebox.showerror("Error", "Hanya 0 dan 1 diperbolehkan!")
        return
    if len(cipher_biner) % 8 != 0:
        messagebox.showerror("Error", "Panjang ciphertext harus kelipatan 8 bit!")
        return
    start_time = time.perf_counter()
    decrypted_biner = xor_cipher(cipher_biner, kunci)
    hasil = biner_ke_teks(decrypted_biner)
    end_time = time.perf_counter()
    
    entry_hasil_teks.delete(0, tk.END)
    entry_hasil_teks.insert(0, hasil)
    time_label_dekripsi.config(text=f"Waktu dekripsi: {end_time - start_time:.6f} detik")
    log_operation("Dekripsi", cipher_biner, hasil, end_time - start_time)

tk.Label(frame_dekripsi, text="Ciphertext (biner):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_cipher_input.pack(pady=3)

tk.Label(frame_dekripsi, text="Kunci Biner:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_kunci_dekripsi.pack(pady=3)

btn_dekripsi = tk.Button(frame_dekripsi, text="Dekripsi", command=dekripsi)
style_button(btn_dekripsi)
btn_dekripsi.pack(pady=10)

tk.Label(frame_dekripsi, text="Hasil Dekripsi (teks):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_hasil_teks.pack(pady=3)
btn_copy_hasil = tk.Button(frame_dekripsi, text="Salin ke Clipboard", command=lambda: copy_to_clipboard(entry_hasil_teks))
style_button(btn_copy_hasil)
btn_copy_hasil.pack(pady=5)
time_label_dekripsi.pack(anchor="w", pady=2)

btn_clear_dekripsi = tk.Button(frame_dekripsi, text="Bersihkan Semua", command=clear_dekripsi)
style_button(btn_clear_dekripsi, bg="#ffcccc", fg="#000000")
btn_clear_dekripsi.pack(pady=10)

# === BAGIAN 7: FRAME RANGKUMAN ===
# Bagian ini mengatur tata letak untuk halaman rangkuman.

frame_rangkuman = tk.Frame(frame_konten, bg="#ffffff")

tk.Label(frame_rangkuman, text="RANGKUMAN PROSES", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)
summary_text = tk.Text(frame_rangkuman, height=20, width=80, bg="#f0f0f0", font=font_label)
summary_text.pack(pady=10, padx=20)

# === BAGIAN 8: MAIN LOOP ===
# Bagian ini memulai aplikasi dengan menampilkan frame petunjuk sebagai default.

tampilkan_petunjuk()
root.mainloop()
