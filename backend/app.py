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

import logging

def handle_payment(amount):
    """
    Process payment safely
    """
    if amount <= 0:
        raise ValueError("Invalid amount")
    return "Success"

def test_payment():
    assert handle_payment(10) == "Success"

def calculate_discount(price, discount):
    return price - (price * discount / 100)