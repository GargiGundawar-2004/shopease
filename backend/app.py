from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ShopEase API"})

if __name__ == "__main__":
    app.run(debug=True)

# backend/app.py
def process_payment(amount):
    if amount <= 0:
        return "Invalid amount"
    return "Success"