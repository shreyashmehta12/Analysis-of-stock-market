import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ufnm=str(res.getvalue('ufnm'))
ulnm=str(res.getvalue('ulnm'))
dob=str(res.getvalue('dob'))
usergen=str(res.getvalue('usergen'))
umno=str(res.getvalue('umno'))
ueid=str(res.getvalue('ueid'))
ano=str(res.getvalue('ano'))
ac=str(res.getvalue('ac'))
ph=str(res.getvalue('ph'))
sign=str(res.getvalue('sign'))
userpwd=str(res.getvalue('userpwd'))

sql="insert into userreg(username,userdob,usergen,usermob,useremail,useraadhar,useraadharph,userphoto,usersign,userlogin,userpwd)values('"+ufnm+" "+ulnm+"','"+dob+"','"+usergen+"','"+umno+"','"+ueid+"','"+ano+"','"+ac+"','"+ph+"','"+sign+"','"+ufnm+umno+"','"+userpwd+"')"


insert=a.execute(sql)
if insert!=0:
	print("Record Inserted Successfully...  Your username is firstname+mobilenumber")
else:
	print("failed")
conn.commit()