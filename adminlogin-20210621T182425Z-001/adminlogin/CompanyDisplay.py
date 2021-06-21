import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>My Stock Market</title>")
print("</head>")
print("<body>")

print("<center>")
print("<table border=1>")
print("<tr><td>Category ID</td><td>Category Name</td><td>Company Name</td><td>Company ISINcode</td><td>Company Icon</td><td>Company Website</td><td>Company Description</td><td>Company IPO Price</td><td>Company IPO Date</td><td>-----</td></tr>")
try:
	res=cgi.FieldStorage()
	cgid=str(res.getvalue('cgid'))
	if cgid=="None":	
		sql="select * from category ca,company co where ca.cgid=co.cgid";
	else:
		sql="select * from category ca,company co where ca.cgid=co.cgid and ca.cgid="+cgid;
except:
	print("Error...")


print(sql)
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td><img src="+str(i[7])+" height=100 width=100></td><td><a href="+str(i[8])+" target=_blank>"+str(i[8])+"</a></td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td>"+str(i[11])+"</td><td><a href=ComPrice.py?ISINcode="+str(i[6])+">Get Data</a></td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</html>")