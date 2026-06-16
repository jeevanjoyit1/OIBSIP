# 🔐 Password Generator

A modern GUI-based Password Generator built using **Python**, **Tkinter**, and **Pyperclip**. This application allows users to generate strong and customizable passwords with an intuitive and colorful user interface.

## 📌 Features

- Generate secure random passwords
- Adjustable password length (4–64 characters)
- Include/Exclude:
  - Uppercase Letters (A-Z)
  - Lowercase Letters (a-z)
  - Numbers (0-9)
  - Special Symbols
- Exclude specific characters manually
- Password strength indicator
- One-click copy to clipboard
- Modern and colorful GUI
- Responsive and user-friendly design

---

## 🖼️ User Interface

### Main Components

- Password Length Selector
- Character Type Options
- Exclude Characters Input
- Generate Password Button
- Password Display Area
- Password Strength Indicator
- Copy to Clipboard Button

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Pyperclip

---

## 📂 Project Structure

```text
Password-Generator/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
    └── app.png
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pyperclip
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🔒 Password Strength Criteria

The application evaluates password strength based on:

- Password Length
- Uppercase Characters
- Lowercase Characters
- Numbers
- Symbols

### Strength Levels

| Score | Strength |
|---------|-----------|
| 0 - 2 | 🔴 Weak |
| 3 - 4 | 🟡 Medium |
| 5 - 6 | 🟢 Strong |

---

## 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Object-Oriented Programming (OOP)
- GUI Development with Tkinter
- Event Handling
- Random Password Generation
- Clipboard Integration
- User Input Validation
- Password Strength Analysis

---

## 🚀 Future Enhancements

- Dark/Light Theme Toggle
- Password History
- Secure Password Generation using `secrets` module
- Save Passwords to File
- Custom Theme Support
- Export Passwords as TXT

---

## 👨‍💻 Author

**Jeevan Joyit**

Oasis Infobyte Internship 2026

---

## 📜 License

This project is created for educational and internship purposes.
