import tkinter as tk
from tkinter import messagebox

class Enigma:
    def __init__(self, rotor1_pos, rotor2_pos, rotor3_pos):
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        return [rotor.index(i) for i in range(26)]

    def encrypt_decrypt_char(self, ch):
        if not ch.isalpha():
            return ch

        is_lower = ch.islower()
        ch = ch.upper()
        offset = ord(ch) - 65

        offset = self.rotor1[(offset + self.rotor1_pos) % 26]
        offset = self.rotor2[(offset + self.rotor2_pos) % 26]
        offset = self.rotor3[(offset + self.rotor3_pos) % 26]

        offset = self.reflector[offset]

        offset = self.inverse_rotor3[(offset - self.rotor3_pos) % 26]
        offset = self.inverse_rotor2[(offset - self.rotor2_pos) % 26]
        offset = self.inverse_rotor1[(offset - self.rotor1_pos) % 26]

        self.rotor1_pos = (self.rotor1_pos + 1) % 26
        if self.rotor1_pos == 0:
            self.rotor2_pos = (self.rotor2_pos + 1) % 26
            if self.rotor2_pos == 0:
                self.rotor3_pos = (self.rotor3_pos + 1) % 26

        result = chr(offset + 65)
        return result.lower() if is_lower else result

    def process(self, text):
        return ''.join(self.encrypt_decrypt_char(ch) for ch in text)


class EnigmaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Cipher")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#34495e")  # Soft grayish background

        # Title
        tk.Label(root, text="Enigma Cipher", font=("Verdana", 18, "bold"), bg="#34495e", fg="#ecf0f1").pack(pady=15)

        # Rotor Positions Frame
        frame_input = tk.Frame(root, bg="#2c3e50")
        frame_input.pack(pady=15, padx=15, fill="x")

        tk.Label(frame_input, text="Rotor 1 Pos:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.rotor1_entry = tk.Entry(frame_input, width=5, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
        self.rotor1_entry.grid(row=0, column=1, padx=15, pady=10)

        tk.Label(frame_input, text="Rotor 2 Pos:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=2, padx=15, pady=10, sticky="w")
        self.rotor2_entry = tk.Entry(frame_input, width=5, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
        self.rotor2_entry.grid(row=0, column=3, padx=15, pady=10)

        tk.Label(frame_input, text="Rotor 3 Pos:", font=("Verdana", 12), bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=4, padx=15, pady=10, sticky="w")
        self.rotor3_entry = tk.Entry(frame_input, width=5, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
        self.rotor3_entry.grid(row=0, column=5, padx=15, pady=10)

        # Input Text Area
        tk.Label(root, text="Input Text:", font=("Verdana", 12), bg="#34495e", fg="#ecf0f1").pack(pady=10)
        self.input_text = tk.Text(root, height=5, width=60, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
        self.input_text.pack(pady=10)

        # Buttons Frame
        frame_buttons = tk.Frame(root, bg="#34495e")
        frame_buttons.pack(pady=20)

        tk.Button(frame_buttons, text="Encrypt", font=("Verdana", 12, "bold"), bg="#1abc9c", fg="#ffffff", width=15, command=self.encrypt_text).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(frame_buttons, text="Decrypt", font=("Verdana", 12, "bold"), bg="#e74c3c", fg="#ffffff", width=15, command=self.decrypt_text).grid(row=0, column=1, padx=20, pady=10)

        # Output Text Area
        tk.Label(root, text="Output Text:", font=("Verdana", 12), bg="#34495e", fg="#ecf0f1").pack(pady=10)
        self.output_text = tk.Text(root, height=5, width=60, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50", state="disabled")
        self.output_text.pack(pady=10)

    def get_rotor_positions(self):
        try:
            rotor1_pos = int(self.rotor1_entry.get())
            rotor2_pos = int(self.rotor2_entry.get())
            rotor3_pos = int(self.rotor3_entry.get())
            return rotor1_pos, rotor2_pos, rotor3_pos
        except ValueError:
            messagebox.showerror("Error", "Rotor positions must be integers between 0 and 25.")
            return None

    def encrypt_text(self):
        positions = self.get_rotor_positions()
        if positions:
            rotor1_pos, rotor2_pos, rotor3_pos = positions
            enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
            input_text = self.input_text.get("1.0", tk.END).strip()
            encrypted_text = enigma.process(input_text)
            self.display_output(encrypted_text)

    def decrypt_text(self):
        positions = self.get_rotor_positions()
        if positions:
            rotor1_pos, rotor2_pos, rotor3_pos = positions
            enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
            input_text = self.input_text.get("1.0", tk.END).strip()
            decrypted_text = enigma.process(input_text)
            self.display_output(decrypted_text)

    def display_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()
