#!/usr/bin/env python3
import shutil
import os
import emails
import psutil

#pip3 install psutil
cpu_percentage = psutil.cpu_percent(interval=5)
disk = shutil.disk_usage('/')
free_disk_percentage = (disk.free / disk.total) * 100
memory = psutil.virtual_memory()

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

if cpu_percentage > 0.8:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if free_disk_percentage < 20.0:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if (memory / 8) < 524288000:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

#TODO: Add the localhost - 127.0.0.1 resolve
