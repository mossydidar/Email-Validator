import re

address = input("Enter an E-mail address: ") #"abir.roy@northsouth.edu" #checking the address
username, domain_name = address.split("@")
grammar = re.match('^[a-z0-9_]+(\.[a-z0-9_]+)*@[a-z0-9_]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',address)

if grammar == None :
    print('Invalid Input')
    raise ValueError('Bad Syntax')

import dns.resolver
records = dns.resolver.query(domain_name,'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

import socket 
import smtplib

#local server hostname 
host = socket.gethostname()

#SMTP lib setup (use debug level for full output)

server = smtplib.SMTP(0)
server.set_debuglevel(0)

#SMTP Convrsation

if grammar:

    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code,message = server.rcpt(str(address))
    server.quit()

#ASSUME 250 AS SUCCESS
if code == 250:
    print('Valid')
else:
    print('Invalid')