import mysql.connector as mysql
import datetime

conn = mysql.connect(host="localhost", user="root", password="", db="ecommerce")

def getNew():
    cur = conn.cursor(dictionary=True)
    qry = "SELECT name FROM `item` "
    cur.execute(qry)
    item = cur.fetchall()
    return [sub['name'] for sub in item]

def checkID(userid):
    cur=conn.cursor(dictionary=True)
    qry="SELECT * FROM `user` WHERE `id`= '{}'".format(userid)
    cur.execute(qry)
    user = cur.fetchone()
    return user

def savemsg(msg):
    cur = conn.cursor(dictionary=True)
    qry = "INSERT INTO `inquiry` (msg) VALUES('{}')".format(msg)
    cur.execute(qry)
    conn.commit()
    
