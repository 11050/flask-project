from flask import Flask, render_template
app = Flask(__name__)




@app.route('/jamol')
def buy_page():
    item2=[
        {'ID':'Sarvar','Name':'sarvar','Surname':'zokirvich','Price':'2112','University':'amity'},
        {'ID':'Jamolldin','Name':'jamolldin','Surname':'sodikov','Price':'2121','University':'wiut'},
        {'ID':'diyora','Name':'Diyorakhone','Surname':'dasbhsahb','Price':'5445','University':'inha'}
    ]
    return render_template('jamol.html',item2=item2)
@app.route('/')
def name_page():
    return render_template('trader.html')
@app.route('/home')
def say_hello():
    item2=[
        {'name':'jamolldin','surname':'sodikov','lastname':'sayfudin'},
        {'name':'diyora,','surname':'gozala','lastname':'johsmall'},
        {'name':'iroda','surname':'lopes','lastname':'johnbig'}
          ]

    return render_template('home.html',item2=item2)

@app.route('/earn')
def earn_page():
    box=[
        {'Currency':'USDT','Cryptocurrency':'bitcoin','Stock':'Nasdaq'},
        {'Currency':'EURO','Cryptocurrency':'Ethereum','Stock':'S&P 500'}

         ]
    return render_template('earn.html',box=box)

@app.route('/trader')
def trader_page():
    trader=[
        {'name':'future','type':'long','type2':'short'},
        {'name':'trading','type':'long','type2':'short'}
    ]
    return render_template('trader.html',trader=trader)