import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
cgid=str(res.getvalue('cgid'))
cgname=str(res.getvalue('cgname'))
cgicon=str(res.getvalue('cgicon'))
cgdes=str(res.getvalue('cgdes'))
btn=str(res.getvalue('btn'))
print(cgdes)
print(cgname)
print(cgicon)

if btn=="Update":
	sql="update category set cgname='"+str(cgname)+"',cgdes='"+str(cgdes)+"',cgicon='"+str(cgicon)+"'where cgid="+str(cgid)
	insert=a.execute(sql)
	print(sql)
	if insert!=0:
		print("Record Updated Successfully...")
	else:
		print("Record Not Updated...")
else:
	sql="delete from category where cgid="+str(cgid)
	insert=a.execute(sql)
	if insert!=0:
		print("Record Deleted Successfully...")
	else:
		print("Record Not Deleted...")
		
conn.commit()		