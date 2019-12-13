'''
Created on 15-Oct-2019

@author: Vipul
'''
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def m1():
    print("Hi Vip's")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()