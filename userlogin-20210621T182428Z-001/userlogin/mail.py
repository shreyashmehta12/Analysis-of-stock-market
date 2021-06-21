import pymysql
import cgi
import smtplib
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage();
userlogin=str(res.getvalue('ulid'))
useremail=str(res.getvalue('eid'))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("pythonstudents123@gmail.com","pythonstudents1")
sql="select useremail,userpwd from userreg where userlogin='"+str(userlogin)+"'"
insert=a.execute(sql)
if insert!=0:
	print("Password has been send to your mail successfully!")
else:
	print("failed to send/Incorrect details Try Again..,!")
data=a.fetchall()
for i in data:
	msg=str(i[1])
	server.sendmail("shreyashmehta12@gmail.com",str(i[0]),msg)
server.quit()


