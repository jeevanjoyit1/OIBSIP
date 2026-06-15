import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional BMI Calculator")
        self.root.geometry("800x650")
        self.root.configure(bg="#EAF4F4")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        # Title
        title = tk.Label(
            self.root,
            text="BMI Calculator",
            font=("Segoe UI", 24, "bold"),
            bg="#EAF4F4",
            fg="#023047"
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="Calculate and Track Your Body Mass Index",
            font=("Segoe UI", 11),
            bg="#EAF4F4",
            fg="#555555"
        )
        subtitle.pack()

        # Input Frame
        input_frame = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="groove"
        )
        input_frame.pack(padx=20, pady=20, fill="x")

        tk.Label(
            input_frame,
            text="Name",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).grid(row=0, column=0, padx=15, pady=10)

        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=10)

        tk.Label(
            input_frame,
            text="Weight (kg)",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).grid(row=1, column=0, padx=15, pady=10)

        self.weight_entry = tk.Entry(input_frame, width=30)
        self.weight_entry.grid(row=1, column=1, pady=10)

        tk.Label(
            input_frame,
            text="Height (m)",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).grid(row=2, column=0, padx=15, pady=10)

        self.height_entry = tk.Entry(input_frame, width=30)
        self.height_entry.grid(row=2, column=1, pady=10)

        # Calculate Button
        tk.Button(
            self.root,
            text="Calculate BMI",
            font=("Segoe UI", 12, "bold"),
            bg="#219EBC",
            fg="white",
            activebackground="#126782",
            activeforeground="white",
            cursor="hand2",
            width=18,
            command=self.calculate_bmi
        ).pack(pady=10)

        # Result Label
        self.result_label = tk.Label(
            self.root,
            text="Enter details and click Calculate",
            font=("Segoe UI", 13, "bold"),
            bg="#EAF4F4"
        )
        self.result_label.pack(pady=10)

        # History Section
        history_frame = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="groove"
        )
        history_frame.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True,
            ipady=30
        )

        tk.Label(
            history_frame,
            text="BMI History",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#023047"
        ).pack(pady=10)

        columns = ("Name", "BMI", "Category")

        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 11, "bold")
        )

        self.tree = ttk.Treeview(
            history_frame,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=230, anchor="center")

        scrollbar = ttk.Scrollbar(
            history_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Bottom Buttons
        button_frame = tk.Frame(self.root, bg="#EAF4F4")
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Clear History",
            bg="#FB8500",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15,
            command=self.clear_history
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="Exit",
            bg="#D62828",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=15,
            command=self.root.quit
        ).grid(row=0, column=1, padx=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get().strip()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                raise ValueError

            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
                color = "#3A86FF"
            elif bmi < 25:
                category = "Normal Weight"
                color = "#2A9D8F"
            elif bmi < 30:
                category = "Overweight"
                color = "#FFB703"
            else:
                category = "Obese"
                color = "#D62828"

            self.result_label.config(
                text=f"BMI: {bmi}   |   Category: {category}",
                fg=color
            )

            self.tree.insert(
                "",
                "end",
                values=(name if name else "User", bmi, category)
            )

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid positive values for weight and height."
            )

    def clear_history(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.result_label.config(
            text="History Cleared",
            fg="black"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
