
import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

print("<head>")
print("<title> My Stock Market</title>")
print("</head>")
print("<body>")
print("<form action=CompriSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Company Stock Price </font></caption>")



print("<tr><td>Enter Company ISINcode</td><td><input type=text name=ISINcode placeholder=\"ISINcode\"></td></tr>")
print("<tr><td>Enter Company Open Price</td><td><input type=text name=op></td></tr>")
print("<tr><td>Enter Company High Price</td><td><input type=text name=hp></td></tr>")
print("<tr><td>Enter Company Low Price</td><td><input type=text name=lp</td></tr>")
print("<tr><td>Enter Company Close Price</td><td><input type=text name=cp></td></tr>")
print("<tr><td>Enter Company Volume</td><td><input type=text name=vol></td></tr>")
print("<tr><td>Enter Company Price Date</td><td><input type=text name=pdate></td></tr>")
print("<tr><td><input type=submit></td><td><input type=reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")
print("</body>")
print("</html>")












