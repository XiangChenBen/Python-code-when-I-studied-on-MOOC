import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "bankchenx@gmail.com"
password = "chen321xiang654"
receivers = ["xiang.chen6@students.mq.edu.au","benchen204@gmail.com"]
subject = "python"

msg = MIMEMultipart()
msg["From"] = sender
if len(receivers) > 1:
    msg["To"] = ",".join(receivers)
else:
    msg["To"] = receivers
msg["Subject"] = subject

body = "python is NO.1"
msg.attach(MIMEText(body,"plain"))

filename = "heart.png"
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment;filename= "+filename)


msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender, password)
print("login successfully")
server.sendmail(sender,receivers,text)
print("Email has been sent to ",receivers)
server.quit()

