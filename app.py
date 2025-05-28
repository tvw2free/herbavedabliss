from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_products():
    with open("products.json", encoding='utf-8') as f:
        return json.load(f)

RAZORPAY_LINK = "https://rzp.io/rzp/gYo37OpN"

@app.route("/")
def index():
    products = load_products()
    return render_template("index.html", products=products)

@app.route("/buy/<int:pid>", methods=["GET", "POST"])
def buy(pid):
    products = load_products()
    if pid < 0 or pid >= len(products):
        return "Invalid product!", 404
    product = products[pid]
    if request.method == "POST":
        # (You can save customer info here if you wish)
        return redirect(RAZORPAY_LINK)
    return render_template("buy.html", product=product)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
