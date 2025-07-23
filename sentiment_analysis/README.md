# 🧠 Sentiment Analysis Web App

This project is part of my Python Internship (Slab 2) and demonstrates a simple web application built with Flask that analyzes the sentiment of user-provided text. Using TextBlob, the app classifies the sentiment as Positive, Negative, or Neutral.

## 🔧 Features

- **User Input**: Users can type any sentence in a text box.
- **Sentiment Analysis**: The application uses TextBlob to determine the polarity of the text.
  - **Positive**: When the polarity is greater than 0.
  - **Negative**: When the polarity is less than 0.
  - **Neutral**: When the polarity is 0.
- **Web Interface**: A clean, responsive UI using a basic HTML template.
- **Flask Backend**: Serves the webpage and processes the sentiment analysis.

## 🛠️ Technologies Used

- **Python 3**
- **Flask** – A lightweight web framework.
- **TextBlob** – For performing sentiment analysis.
- **HTML & CSS** – For the frontend design.

## 📂 Project Structure

Sentiment_App/
├── app.py # Flask backend application
├── templates/
│ └── index.html # HTML template for the web app
└── README.md # This file

## ▶️ How to Run the App

1. **Clone or Download** the repository to your local machine.
2. **Install Dependencies**:
   Open a terminal inside the `Sentiment_App` folder and run:
   
   pip install flask textblob
   python -m textblob.download_corpora

   Run the Application:
   python app.py
   🔍 How It Works
Homepage: The web page presents a textarea where you can type your sentence.

Form Submission: After clicking "Analyze", the sentence is sent to the Flask backend.

Sentiment Calculation: Using TextBlob, the app calculates the sentiment polarity.

Result Display: The page is refreshed to display the original text along with the sentiment (Positive, Negative, or Neutral).

💡 Example
Input: "I love learning Python!"

Output: "Sentiment: Positive 😊"

🚀 Future Enhancements
Add more styling and responsive design using CSS frameworks like Bootstrap.

Integrate additional NLP libraries for more nuanced sentiment analysis.

Expand the app to support multiple languages.


   
