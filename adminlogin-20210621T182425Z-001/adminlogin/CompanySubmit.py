import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
cgid=str(res.getvalue('cgid'))
cpname=str(res.getvalue('cpname'))
ISINcode=str(res.getvalue('ISINcode'))
cpdesc=str(res.getvalue('cpdesc'))
cpicon=str(res.getvalue('cpicon'))
cpweb=str(res.getvalue('cpweb'))
ipop=str(res.getvalue('ipop'))
ipod=str(res.getvalue('ipod'))
sql="insert into company(cgid,cpname,ISINcode,cpicon,cpweb,cpdesc,ipop,ipod) values("+cgid+",'"+cpname+"','"+ISINcode+"','"+cpicon+"','"+cpweb+"','"+cpdesc+"','"+ipop+"','"+ipod+"')"
insert=a.execute(sql)

if insert!=0:
	print("Record Inserted Successfully...")
else:
	print("failed")
conn.commit()