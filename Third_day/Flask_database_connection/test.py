from flask import Flask,request,render_template,redirect,url_for

from flask_sqlalchemy import SQLAlchemy

obj = Flask(__name__)

obj.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/hero'

db = SQLAlchemy(obj)

class Student(db.Model):
    __tablename__ = 'Katrina'
    rollno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    addr = db.Column(db.String(30))
    
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        
@obj.route("/")
def m1():
    return render_template("reg.html")

@obj.route("/addstudent",methods = ["POST"])
def savestu():
    stu = Student(request.form.get('t1'),request.form.get('t2'))
    print(stu.name)
    print(stu.addr)
    db.session.add(stu)
    
    db.session.commit()
    return redirect(url_for("show"))

@obj.route("/show")
def show():
    studentlist = Student.query.all()
    return render_template("success.html",list = studentlist)
    

if __name__== '__main__':
    db.create_all()
    
    obj.run(debug=True)