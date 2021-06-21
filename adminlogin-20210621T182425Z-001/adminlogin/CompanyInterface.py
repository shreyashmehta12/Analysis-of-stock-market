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
print("<form action=CompanySubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Stock Company Registration </font></caption>")
print("<tr><td>Enter Category ID</td><td>")

#fill dropdown from database
print("<select name=cgid>")
sql="select * from category";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<option value="+str(i[0])+">"+str(i[1])+"</option>")
	
print("</select>")	
#end

print("</td></tr>")
print("<tr><td> Enter Company Name</td><td><input type=text name=cpname placeholder=\"Company Name\"></td></tr>")
print("<tr><td>Enter Company ISINcode</td><td><input type=text name=ISINcode placeholder=\"ISINcode\"></td></tr>")
print("<tr><td>Upload Company Icon</td><td><input type=file name=cpicon></td></tr>")
print("<tr><td>Enter Company Website</td><td><input type=web name=cpweb></td></tr>")
print("<tr><td>Enter Company Description</td><td><textarea name=cpdesc rows=4 cols=30></textarea></td></tr>")
print("<tr><td>Enter Company IPO Price</td><td><input type=number name=ipop></td></tr>")
print("<tr><td>Enter Company IPO Date</td><td><input type=date name=ipod></td></tr>")
print("<tr><td><input type=submit></td><td><input type=reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("<center>")
print("<table border=1>")
print("<tr><td>Category ID</td><td>Category Name</td><td>Company Name</td><td>Company ISINcode</td><td>Company Icon</td><td>Company Website</td><td>Company Description</td><td>Company IPO Price</td><td>Company IPO Date</td><td>update/delete</td></tr>")
sql="select * from category ca,company co where ca.cgid=co.cgid";
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td><img src="+str(i[7])+" height=100 width=100></td><td><a href=+"+str(i[8])+" target=_blank>"+str(i[8])+"</a></td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td>"+str(i[11])+"</td><td><a href= CompanyUpDe.py?ISINcode="+str(i[6])+">update/delete</a></td></tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")












