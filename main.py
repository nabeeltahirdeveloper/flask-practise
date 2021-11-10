from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route('/')
def products():
    return render_template('index.html')
@app.route('/pending-money')
def pendingmoney():
    return render_template('pending-money.html')
@app.route('/processed-money')
def processedmoney():
    return render_template('processed-money.html')
@app.route('/account-money')
def accountmoney():
    return render_template('account-money.html')

if __name__=="__main__":
    app.run(debug=True)