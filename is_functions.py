# Python Libs
import re
import requests

# Hashtag
def is_hashtag(text):
    word_list = text.split()
    for i in word_list:
        if i.startswith("#") and len(i) > 1:
            return True

# Greeting - Array inside Function
def is_greeting(text):
    greeting_list = ['hi', 'hello', 'hey', "what's up", "what's up?", "wassup?", "wassup", "hi there", "hello there"]
    for i in greeting_list:
        if i == text.lower():
            return True

# Call to PM - Array inside Function
def is_call_to_pm(text):
    greeting_list = ['message me', 'dm me', 'write me', "pm me", "contact me", "wassup?"]
    for i in greeting_list:
        if i in text.lower():
            return True

# Command
def is_command(text):
    word_list = text.split()
    for i in word_list:
        if i.startswith("/") and len(i) > 1:
            return True

# Username
def is_username(text):
    word_list = text.split()
    for i in word_list:
        if i.startswith("@") and len(i) > 5:
            return True

# Email
def is_email(text):
    if len(re.findall(".*@.*\..*", text)) > 0:
        return True

# Location - TODO: Bypassed for now
def is_location(event):
    return False

# URL
def is_url(text):
    word_list = text.split()
    if len(re.findall("\[.*\]\((.*)\)", text)) > 0:
        return True
    for i in word_list:
        if i.startswith('www.'):
            return True
        try:
            response = requests.get(i)
            return True
        except:
            try:
                response = requests.get('https://' + i)
                return True
            except:
                pass

# Phone
def is_phone(text):
    if len(re.findall("\+[0-9]{7,13}", text)) > 0:
        return True
    elif len(re.findall("[0-9]{2,4}-[0-9]{2,4}-[0-9]{2,4}", text)) > 0:
        return True
    elif len(re.findall("[0-9]{10,20}", text)) > 0:
        return True

# More than 1000
def is_more_than_1000(text):
    if len(text) > 1000:
        return True