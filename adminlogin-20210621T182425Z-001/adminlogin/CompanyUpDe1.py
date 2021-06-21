import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='',db='stock')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ISINcode=str(res.getvalue('ISINcode'))
cgid=str(res.getvalue('cgid'))
cpicon=str(res.getvalue('cpicon'))
cpdesc=str(res.getvalue('cpdesc'))
cpname=str(res.getvalue('cpname'))
cpweb=str(res.getvalue('cpweb'))
ipop=str(res.getvalue('ipop'))
ipod=str(res.getvalue('ipod'))
btn=str(res.getvalue('btn'))




if btn=="Update":
	sql="update company set cgid='"+str(cgid)+"',cpname='"+str(cpname)+"',cpicon='"+str(cpicon)+"',cpdesc='"+str(cpdesc)+"',cpweb='"+str(cpweb)+"',ipop='"+str(ipop)+"',ipod='"+str(ipod)+"'where ISINcode="+"'"+str(ISINcode)+"'"
	insert=a.execute(sql)
	print(sql)
	print(cgid)
	if insert!=0:
		print("Record Updated Successfully...")
	else:
		print("Record Not Updated...")
else:
	sql="delete from company where ISINcode="+"'"+str(ISINcode)+"'"
	insert=a.execute(sql)
	if insert!=0:
		print("Record Deleted Successfully...")
	else:
		print("Record Not Deleted...")
		
conn.commit()		