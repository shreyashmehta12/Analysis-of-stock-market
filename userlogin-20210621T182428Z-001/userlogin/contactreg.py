import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
name=str(res.getvalue('name'))
mob=str(res.getvalue('mob'))
email=str(res.getvalue('email'))
msg=str(res.getvalue('msg'))


sql="insert into contactform(name,mob,email,msg)values('"+name+"','"+mob+"','"+email+"','"+msg+"')"


insert=a.execute(sql)
if insert!=0:
	print("Form Submitted...Thank You!! ")
else:
	alert('failed to submit')
conn.commit()