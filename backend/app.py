from flask import Flask, jsonify

from fastapi import HTTPException

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


@app.get("/item")
def get_item(id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"id": id}


@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    
    return {"result": a / b}


# backend/app.py
import time

def process_payment():
    retries = 3

    for attempt in range(retries):
        success = False  # simulate failure

        if success:
            return {"status": "success"}

        time.sleep(1)

    return {"status": "failed after retries"}



# backend/app.py
@app.get("/orders")
def get_orders():
    orders = [
        {"id": 1, "item": "Shoes"},
        {"id": 2, "item": "Bag"}
    ]
    return {"orders": orders}
