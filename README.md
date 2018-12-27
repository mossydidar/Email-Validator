# email-verification-module
Repository for sharing group project files. 
CSE482 Group Project. 
Supervisor/Instructor: Mohammed Ashrafuzzaman Khan

Group members:

	Muhtadi Islam Akif
	Abir Roy
	Mostafa Didar Mahdi
	Asif Haider Khan

----------------------------------------------------------------------------

Python Version: 3.6.7

Library Dependencies :

	python dns.resolver
	python smtplib
	python socket
	python re
	python string
	python random
	python httplib or http.client


input: mail_address.txt (non-dynamic)

	Input file consists of the list of emails that are to be tested.	

output: terminal

----------------------------------------------------------------------------


Abstract:
Module runs on the terminal successfully upon the file being invoked from the 
terminal, if all the python library dependencies are met. Checks each email 
from the 'mail_address.txt', gives the respective outputs in the terminal.
 
Domain exceptions: Microsoft Servers (Live, Hotmail, Outlook). 
Exceptions are handled

