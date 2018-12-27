The project is based on a fully software-based module that checks whether a given list of emails are
Valid or not. The whole project is written in Python language (version – 3.6.7). The given list of
emails are placed on a .txt file and are fed into the program through as the overall atomic ‘Input’ (nondynamic). The program takes the emails as input and iterates through each email, checking whether
the given emails are valid or not. The program uses various Python Libraries to match the emails,
open Sockets and SMTP conversations to pull out MX records and finally give the output on the given
list of emails as Valid or Invalid depending on some circumstances. The program runs on the terminal
and also delivers the ‘OUTPUT’ at the end of the Terminal.
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

