'''
Created on Oct 18, 2019

@author: user
'''
from flask import Flask,render_template,request,make_response

app=Flask(__name__)

@app.route("/")
def m1():
    return render_template("first.html")
    
@app.route("/first")
def second():
    
    fdata=request.args.get("t1")
    resp=make_response(render_template("second.html",fd=fdata)) 
    resp.set_cookie("fd",fdata,max_age=60*60*24*365)  
    
    return resp

@app.route("/second")
def third():
    
    fdata=request.args.get("t1")
    sdata=request.args.get("t2")
    print(request.cookies.get("fd"))
    return render_template("third.html",fd=fdata,sd=sdata)
        


@app.route("/third")
def display():
    
    fdata=request.args.get("t1")
    sdata=request.args.get("t2")
    tdata=request.args.get("t3")
    return  render_template("display.html",fd=fdata,sd=sdata,td=tdata)
        








if __name__=='__main__':
    app.run(debug=True)
