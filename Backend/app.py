from flask import Flask, jsonify
from flask import Flask, request , jsonify ,url_for ,flash, redirect;

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS, cross_origin
import psycopg2
import os
import time

time.sleep(20)

app = Flask(__name__)
cors = CORS(app)
app.config["SECRET_KEY"] = "pogchampsecret"
app.config["CORS_HEADERS"] = "Content-Type"


DB_HOST = "localhost"
DB_NAME = "packlotus"
DB_USER = "postgres"
DB_PASS = "123456789"
# conn=psycopg2.connect(database="packlotus", user="postgres", password="123456789", host="localhost", port=5431)
conn = psycopg2.connect("dbname=packlotus user=postgres host=localhost password=123456789")
# conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
app.config["SQLALCHEMY_DATABASE_URI"]=f"postgresql://postgres:123456789@postgres:5432/packlotus"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
db = SQLAlchemy(app)

@app.route("/")
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT row_to_json(user1) FROM (SELECT id, username,message,comments FROM user1 ) user1 ')
  
    data=cur.fetchall()
    print(data)
    return data
    
@app.route('/add_blog',methods=['POST'])
def add_blog():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        username =request.json['username']
        message= request.json['message']
        comments=[]
        cur.execute("INSERT INTO user1 (username , message ,comments) VALUES (%s,%s,%s)",(username,message,comments))
        conn.commit()
        flash('Blog addedd successfully')
        # return redirect(url_for('index'))
        s= "SELECT * FROM user1"
        cur.execute(s)
        data=cur.fetchall()

        return jsonify({'status':data,'msg':'message added successful'})

@app.route('/add/comment/<id>',methods=['POST','GET'])
def get_blog(id):
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM user1 WHERE id = %s',(id))
    data=cur.fetchall()
    cur.close()
    print(data)
    return data[0]

@app.route('/update/<id>',methods=['POST'])
def update_blog(id):
    if request.method=='POST':
        comment=request.json['comment']
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # cur.execute('SELECT * FROM user1 WHERE id = %s',(id))
        cur.execute('SELECT  row_to_json(user1) FROM user1 WHERE id = %s',(id))
        data=cur.fetchall()
        # cur.close()
       
        # print(data[0][0]['comments'])
        data[0][0]['comments'].append(comment)
  
        data1=data[0][0]['comments']
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("UPDATE user1 SET comments =  %s WHERE id = %s",(data1,id))
        flash('comment added')
        return ['comment added successfully',data]


if __name__=='__main__':
    # app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True,port=5500)
    app.run(host="0.0.0.0", port= 8000, debug=True)
