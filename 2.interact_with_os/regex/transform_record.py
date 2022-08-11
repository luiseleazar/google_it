"""working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. 
The phone number field contains U.S. phone numbers, 
and needs to be modified to the international format, with "+1-" in front of the phone number"""
import re

def transform_record(record):
    """Capture desire variables from text"""
    new_record = re.sub(r"(\w+\s\w+),(\d{3}-)", r"\1,+1-\2", record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
print(transform_record("Eli Jones,684-3481127,IT specialist"))
print(transform_record("Melody Daniels,846-687-7436,Programmer"))
print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Output should be:
# Charlie Rivera,+1-698-746-3357,Web Developer
# Sabrina Green,+1-802-867-5309,System Administrator
# Eli Jones,+1-684-3481127,IT specialist
# Melody Daniels,+1-846-687-7436,Programmer
