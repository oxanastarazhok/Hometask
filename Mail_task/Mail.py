import smtplib
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sender", "-o", type = str, default ="testpython2015@yandex.ru",help="e-mail address of a sender")
parser.add_argument("--receiver","-r", type = str, default ="drednout.by@gmail.com", help= "e-mail adress of a receiver")
parser.add_argument("--subject", "-s" , type = str, default = "Test Message",  help="subject of a message")
parser.add_argument("--message",  "-m",type = str,default =" Hello!How are you?",help="text of of a message")
parser.add_argument("--host" , "-q", type = str, default = "smtp.yandex.ru", help="host")
parser.add_argument("--port", "-p", type = int,  default = 587,help= "port")
args = parser.parse_args()

from email.message import Message
from email.header import Header
subject = args.subject.decode('cp1251')
msg = Message()
msg.set_charset('utf-8')
h = Header(subject.encode('utf-8'), 'utf-8')
msg["Subject"] = h
text = args.message.decode('cp1251')
msg.set_payload(text.encode('utf-8'), 'utf-8')

smtp_obj = smtplib.SMTP(args.host, args.port)
smtp_obj.starttls()
smtp_obj.login(args.sender, "111111hi")
smtp_obj.sendmail(args.sender, args.receiver, msg.as_string())
smtp_obj.quit()