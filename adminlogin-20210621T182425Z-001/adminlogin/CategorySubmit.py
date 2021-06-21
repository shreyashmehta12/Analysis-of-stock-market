import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
cgname=str(res.getvalue('cgname'))
cgicon=str(res.getvalue('cgicon'))
cgdes=str(res.getvalue('cgdes'))
sql="insert into category(cgname,cgdes,cgicon) values('"+cgname+"','"+cgdes+"','"+cgicon+"')"
insert=a.execute(sql)

if insert!=0:
	print("Record Inserted Successfully...")
else:
	print("failed")
conn.commit()
	