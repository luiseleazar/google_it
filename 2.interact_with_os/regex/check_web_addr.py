"""Looks for a possible web page address on texts"""
import re

def check_web_address(text):
    """Looks for text that could be a web address"""
    pattern = r'.*[a-zA-Z0-9_][.][a-zA-Z]+$'
    result = re.search(pattern, text)
    return result is not None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
