import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os

def get_image_path():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
    if img_path:
        return img_path
    else:
        messagebox.showerror("Error", "Path gambar tidak valid.")
        return None

def hide_message():
    image_path = get_image_path()
    if image_path:
        message = entry_message.get()
        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            try:
                secret = lsb.hide(image_path, message)
                secret.save(save_path)
                messagebox.showinfo("Success", f"Pesan berhasil disembunyikan! Gambar disimpan di: {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan gambar: {e}")

def show_message():
    image_path = get_image_path()
    if image_path:
        try:
            clear_message = lsb.reveal(image_path)
            if clear_message:
                entry_result.delete(0, tk.END)
                entry_result.insert(0, clear_message)
            else:
                messagebox.showinfo("No Message", "Tidak ada pesan tersembunyi dalam gambar ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

window = tk.Tk()
window.title("Aplikasi Steganografi")
window.geometry("600x400")
window.configure(bg="#34495e")  # Soft grayish background

# Title Label
title_label = tk.Label(window, text="Aplikasi Steganografi", font=("Verdana", 18, "bold"), bg="#34495e", fg="#ecf0f1")
title_label.pack(pady=15)

# Message Input Frame
frame_input = tk.Frame(window, bg="#2c3e50")
frame_input.pack(pady=15, padx=15, fill="x")

label_message = tk.Label(frame_input, text="Masukkan pesan rahasia:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1")
label_message.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_message = tk.Entry(frame_input, width=50, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
entry_message.grid(row=0, column=1, padx=10, pady=10)

# Buttons Frame
frame_buttons = tk.Frame(window, bg="#34495e")
frame_buttons.pack(pady=20)

button_hide = tk.Button(frame_buttons, text="Sembunyikan Pesan", font=("Verdana", 12, "bold"), bg="#1abc9c", fg="white", width=20, command=hide_message)
button_hide.grid(row=0, column=0, padx=20, pady=10)

button_show = tk.Button(frame_buttons, text="Tampilkan Pesan", font=("Verdana", 12, "bold"), bg="#e74c3c", fg="white", width=20, command=show_message)
button_show.grid(row=0, column=1, padx=20, pady=10)

# Output Frame
frame_output = tk.Frame(window, bg="#2c3e50")
frame_output.pack(pady=15)

label_result = tk.Label(frame_output, text="Pesan Tersembunyi:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1")
label_result.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_result = tk.Entry(frame_output, width=50, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
entry_result.grid(row=0, column=1, padx=10, pady=10)



window.mainloop()
