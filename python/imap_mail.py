import sys
import imaplib
import getpass
import email
import pdb

'''
__author__ : Tanigaiarassane D
__Date__ : 15 Jul 2016
https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
http://stackoverflow.com/questions/32193953/imap-error-when-accessing-gmail-from-command-line
'''
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "tanigai.dj@gmail.com"
EMAIL_FOLDER = "Inbox"

def connect_to_email_server(email_client, login_detail):
    "Return the email object after connecting to a imap server and login through username and password."

    mail = imaplib.IMAP4_SSL(email_client)
    try:
        mail.login(login_detail, getpass.getpass()) 
    except imaplib.IMAP4.error,err:
        print "Login failed - {} ".format(err)
        exit()
    return mail

def search_email(mail,folder="inbox"):

        print "Searching email ....{}".format(type(mail))
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        mail.select(folder) # connect to inbox.
        #result, data = mail.search(None, "ALL")

        result, data = mail.uid('search', None, "ALL") # search and return uids instead
        return data

def read_email(email_body):


        email_message_raw =email_body.decode('utf-8')
        email_message = email.message_from_string(email_body)
        #mail_message = str(email.message_from_string(raw_email)).decode("quoted-printable")
        print email_message['To']
 
        print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
 
        #print email_message.items() # print all headers
        print "=======Subject=========="
        print email_message["Subject"]
        print email_message["Body"]

        for part in email_message.walk():

                if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        print "------Body--------"
                        print body.decode('utf-8')
                if part.get('Content-Disposition') != None:
                        filename = part.get_filename()
                        print "Filename {}".format(filename)
                        if not filename:
                            filename = 'temp_attachment'
                        fp = open(filename, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close() 


if __name__ == "__main__":

	#mail = imaplib.IMAP4_SSL('imap.gmail.com')
	#mail.login('tanigai.dj@gmail.com', getpass.getpass())
	mail = connect_to_email_server('imap.gmail.com', 'tanigai.dj@gmail.com')
        mail.list()
        data = search_email(mail) 
        print data

	latest_email_uid = data[0].split()[-1]
	raw_email = data[0][1]
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	
	#result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
	read_email(data[0][1]) # here's the body, which is raw text of the whole email
