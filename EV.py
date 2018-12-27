##################    Email-Validator   #######################
##########   CSE482: Internet and Web Technology  #############

import re
import string
import random
import socket
import smtplib
import dns.resolver

try:
    import httplib
except:
    import http.client as httplib

EMPTY = 100
VALID = 200
NO_INTERNET = 300
INVALID = 400
WRONG_INPUT = 500
BLOCKED = 600
INTERNAL_ERROR = 700
BLACK_LIST = 800


def main():
    with open("mail_address.txt", "r") as ins:
        email_list = []
        for line in ins:
            email_list.append(line.rstrip())
    if have_internet():
        if len(email_list) > 0:
            check(0, email_list)
        else:
            result('', EMPTY)
    else:
        result('', NO_INTERNET)


def check(position, email_list):  # values is of type 'list'
    addressToVerify = email_list[position]
    domain = addressToVerify.rsplit('@', 1);
    # print(domain)
    match = re.match('^[A-Za-z0-9-_]+(\.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*(\.[A-Za-z]{2,4})$',
                     addressToVerify)

    if match == None:
        result(email_list[position], WRONG_INPUT)
        check_position(position, email_list)
        # raise ValueError('Bad Syntax')
    else:
        records = dns.resolver.query(domain[1], 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)

        server = smtplib.SMTP(0)
        server.set_debuglevel(0)

        # creating random email
        random_email = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        random_email += '@domain.com'

        # SMTP Convrsation
        if match:
            try:
                server.connect(mxRecord)
                server.helo(host)
                server.mail(random_email)
                code, message = server.rcpt(str(addressToVerify))
                server.quit()
                # ASSUME 250 AS SUCCESS
                if code == 250:
                    result(email_list[position], VALID)
                elif code == 550:
                    result(email_list[position], BLOCKED)
                else:
                    result(email_list[position], INVALID)
                check_position(position, email_list)
            except smtplib.SMTPServerDisconnected as err:
                result(email_list[position], INTERNAL_ERROR)
                check_position(position, email_list)

            except smtplib.SMTPConnectError as err:
                result(email_list[position], BLACK_LIST)
                check_position(position, email_list)


def check_position(position, email_list):
    new_position = position + 1
    if new_position < len(email_list):
        check(new_position, email_list)
    else:
        print('THE END')


def result(email_address, val_response):
    if val_response == VALID:
        print(email_address + ' ::: ' + 'Valid')
    elif val_response == INVALID:
        print(email_address + ' ::: ' + 'Invalid')
    elif val_response == WRONG_INPUT:
        print(email_address + ' ::: ' + 'Invalid Input')
    elif val_response == BLOCKED:
        print(email_address + ' ::: ' + 'Blocked by mail server')
    elif val_response == NO_INTERNET:
        print('Please check your connection')
    elif val_response == INTERNAL_ERROR:
        print(email_address + ' ::: ' + 'Internal Error')
    elif val_response == BLACK_LIST:
        print(email_address + ' ::: ' + 'Internal Error. Maybe blacklisted')
    elif val_response == EMPTY:
        print('Empty list')
    else:
        print('Something went wrong')


def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


if __name__ == "__main__":
    main()
