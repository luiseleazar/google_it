import smtplib
import getpass
from email.message import EmailMessage

mail_server = smtplib.SMTP('localhost')
mail_server.set_debuglevel(1)
message = EmailMessage()
sender = "luiseleazar4@hotmail.com"
recipient = "eleanv05@gmail.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = f'Greeting from {sender} to {recipient}'
body = "Hey there!"
message.set_content(body)
sender = "luiseleazar4@hotmail.com"

mail_pass = getpass.getpass('Password: ')
mail_server.login(sender, mail_pass)

mail_server.send_message(message)
mail_server.quit()
