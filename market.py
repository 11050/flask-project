from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    jamol = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('home.html',jamol=jamol)





@app.route('/market')
def market_page():
    items= [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id':4,'name':'samsung','barcode':'212112121','price':31}
    ]
    return render_template('market.html', items=items)

@app.route('/apple')
def jamol_say():
    return f'nima gap'








@app.route('/about/<username>')


def toliq_ism_yasa(username):
    return f'<h1>Mani ism {username}Jamollldin</h1>'
@app.route('/home')
def say_hello():
    return '<h1>say JAmol</h1>'

@app.route('/jamol/<username>')
def say_hellos(username):
         return f'<p>sajdnasdasn {username}'

@app.route('/name/<fullname>')

def agant(fullname):
    return f'<p>sadsa{fullname}</p>'
