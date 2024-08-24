import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

# Database setup
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
    db.commit()

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Password Generator')
        self.master.geometry('400x300')
        self.master.config(bg='#FF8000')

        # User Input
        Label(master, text="Enter Username:", bg='#FF8000').pack(pady=5)
        self.username_entry = Entry(master)
        self.username_entry.pack(pady=5)

        Label(master, text="Enter Password Length:", bg='#FF8000').pack(pady=5)
        self.length_entry = Entry(master)
        self.length_entry.pack(pady=5)

        # Generated Password Output
        Label(master, text="Generated Password:", bg='#FF8000').pack(pady=5)
        self.password_entry = Entry(master)
        self.password_entry.pack(pady=5)

        # Buttons
        Button(master, text="Generate Password", command=self.generate_password).pack(pady=10)
        Button(master, text="Save Password", command=self.save_password).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 6:
                raise ValueError("Password length must be at least 6")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, password)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def save_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty")
            return

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "This username already exists! Please use another username.")
            else:
                cursor.execute("INSERT INTO users(Username, GeneratedPassword) VALUES(?, ?)", (username, password))
                db.commit()
                messagebox.showinfo("Success", "Password saved successfully")

if __name__ == '__main__':
    root = Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
