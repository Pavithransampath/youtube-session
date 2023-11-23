from flask import Flask,render_template,request,session,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)

app.secret_key="pavi"

 
@app.route('/')
def home():
    conn=sql.connect("youtube.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("Select * from display where name=? ",(session["username"],))
    data=cur.fetchall()
    return render_template("index.html",thumbnaillist1=data)


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        Email=request.form.get("Email")
        password=request.form.get("Password")
        conn=sql.connect("youtube.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("Select * from login where name=?",(name,))
        data=cur.fetchone()
        if data:
            if  str(data["name"])==name and str(data["Password"])==password:
                session["username"]= data["name"]
        return redirect(url_for("home"))
    return render_template("login.html")



@app.route("/newUser",methods=["POST","GET"])
def newUser():
   if request.method=="POST":
      name=request.form.get("name")
      Email=request.form.get("Email")
      Password=request.form.get("Password")
      conn=sql.connect("youtube.db")
      conn.row_factory=sql.Row
      cur=conn.cursor()
      cur.execute("Insert into login(name,Email,Password) values(?,?,?)",(name,Email,Password))
      conn.commit()
      return redirect(url_for('home'))
   return render_template("newUser.html")


@app.route("/logout")
def logout():
    session.pop("name",None)
    return redirect(url_for("login"))
    
if __name__=="__main__":
    app.run(debug=True)





# from flask import Flask,render_template,request,redirect,session,url_for
# import sqlite3

# app=Flask(__name__)
# app.secret_key="key"

# @app.route("/",methods=["GET","POST"])
# def func():  
#     conn=sqlite3.connect("youtube.db")
#     conn.row_factory=sqlite3.Row
#     cur=conn.cursor() 
#     cur.execute("select * from display where userId=?",(session["userId"],))
#     data=cur.fetchall()
   
#     if request.method=="POST":
#      res =request.json
#      print(res)
#      cur.execute("insert into thumbnailList(VIDEOID,THUMBNAIL,PROFILEPIC,DESCRIPTION,UPLOADED_BEFORE,CHANNEL,VIEWS,USERID) values(?,?,?,?,?,?,?,?)",
#                 (res["videoID"],res["thumbnail"],res["profilePic"],res["description"],res["uploaded_before"],res["channel"],res["views"],session["userId"]))

#     conn.commit()
#     return render_template("index.html",thumbnailList=data)

# @app.route("/login",methods=["POST","GET"])
# def login():
#     if request.method=="POST":
       
#         Email=request.form.get("mobileno")
#         password=request.form.get("password")
#         conn=sqlite3.connect("youtube.db")
#         conn.row_factory=sqlite3.Row
#         cur=conn.cursor()
#         cur.execute("select * from login where Email=?",(Email,))
#         data=cur.fetchall()
#         print(data)
#         if data: 
#           if str(data["Email"])==Email and str(data["Password"])==password:
#            session["Email"]= data["Email"]
#            return "Login as"+" "+session["Email"]
#     return render_template("login.html")      

# @app.route("/logout")
# def logout():
#    session.pop("Email",None)
#    return redirect(url_for("login"))



# if __name__ == "__main__":
#     app.run(debug=True)






