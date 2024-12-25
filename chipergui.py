import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def encrypt_text():
    plain_text = entry_plain_text.get()
    shift = shift_value.get()
    try:
        shift = int(shift)
        cipher_text = enkripsi(plain_text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, cipher_text)
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")

def decrypt_text():
    cipher_text = entry_plain_text.get()
    shift = shift_value.get()
    try:
        shift = int(shift)
        plain_text = dekripsi(cipher_text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, plain_text)
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")

# Setup GUI
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("700x500")
window.configure(bg="#34495e")

# Title label
title_label = tk.Label(window, text="Caesar Cipher Encryption & Decryption", font=("Verdana", 18, "bold"), bg="#34495e", fg="#ecf0f1")
title_label.pack(pady=15)

# Input Frame
frame_input = tk.Frame(window, bg="#2c3e50")
frame_input.pack(pady=15, padx=15, fill="x")

label_plain_text = tk.Label(frame_input, text="Input Text:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1")
label_plain_text.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_plain_text = tk.Entry(frame_input, width=60, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
entry_plain_text.grid(row=0, column=1, padx=15, pady=10)

label_shift = tk.Label(frame_input, text="Shift Value:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1")
label_shift.grid(row=1, column=0, padx=15, pady=10, sticky="w")
shift_value = tk.Entry(frame_input, width=10, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
shift_value.grid(row=1, column=1, padx=15, pady=10, sticky="w")

# Buttons
frame_buttons = tk.Frame(window, bg="#34495e")
frame_buttons.pack(pady=20)

button_encrypt = tk.Button(frame_buttons, text="Encrypt", font=("Verdana", 12, "bold"), bg="#1abc9c", fg="#ffffff", width=15, command=encrypt_text)
button_encrypt.grid(row=0, column=0, padx=20, pady=10)

button_decrypt = tk.Button(frame_buttons, text="Decrypt", font=("Verdana", 12, "bold"), bg="#e74c3c", fg="#ffffff", width=15, command=decrypt_text)
button_decrypt.grid(row=0, column=1, padx=20, pady=10)

# Result Output
frame_output = tk.Frame(window, bg="#2c3e50")
frame_output.pack(pady=15, padx=15, fill="x")

label_result = tk.Label(frame_output, text="Result:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1")
label_result.grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_result = tk.Entry(frame_output, width=60, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
entry_result.grid(row=0, column=1, padx=15, pady=10)


# Run the application
window.mainloop()
