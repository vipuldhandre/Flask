from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def m1():
    print("Hello")
    return render_template("success.html")

@app.route("/home/<int:id>")
def m2(id):
    print(id)
    print("Hello")
    return render_template("success.html",id=id)

if __name__ == "__main__":
    app.run()
