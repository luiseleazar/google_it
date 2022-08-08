#!/usr/bin/env python3
import shutil
import os
import socket
import emails
import psutil

def get_disk_usage(disk):
    """Get disk usage in %"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def get_cpu_usage():
    """Get CPU usage in %"""
    usage = psutil.cpu_percent(1)
    return usage

def available_memory():
    mem = psutil.virtual_memory()
    return mem[1] / 8

def check_localhost():
    """Checks if localhost is resolved as 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

cpu_usage = get_cpu_usage()
disk_free = get_disk_usage('/')
memory = available_memory()

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if disk_free < 20.0:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if memory < 524288000:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
