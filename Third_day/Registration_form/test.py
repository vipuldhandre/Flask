from flask import Flask,render_template,request

obj = Flask(__name__)

class Registration:
    def __init__(self,name,username,password,email,mobno):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.mobno = mobno

user_list = []
        
@obj.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        uname = request.form.get('t1')
        password = request.form.get('t2')
        print(uname)
        print(password)
        return render_template("success.html")
    return render_template("login.html")
    
@obj.route("/registration",methods=["GET","POST"])
def registration():
    if request.method == "POST":
        name = request.form.get('r1')
        uname = request.form.get('r2')
        password = request.form.get('r3')
        email = request.form.get('r4')
        mobno = request.form.get('r5')
        user = Registration(name,uname,password,email,mobno)
        user_list.append(user)
        return render_template("login.html")
    return render_template("registration.html")
        
        
    
obj.run(debug=True)
        
    
    

    