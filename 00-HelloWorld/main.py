import tkinter as tk

# Membuat jendela utama
window = tk.Tk()
window.title("Hello World")
window.geometry("300x200")

# Fungsi saat tombol ditekan
def tombol_diklik():
	label.config(text="Halo Gantengg")

# Label
label = tk.Label(window, text="Welcome to World", font=("Arial", 14))
label.pack(pady=10)

# Tombol
tombol = tk.Button(window, text="Tekan saya bang", command=tombol_diklik)
tombol.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()