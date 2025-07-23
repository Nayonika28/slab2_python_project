from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()

        # New API (no key required)
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "rates" in data:
            rate = data["rates"].get(to_currency)
            if rate:
                result = round(amount * rate, 2)
                return render_template('index.html', result=result, amount=amount,
                                       from_currency=from_currency, to_currency=to_currency)
            else:
                return render_template('index.html', error="Invalid target currency.")
        else:
            return render_template('index.html', error="Failed to fetch exchange rate.")
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
