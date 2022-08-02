from email.message import EmailMessage

message = EmailMessage()
sender = "luiseleazar4@hotmail.com"
recipient = "eleanv05@gmail.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = f'Greeting from {sender} to {recipient}'
body = """Hey there!,
I'm learning to send emails using Python!"""
message.set_content(body)

print(message)
