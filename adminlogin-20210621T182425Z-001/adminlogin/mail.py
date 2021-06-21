import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "pythonstudents123@gmail.com"
toaddr = "shreyashmehta12@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body,'plain'))


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"pythonstudents1")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()