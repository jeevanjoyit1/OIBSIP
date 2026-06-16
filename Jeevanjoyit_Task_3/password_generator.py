import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets
import pyperclip

# =========================
# Color Theme
# =========================
PRIMARY = "#2563EB"
SUCCESS = "#16A34A"
WARNING = "#EA580C"
DANGER = "#DC2626"
BG_COLOR = "#F1F5F9"


class PasswordGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("700x800")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        # Title
        title = tk.Label(
            self.root,
            text="🔐 Password Generator",
            font=("Segoe UI", 24, "bold"),
            fg=PRIMARY,
            bg=BG_COLOR
        )
        title.pack(pady=20)

        # =========================
        # Password Length
        # =========================
        length_frame = ttk.LabelFrame(
            self.root,
            text="Password Settings"
        )
        length_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(
            length_frame,
            text="Password Length:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.IntVar(value=12)

        ttk.Spinbox(
            length_frame,
            from_=4,
            to=64,
            textvariable=self.length_var,
            width=10
        ).grid(row=0, column=1, padx=10, pady=10)

        # =========================
        # Character Options
        # =========================
        options_frame = ttk.LabelFrame(
            self.root,
            text="Character Options"
        )
        options_frame.pack(fill="x", padx=20, pady=10)

        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.number_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            options_frame,
            text="Uppercase (A-Z)",
            variable=self.upper_var
        ).pack(anchor="w", padx=10, pady=5)

        ttk.Checkbutton(
            options_frame,
            text="Lowercase (a-z)",
            variable=self.lower_var
        ).pack(anchor="w", padx=10, pady=5)

        ttk.Checkbutton(
            options_frame,
            text="Numbers (0-9)",
            variable=self.number_var
        ).pack(anchor="w", padx=10, pady=5)

        ttk.Checkbutton(
            options_frame,
            text="Symbols (!@#$%^&*)",
            variable=self.symbol_var
        ).pack(anchor="w", padx=10, pady=5)

        # =========================
        # Exclude Characters
        # =========================
        exclude_frame = ttk.LabelFrame(
            self.root,
            text="Exclude Characters"
        )
        exclude_frame.pack(fill="x", padx=20, pady=10)

        self.exclude_entry = ttk.Entry(exclude_frame)
        self.exclude_entry.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # =========================
        # Generate Button
        # =========================
        self.generate_btn = tk.Button(
            self.root,
            text="⚡ Generate Password",
            command=self.generate_password,
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )

        self.generate_btn.pack(pady=15)

        self.generate_btn.bind(
            "<Enter>",
            lambda e: self.generate_btn.config(bg="#1D4ED8")
        )

        self.generate_btn.bind(
            "<Leave>",
            lambda e: self.generate_btn.config(bg=PRIMARY)
        )

        # =========================
        # Password Display
        # =========================
        output_frame = ttk.LabelFrame(
            self.root,
            text="Generated Password"
        )
        output_frame.pack(fill="x", padx=20, pady=10)

        self.password_var = tk.StringVar()

        self.password_entry = tk.Entry(
            output_frame,
            textvariable=self.password_var,
            font=("Consolas", 18, "bold"),
            bg="#1E293B",
            fg="#00FF88",
            insertbackground="white",
            relief="solid",
            bd=2,
            justify="center"
        )

        self.password_entry.pack(
            fill="x",
            padx=10,
            pady=15,
            ipady=10
        )

        # =========================
        # Strength Indicator
        # =========================
        self.strength_label = tk.Label(
            self.root,
            text="Strength: Not Generated",
            font=("Segoe UI", 12, "bold"),
            bg=BG_COLOR
        )

        self.strength_label.pack(pady=10)

        # =========================
        # Copy Button
        # =========================
        self.copy_btn = tk.Button(
            self.root,
            text="📋 Copy Password",
            command=self.copy_password,
            bg=SUCCESS,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )

        self.copy_btn.pack(pady=10)

        self.copy_btn.bind(
            "<Enter>",
            lambda e: self.copy_btn.config(bg="#15803D")
        )

        self.copy_btn.bind(
            "<Leave>",
            lambda e: self.copy_btn.config(bg=SUCCESS)
        )

    def generate_password(self):

        characters = ""

        if self.upper_var.get():
            characters += string.ascii_uppercase

        if self.lower_var.get():
            characters += string.ascii_lowercase

        if self.number_var.get():
            characters += string.digits

        if self.symbol_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror(
                "Error",
                "Please select at least one character type."
            )
            return

        excluded = self.exclude_entry.get()

        characters = ''.join(
            char for char in characters
            if char not in excluded
        )

        if not characters:
            messagebox.showerror(
                "Error",
                "All characters have been excluded."
            )
            return

        length = self.length_var.get()

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        self.password_var.set(password)

        self.update_strength(password)

    def update_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 1

        if len(password) >= 12:
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in string.punctuation for c in password):
            score += 1

        if score <= 2:
            self.strength_label.config(
                text="🔴 Strength: Weak",
                fg=DANGER
            )

        elif score <= 4:
            self.strength_label.config(
                text="🟡 Strength: Medium",
                fg=WARNING
            )

        else:
            self.strength_label.config(
                text="🟢 Strength: Strong",
                fg=SUCCESS
            )

    def copy_password(self):

        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "Warning",
                "Generate a password first."
            )
            return

        pyperclip.copy(password)

        messagebox.showinfo(
            "Success",
            "Password copied to clipboard!"
        )


def main():

    root = tk.Tk()

    style = ttk.Style()
    style.theme_use("clam")

    PasswordGenerator(root)

    root.mainloop()


if __name__ == "__main__":
    main()
