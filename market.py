from flask import Flask, render_template
app = Flask(__name__)




@app.route('/jamol')
def buy_page():
    item2=[
        {'ID':'Sarvar','Name':'sarvar','Surname':'zokirvich','Price':'2112','University':'amity'},
        {'ID':'Jamolldin','Name':'jamolldin','Surname':'sodikov','Price':'2121','University':'wiut'},
        {'ID':'diyora','Name':'Diyorakhone','Surname':'Khodjaeva','Price':'5445','University':'inha'}
    ]
    return render_template('jamol.html',item2=item2)
@app.route('/')
def name_page():
    return render_template('order.html')
@app.route('/home')
def say_hello():
    item2=[
        {'name':'jamolldin','surname':'sodikov','lastname':'sayfudin'},
        {'name':'diyora,','surname':'khodjaeva','lastname':'sasa'},
        {'name':'iroda','surname':'karimova','lastname':'shoxsaroy'}
          ]

    return render_template('home.html',item2=item2)

@app.route('/earn')
def earn_page():
    box=[
        {'currency':'USDT','Cryptocurrency':'bitcoin','Stock':'Nasdaq'},
        {'currency':'EURO','Cryptocurrency':'Ethereum','Stock':'S&P 500'}

         ]
    return render_template('earn.html',box=box)