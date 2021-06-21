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
print("<tr><td>Category ID</td><td>Category Name</td><td>Category Description</td><td>Category Icon</td><td>Company Display</td></tr>")
sql="select * from category";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td><img src=myimg/dhoni.jpg alt=Dhoni"+str(i[3])+" height=100 width=100></td><td><a href=CompanyDisplay.py?cgid="+str(i[0])+">Company Display</a></td></tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")
