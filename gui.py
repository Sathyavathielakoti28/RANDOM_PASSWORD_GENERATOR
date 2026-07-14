import tkinter as tk
from tkinter import messagebox

from password_generator import generate_password
from clipboard import copy_password

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Title
        title = tk.Label(
            root,
            text="Random Password Generator",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        # Password Length
        length_label = tk.Label(
            root,
            text="Enter Password Length:",
            font=("Arial", 12)
        )
        length_label.pack()

        self.length_entry = tk.Entry(
            root,
            font=("Arial", 12),
            width=10,
            justify="center"
        )
        self.length_entry.pack(pady=5)

        # Checkbox Variables
        self.uppercase = tk.BooleanVar(value=True)
        self.lowercase = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar(value=True)

        # Checkboxes
        tk.Checkbutton(
            root,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase
        ).pack(anchor="w", padx=120)

        tk.Checkbutton(
            root,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase
        ).pack(anchor="w", padx=120)

        tk.Checkbutton(
            root,
            text="Numbers (0-9)",
            variable=self.numbers
        ).pack(anchor="w", padx=120)

        tk.Checkbutton(
            root,
            text="Symbols (!@#$%^&*)",
            variable=self.symbols
        ).pack(anchor="w", padx=120)

        # Generate Button
        generate_button = tk.Button(
            root,
            text="Generate Password",
            command=self.generate,
            width=20,
            bg="green",
            fg="white",
            font=("Arial", 12)
        )
        generate_button.pack(pady=20)

        # Password Display
        self.password_entry = tk.Entry(
            root,
            font=("Arial", 12),
            width=35,
            justify="center"
        )
        self.password_entry.pack(pady=10)

        # Copy Button
        copy_button = tk.Button(
            root,
            text="Copy Password",
            command=self.copy,
            width=20,
            bg="blue",
            fg="white",
            font=("Arial", 12)
        )
        copy_button.pack()

    def generate(self):
        try:
            length = int(self.length_entry.get())

            if length < 4 or length > 50:
                messagebox.showerror(
                    "Error",
                    "Password length must be between 4 and 50."
                )
                return

            password = generate_password(
                length,
                self.uppercase.get(),
                self.lowercase.get(),
                self.numbers.get(),
                self.symbols.get()
            )

            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def copy(self):
        copy_password(
            self.root,
            self.password_entry.get()
        )