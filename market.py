from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'T-shirt', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Shoes', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'dress', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)

@app.route('/Order')
def order_page():
    return render_template('order.html')
@app.route('/jamol')
def buy():
    return render_template('jamol.html')