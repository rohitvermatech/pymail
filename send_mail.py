from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = ''
port = 587
username = ''
password = ''


server = smtplib.SMTP(host, port)  # SMTP HOST Config
server.starttls()
server.login(username, password)


msg = MIMEMultipart()

msg['From'] = ''
msg['To'] = ''
msg['Subject'] = ''
message = ''

msg.attach(MIMEText(message, 'plain'))

server.sendmail(msg['From'], msg['To'], msg.as_string())  # send mail

print('Mail sent to: '+msg['To'])
print('Message: '+message)

server.quit()
