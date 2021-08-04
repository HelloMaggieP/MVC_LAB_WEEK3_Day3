from app import app
from flask import render_template
from models.order_list import *

@app.route("/orders")
def index():
    return render_template("index.html", orders=orders)

@app.route("/orders/<index>")
def get(index):
    return render_template("order.html", order=orders[int(index)])

