import imaplib
import email

imapHost = ''
imapUser = ''
imapPass = ''

# connecting to host via SSL
imap = imaplib.IMAP4_SSL(imapHost)

# logging in to servers
imap.login(imapUser, imapPass)

# Selecting the inbox of the logged in account
imap.select('Inbox')

msg, allmails = imap.search(None, 'ALL')

for num in allmails[0].split():
    msg, mails = imap.fetch(num, '(RFC822)')
    mail = email.message_from_bytes(mails[0][1])

    sender = mail['From']
    subject = mail['Subject']

    for paylod in mail.get_payload():
        row = paylod.get_payload()
        row = row.split('\n')
        message = row[0]
        break

    print('From: '+sender)
    print('Subject: '+subject)
    print('Message: '+message)


imap.close()
