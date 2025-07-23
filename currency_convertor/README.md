# 💱 Currency Converter Web App

A simple Flask-based web application that converts an amount from one currency to another using real-time exchange rates from `open.er-api.com`. This project was developed as part of my Python Internship (Slab 2).

---

## 🌟 Features

- Input amount, base currency, and target currency
- Real-time conversion using free exchange rate API
- Clean and user-friendly web interface
- Error handling for invalid input

---

## 🛠️ Tech Stack

- Python
- Flask
- requests (for HTTP API calls)
- HTML + basic CSS (for UI)

---

## 📂 Project Structure

Currency_Converter_App/
├── app.py                 # Main Flask application  
├── templates/  
│   └── index.html         # Frontend HTML page  
└── README.md              # Project description

---

## ▶️ How to Run

1. Clone or download the project  
2. Open terminal inside the folder and install dependencies:

   pip install flask requests

3. Run the App:

   python app.py

4. Visit: http://127.0.0.1:5000

---

## 💡 Example

**Input**: 100 USD → INR  
**Output**: 100 USD = 8325.60 INR (based on real-time rates)

---

## 🔗 API Used

- https://open.er-api.com/v6/latest (Free, No API key required)

---

## 🏁 Final Note

This is part of my Slab 2 submission for the Python Backend Internship program.  
I'm excited to keep building smarter apps using Python!
