import os
import datetime
import reports
import emails

path = '/mnt/c/Users/luise/Documents/dev/dev_wsl/google_it/6.automating_real_tasks/final_project/assets/'
file_list = os.listdir(path)
info_list = []

for file in file_list:
    with open(path +file, "r", encoding="utf-8") as txt:
        if file.endswith("txt"):
            name = txt.readline()
            weight = txt.readline()
            info_list.append((name, weight))

info = ""
for line in info_list:
    info += '<br/>' + 'name: ' + line[0] + "<br/>" + 'weight: ' + line[1] + '<br/>'
filename = 'processed.pdf'
today = datetime.datetime.today()
title = f'Processed Update on {today}'
body = info

if __name__ == "__main__":
    reports.generate_report(filename,title, body)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body,"processed.pdf")
    emails.send_email(message)