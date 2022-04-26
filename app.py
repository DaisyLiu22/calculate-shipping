"""
Simple "Hello, World" application using Flask
"""

from shipping_helper import total_amount
from shipping_helper import calculate_shipping
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/shipping_fee/', methods=["GET", "POST"])
def get_fee():
    if request.method == "POST":
        quantity = request.form["order_quantity"]
        total_cost = calculate_shipping(quantity)
        total_deposit = total_amount(quantity)
        return render_template("shipping_result.html", order_quantity=quantity, total_fee = total_cost, total_price = total_deposit)
    return render_template("shipping_form.html")


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)