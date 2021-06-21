import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ISINcode=str(res.getvalue('ISINcode'))
op=str(res.getvalue('op'))
hp=str(res.getvalue('hp'))
lp=str(res.getvalue('lp'))
cp=str(res.getvalue('cp'))
vol=str(res.getvalue('vol'))
pdate=str(res.getvalue('pdate'))
sql="insert into compri(ISINcode,op,hp,lp,cp,vol,pdate) values('"+ISINcode+"','"+op+"','"+hp+"','"+lp+"','"+cp+"','"+vol+"','"+pdate+"')"
insert=a.execute(sql)

if insert!=0:
	print("Record Inserted Successfully...")
else:
	print("failed")
conn.commit()
	