import os.path
import mimetypes
from email.message import EmailMessage

attachment_path = "email.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type, mime_subtype)
message = EmailMessage()

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
    maintype = mime_type,
    subtype=mime_subtype,
    filename=os.path.basename(attachment_filename))

print(message)
