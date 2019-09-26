import smtplib
import email.message



toaddr = ['basis@indianoil.in',]
cc = ['kumars21@indianoil.in','saxena.shubham.2110@gmail.com']
bcc = ['basis@indianoil.in']
toaddrs = toaddr + cc + bcc
#print toaddrs
fromaddr = 'kumars21@indianoil.in'
message_subject = "Checking Mail Client"

message_text = "Hi, This is a test message \n You know that. <b> Hello </b>"

msg = email.message.Message()
msg['Subject'] = message_subject
msg['From'] = fromaddr
msg['To'] = ','.join(toaddr)
msg['Cc'] = ',' . join(cc)
msg['Bcc'] = ','.join(bcc)
msg.add_header('Content-Type','text/html')

msg.set_payload(message_text)

server = smtplib.SMTP('10.51.10.210', 55525)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
