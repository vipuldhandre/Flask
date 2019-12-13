from flask import Flask,render_template,request,redirect,url_for

from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for

obj = Flask(__name__)

obj.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost:3306/flask"

db = SQLAlchemy(obj)

class Student(db.Model):
    __tablename__ = "registration_table"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    email = db.Column(db.String(30))
    mobno = db.Column(db.String(30))
    
    def __init__(self,name,username,password,email,mobno):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.mobno = mobno
    
@obj.route("/")
def m1():
    return render_template("login.html")

# @obj.route("/registration")
# def registration():
#     return render_template("registration.html")

@obj.route("/log",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('t1')
        password = request.form.get('t2')
        stu = Student.query.filter(Student.username == username , Student.password == password).first()
        print(stu)
        if stu != None:
           return redirect(url_for("show"))
    return render_template("login.html")
        
        
    
@obj.route("/addinfo",methods=['GET','POST'])
def savestu():
    if request.method == "POST":
        name = request.form.get('k1')
        username = request.form.get('k2')
        password = request.form.get('k3')
        email = request.form.get('k4')
        mobno = request.form.get('k5')
        stu = Student(name,username,password,email,mobno)
        print(stu.name)
        print(stu.username)
        print(stu.password)
        print(stu.email)
        print(stu.mobno)
        db.session.add(stu)
        db.session.commit()
        print("SUCCESSSSSSSSSSS")
        return redirect(url_for("login"))
    else:
        return render_template("registration.html")

stu_list = []
@obj.route("/show")
def show():
     stu_list = Student.query.all()
     for i in stu_list:
         print(i.name)
         print(i.username)
         print(i.password)
         print(i.email)
         print(i.mobno)
     return render_template("success.html",li = stu_list)

@obj.route("/delete/<int:id>",methods=["GET"])
def  delete(id):
    stu = Student.query.get(id)
    db.session.delete(stu)
    db.session.commit()
    return redirect(url_for("show"))


@obj.route("/update/<int:id>",methods=["GET"])
def update(id):
    user1=Student.query.get(id)
    return render_template("update.html",user1=user1)

@obj.route("/updateuser",methods=["POST"])
def updateuser():
    user=Student(request.form.get('k1'),request.form.get('k2'),request.form.get('k3'),request.form.get('k4'),request.form.get('k5'))
    var_id=request.form.get('k')
    db.session.query(Student).filter(Student.id==var_id).update({Student.name:user.name,Student.username:user.username,Student.password:user.password,Student.email:user.email,Student.mobno:user.mobno})
    db.session.commit()
    return redirect(url_for('show'))
 
if __name__ == "__main__":
    db.create_all()
    obj.run(debug = True)