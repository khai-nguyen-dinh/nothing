import imaplib
import email
import re
from email.mime.multipart import MIMEMultipart

mail = imaplib.IMAP4_SSL('outlook.office365.com')
mail.login('bonnie4lde@hotmail.com', 'bbw9Lpz3w')
mail.list()
mail.select('inbox')
verify_link = ''
for i in range(1, 5):
    typ, msg_data = mail.fetch(str(i), '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(str(response_part[1]))
            text = str(msg).replace(r'=\r\n', '')
            try:
                verify_link = re.search('https://www.reddit.com/verification/(.+?)ref_source=3Demail', text).group()
            except AttributeError:
                found = ''
print(verify_link)
