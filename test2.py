from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anupam@97'
app.config['MYSQL_DB'] = 'sqltask'

mysql = MySQL(app)
@app.route('/anupam/insert11',methods=["POST"])
def inseration():
    try:
        if request.method=="POST":
            NAME=request.json["NAME"]
            address=request.json["address"]
            phoneno = request.json["phone"]
            membership = request.json["premiumcustomer"]
            print(NAME,address,phoneno,membership)
            cur=mysql.connection.cursor()
            cur.execute(f"INSERT INTO sqltask.customers VALUES('{NAME}','{address}',{phoneno},{membership})")
            mysql.connection.commit()
            return "insertion complete"
    except Exception as e:
            return str(e)
@app.route('/anupam/fetchall',methods=["POST"])
def fetchall():
    try:
        if request.method=="POST":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM customers")
            data=cur.fetchall()
            return jsonify((str(data)))
    except Exception as e:
        print(e)
@app.route('/anupam/delete',methods=["POST"])
def delete():
    try:
        if request.method=="POST":
            NAME=request.json["NAME"]
            print("NAME")
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM customers where NAME =%s",(NAME,))
            mysql.connection.commit()
            response=jsonify("deleted")
            return response
    except Exception as e:
        print(e)
@app.route('/anupam/update',methods=["POST"])
def update():
    try:
        if request.method == "POST":
            NAME = request.json["NAME"]
            address = request.json["address"]
            phoneno = request.json["phone"]
            membership = request.json["premiumcustomer"]
            print("NAME")
            cur = mysql.connection.cursor()
            cur.execute(f"UPDATE customers  set phone =%s ,NAME=%s,premiumcustomer=%s WHERE address=%s" , (phoneno,NAME,membership,address))
            mysql.connection.commit()
            return "Data updated"
    except Exception as e:
        print(e)
#








if __name__ == '__main__':
    app.run(debug=True)