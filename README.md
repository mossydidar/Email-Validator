## Email Validator 
This repository contains all the information about how to check a bulk of E-mails for validity by sending requests to the respective mail servers and receiving those requests and outputting them in a terminal application.
   

----------------------------------------------------------------------------

## Python Version: 3.6.7

## Library Dependencies :

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


## Abstract:
Module runs on the terminal successfully upon the file being invoked from the 
terminal, if all the python library dependencies are met. Checks each email 
from the 'mail_address.txt', gives the respective outputs in the terminal.
 
Domain exceptions: Microsoft Servers (Live, Hotmail, Outlook). 
Exceptions are handled


## Core Software Requirements
The project primarily requires resources which can interact with mail services and their respective
domains. Open Source programming languages such as Java and Python have numerous Libraries,
functionalities and other similar resources that can be used to read and/or write to files or the console,
manipulate strings and similar data types and data structures, match regular expressions, open and
utilize sockets, get domain information on mailing services. We also require resources that can utilize
some operations of the Simple Mail Transfer Protocol. Once all of the resources are accommodated,
the project implementation can be initiated.

## Physical Dependencies:

The physical dependencies or requirements include the availability of a functional Computer that has
a favorable Operating System and an environment that can run programs of such nature. Additional
physical Dependencies include an active internet connection.

## Resourcing similar projects
For ease and reliability of our implementation, we also need to resource out similar projects or works
done on email verification/validation on other languages or platforms, usually open-source. An
example code (undeveloped) has been resourced from an open source blog from
www.emailhippo.com.

## Implementation
Programming Language used in the implementation of the project upon a majority of opinion was
chosen to be Python (version 3.6.7). Python is a high-level, general purpose programming language,
that provides numerous libraries among which a few of them are of great importance to this project.

## Python DNS Resolver Library:
DNS Resolver is an API of Python that enables a program to collect resolved records about
a specific domain. The domain of a e-mail address is parsed out of the string and then is
used to retrieve the MX records of that specific domain.

## Python Simple Mail Transfer Protocol Library:
Python smtplib is a module that allows the instantiation of a SMTP Client Session object
that can be used to send or receive emails to any machine that has a SMTP listener daemon
Here, the module is used to create an object ‘Server’ that does a ‘SMTP Conversation’,
connecting and retrieving Mail Exchange (MX) records, matching and in turn receiving a
code that implies whether an address is valid or not.

## Python Socket Library:
The Socket module allows to instantiate a socket object, providing access to a socket
interface. Here, the socket module is used to retrieve the host name required for the
validation to take place.

## Python Regular Expressions Library:
A python module that is used to match string and byte patterns; here the module is used
match the given e-mail (input) to check if the address is a regular expression.

## Python Random Library:
A python module that generates random characters and numbers. The random module is
required to generate a random e-mail address that is sent SMTP object before receiving a
validation code.

## Python HTTP Client Library:
A module of python that allows to instantiate a HTTP or HTTPS Client side object. For
this project, the module is only used to check if the internet connection is active or not
prior to any kind of checking.


## Source Code implementation -

The implementation of the whole project has been compiled to a single Python file. On run-time, the
program takes inputs from another file (mail_address.txt) which contains the list of the e-mails to
be validated. Upon being read and stored into a ‘List’, each e-mail is then checked through function
calls recursively. After each successful check has been done, the results (val_response) are then
printed on the console alongside each e-mail.

