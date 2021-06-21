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
print("<tr><td><b>ISIN code</b></td><td><b>Symbol</b></td><td><b>Date</b></td><td><b>Prev Close</b></td><td><b>Open Price</b></td><td><b>High Price</b></td><td><b>Low Price</b></td><td><b>Last Price</b></td><td><b>Close Price</b></td><td><b>Average Price</b></td><td><b>Total Trade Quantity</b></td><td><b>No. of Trades</b></td><td><b>OC Change</b></td><td><b>OC Percentage</b></td></tr>")
try:
	res=cgi.FieldStorage()
	ISINcode=str(res.getvalue('ISINcode'))
	sql="select * from data where ISINcode='"+ISINcode+"'";

except:
	print("Error...")


#print(sql)
display=a.execute(sql)
data=a.fetchall()
for i in data:
	print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td>"+str(i[7])+"</td><td>"+str(i[8])+"</td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td>"+str(i[11])+"</td>")
	oc=int(i[8])-int(i[4])
	per=(oc/int(i[8]))*100
	if oc>0:
		print("<td><font color=green>"+str(oc)+"</font></td><td><font color=green>"+str(per)+"</font></td>")
	elif oc<0:
		print("<td><font color=red>"+str(oc)+"</font></td><td><font color=red>"+str(per)+"</font></td>")
	else:
		print("<td>"+str(oc)+"</td><td>"+str(per)+"</td>")
	
	#print("<td>"+str(i[6])+"</td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</html>")
