#!/usr/bin/env python3
import shutil
import psutil
import socket

def check_disk_usage(disk):
    """Check if free space in disk is greater than 20%"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Check if CPU usage is less than 75%"""
    usage = psutil.cpu_percent(1)
    return usage < 75

def check_localhost():
    """Check if localhost is resolve as 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

if not check_disk_usage("/") or not check_cpu_usage() or not check_localhost():
    print("ERROR!")
else:
    print("Everything is OK!")
    