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
print("<form action=mail.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Forget Password</font></caption>")
print("<tr><td>Enter Login ID</td><td><input type=text name=ulid></td></tr>")
print("<tr><td>Enter Email ID</td><td><input type=email name=eid></td></tr>")
print("<tr><td><input type=submit value=\"Get Password\"></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")


print("</body>")
print("</html>")
