from flask import Flask,render_template,request

app = Flask(__name__)

class Student:
    def __init__(self,rollno,name,addr):
        self.rollno = rollno
        self.name = name
        self.addr = addr

@app.route("/",methods=['GET','POST'])
def m1():
     s1 = Student(1,"Vipul","KarveNagar")
     s2 = Student(2,"Piu","SaiNagar")
     list1 = [s1,s2]
     return render_template("index.html",li=list1)

 
@app.route("/login",methods=["GET",'POST'])
def login():
    if request.method == "POST":
        uname = request.form['t1']
        password = request.form['t2']
        print(uname)
        print(password)
        s1 = Student(1,"Vipul","KarveNagar")
        s2 = Student(2,"Piu","SaiNagar")
        list1 = [s1,s2]
    else:
         
         print("Please enter username and password")
         return render_template("success.html")
    return render_template("index.html",li=list1)

if __name__ == "__main__":
    app.debug = True
    app.run()
        

