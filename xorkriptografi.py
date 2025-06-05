import tkinter as tk
from tkinter import messagebox

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

# === GUI SETUP ===
root = tk.Tk()
root.title("XOR Cipher - Enkripsi & Dekripsi (Soft White Theme)")
root.geometry("880x580")
root.configure(bg="#f9f9f9")

font_title = ("Courier New", 20, "bold")
font_label = ("Courier New", 12, "bold")
font_entry = ("Courier New", 12)
font_button = ("Courier New", 11, "bold")

# === FRAME STRUCTURE ===
frame_menu = tk.Frame(root, bg="#adadad", width=150)
frame_menu.pack(side="left", fill="y")

frame_konten = tk.Frame(root, bg="#ffffff")
frame_konten.pack(side="left", fill="both", expand=True)

frame_exit = tk.Frame(root, bg="#e0e0e0", width=150)
frame_exit.pack(side="right", fill="y")

frame_enkripsi = tk.Frame(frame_konten, bg="#ffffff")
frame_dekripsi = tk.Frame(frame_konten, bg="#ffffff")

def tampilkan_enkripsi():
    frame_dekripsi.pack_forget()
    frame_enkripsi.pack(fill="both", expand=True, padx=25, pady=25)

def tampilkan_dekripsi():
    frame_enkripsi.pack_forget()
    frame_dekripsi.pack(fill="both", expand=True, padx=25, pady=25)

# === BUTTON STYLING ===
def style_entry(e):
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
    l.config(fg=fg, bg="#ffffff", font=font_label)

# === SIDEBAR MENU (LEFT) ===
btn_enkripsi_menu = tk.Button(frame_menu, text="Enkripsi", command=tampilkan_enkripsi)
style_button(btn_enkripsi_menu, bg="#ffffff", fg="#000000")
btn_enkripsi_menu.pack(pady=20, padx=10, fill="x")

btn_dekripsi_menu = tk.Button(frame_menu, text="Dekripsi", command=tampilkan_dekripsi)
style_button(btn_dekripsi_menu, bg="#ffffff", fg="#000000")
btn_dekripsi_menu.pack(pady=10, padx=10, fill="x")

# === FRAME ENKRIPSI ===
tk.Label(frame_enkripsi, text="ENKRIPSI", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)

entry_plaintext = tk.Entry(frame_enkripsi, width=80)
entry_plain_biner = tk.Entry(frame_enkripsi, width=80)
entry_kunci_enkripsi = tk.Entry(frame_enkripsi, width=80)
entry_cipher_biner = tk.Entry(frame_enkripsi, width=80)

for e in [entry_plaintext, entry_plain_biner, entry_kunci_enkripsi, entry_cipher_biner]:
    style_entry(e)

def konversi_ke_biner():
    teks = entry_plaintext.get()
    if not teks:
        messagebox.showwarning("Peringatan", "Masukkan plaintext.")
        return
    biner = teks_ke_biner(teks)
    entry_plain_biner.delete(0, tk.END)
    entry_plain_biner.insert(0, biner)

def enkripsi():
    pesan_biner = entry_plain_biner.get()
    kunci = entry_kunci_enkripsi.get()
    if not pesan_biner or not kunci:
        messagebox.showwarning("Peringatan", "Isi biner plaintext dan kunci!")
        return
    if any(c not in '01' for c in pesan_biner + kunci):
        messagebox.showerror("Error", "Hanya 0 dan 1 diperbolehkan!")
        return
    cipher = xor_cipher(pesan_biner, kunci)
    entry_cipher_biner.delete(0, tk.END)
    entry_cipher_biner.insert(0, cipher)

style_label(tk.Label(frame_enkripsi, text="Plaintext:"))
tk.Label(frame_enkripsi, text="Plaintext:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_plaintext.pack(pady=3)

btn_konversi = tk.Button(frame_enkripsi, text="Konversi ke Biner", command=konversi_ke_biner)
style_button(btn_konversi)
btn_konversi.pack(pady=8)

style_label(tk.Label(frame_enkripsi, text="Biner Plaintext:"))
tk.Label(frame_enkripsi, text="Biner Plaintext:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_plain_biner.pack(pady=3)

style_label(tk.Label(frame_enkripsi, text="Kunci Biner:"))
tk.Label(frame_enkripsi, text="Kunci Biner:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_kunci_enkripsi.pack(pady=3)

btn_enkripsi = tk.Button(frame_enkripsi, text="Enkripsi XOR", command=enkripsi)
style_button(btn_enkripsi)
btn_enkripsi.pack(pady=10)

style_label(tk.Label(frame_enkripsi, text="Ciphertext (biner):"))
tk.Label(frame_enkripsi, text="Ciphertext (biner):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_cipher_biner.pack(pady=3)

# === FRAME DEKRIPSI ===
tk.Label(frame_dekripsi, text="DEKRIPSI", font=font_title, fg="#000000", bg="#ffffff").pack(pady=20)

entry_cipher_input = tk.Entry(frame_dekripsi, width=80)
entry_kunci_dekripsi = tk.Entry(frame_dekripsi, width=80)
entry_hasil_teks = tk.Entry(frame_dekripsi, width=80)

for e in [entry_cipher_input, entry_kunci_dekripsi, entry_hasil_teks]:
    style_entry(e)

def dekripsi():
    cipher_biner = entry_cipher_input.get()
    kunci = entry_kunci_dekripsi.get()
    if not cipher_biner or not kunci:
        messagebox.showwarning("Peringatan", "Isi ciphertext dan kunci!")
        return
    if any(c not in '01' for c in cipher_biner + kunci):
        messagebox.showerror("Error", "Hanya 0 dan 1 diperbolehkan!")
        return
    decrypted_biner = xor_cipher(cipher_biner, kunci)
    hasil = biner_ke_teks(decrypted_biner)
    entry_hasil_teks.delete(0, tk.END)
    entry_hasil_teks.insert(0, hasil)

style_label(tk.Label(frame_dekripsi, text="Ciphertext (biner):"))
tk.Label(frame_dekripsi, text="Ciphertext (biner):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_cipher_input.pack(pady=3)

style_label(tk.Label(frame_dekripsi, text="Kunci Biner:"))
tk.Label(frame_dekripsi, text="Kunci Biner:", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_kunci_dekripsi.pack(pady=3)

btn_dekripsi = tk.Button(frame_dekripsi, text="Dekripsi", command=dekripsi)
style_button(btn_dekripsi)
btn_dekripsi.pack(pady=10)

style_label(tk.Label(frame_dekripsi, text="Hasil Dekripsi (teks):"))
tk.Label(frame_dekripsi, text="Hasil Dekripsi (teks):", bg="#ffffff", fg="#333333", font=font_label).pack(anchor="w", pady=(10,3))
entry_hasil_teks.pack(pady=3)

tampilkan_enkripsi()
root.mainloop()