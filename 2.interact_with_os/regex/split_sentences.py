"""Split sentences every . ! or ?"""
import re

def split_sentence(text: str) -> list:
    """Returns a list of sentences in a text"""
    pattern = r"[.!?]"
    result = re.split(pattern, text)
    return result

random_text = "Hello World! I'm learning Python. Do you want to join me? Come on"
print(split_sentence(random_text))
