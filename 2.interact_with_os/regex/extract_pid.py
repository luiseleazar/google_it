"""Extract PID using regex - capturing groups and scaping character"""
import re

def extract_pid(log_line):
    """Extract PID [number]"""
    pattern = r"\[(\d+)\]"
    result = re.search(pattern, log_line)
    return result[1]

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
print(extract_pid(log))
