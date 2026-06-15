# BMI Calculator

A professional GUI-based BMI (Body Mass Index) Calculator developed using Python and Tkinter. This application allows users to calculate BMI, view categorized results, and maintain a persistent history of calculations using a JSON file.

## Features

- Calculate BMI using weight (kg) and height (m)
- Color-coded BMI categories
- Attractive and user-friendly GUI
- Input validation and error handling
- Automatic date and time recording
- Scrollable BMI history table
- Persistent history storage using JSON
- Automatic history loading on startup
- Clear history functionality
- Object-Oriented Programming (OOP) implementation

## Technologies Used

- Python 3.x
- Tkinter
- JSON
- Datetime
- OOP Concepts

## Project Structure

```text
BMI_Calculator/
│
├── bmi_calculator.py
├── bmi_history.json
├── README.md
└── requirements.txt
```

## BMI Categories

| BMI Range | Category |
|------------|------------|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal Weight |
| 25.0 - 29.9 | Overweight |
| 30.0 and Above | Obese |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/BMI_Calculator.git
```

2. Navigate to the project directory:

```bash
cd BMI_Calculator
```

3. Run the application:

```bash
python bmi_calculator.py
```

## How to Use

1. Enter your name.
2. Enter your weight in kilograms (kg).
3. Enter your height in meters (m).
4. Click the **Calculate BMI** button.
5. View the BMI result and category.
6. Check the history section for previously saved records.
7. Use the **Clear History** button to remove all saved records.

## Sample Output

| Date & Time | Name | BMI | Category |
|------------|------|------|----------|
| 15-06-2026 09:30 | Jeevan | 22.86 | Normal Weight |
| 15-06-2026 09:35 | Arun | 28.12 | Overweight |

## JSON History Format

```json
[
    {
        "date": "15-06-2026 09:30",
        "name": "Jeevan",
        "bmi": 22.86,
        "category": "Normal Weight"
    }
]
```

## Future Enhancements

- BMI Trend Graph
- Export History to CSV/Excel
- Dark Mode Theme
- User Profile Management
- Health Recommendations Based on BMI

## Learning Outcomes

- GUI Development using Tkinter
- Object-Oriented Programming in Python
- File Handling with JSON
- Exception Handling
- Data Persistence Techniques
- User Interface Design

## Author

**Jeevan Joyit**

Oasis Infobyte Internship 2026

## License

This project is developed for educational and internship purposes.
## Author

Jeevan Joyit  
Oasis Infobyte Internship 2026
