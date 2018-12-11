import re
addressToVerify = input("Enter e-mail: ")# "fusion_mos@yahoo.com" #checking the address
match = re.match('^[a-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',addressToVerify)

if match == None :
    print('Invalid Input')
    raise ValueError('Bad Syntax')

import dns.resolver
records = dns.resolver.query('gmail.com','MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

import socket 
import smtplib

#Get local server hostname
host = socket.gethostname()

#SMTP lib setup (use debug level for full output)

server = smtplib.SMTP(0)
server.set_debuglevel(0)



if (match):
    #SMTP Convrsation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

#ASSUME 250 AS SUCCESS
if code == 250:
    print('Valid')
else:
    print('Invalid')
