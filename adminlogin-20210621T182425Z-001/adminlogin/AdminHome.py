import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
alid=str(res.getvalue('alid'))
apwd=str(res.getvalue('apwd'))

if alid=="admin" and apwd=="1234":
	print("<html>")
	print("<head>")
	print("<title>My Stock Market</title>")
	print("</head>")
	print("<body>")
	print("<center>")
	print("<table border=0>")
	print("<caption><font size =7>Admin Home Page</font></caption>")
	print("<tr><td><a href=CategoryInterface.py target= aa>Category Form</a><br>")
	print("<a href=CompanyInterface.py target= aa>Company Form</a><br>")
	print("</td><td><iframe src=CategoryInterface.py name=aa height=800 width=800 frameborder=0></iframe></td></tr>")
	print("<tr><td>Footer</td><td>Footer</td></tr>")
	print("</table>")
	print("</center>")
	print("</form>")
	print("</body>")
	print("</html>")
else:
	print("ID/Password Not Matched...")
conn.commit()	