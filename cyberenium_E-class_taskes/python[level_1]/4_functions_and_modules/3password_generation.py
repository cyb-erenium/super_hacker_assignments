import random
import string

def password_generation():
    special_characters = string.punctuation
    numbers = string.digits
    letters = string.ascii_letters
    passwrd = special_characters + numbers + letters
    password = (random.choices(passwrd, k=12))
    pw = ""
    for i in password:
        pw += i
    print(f"Password: {pw}")    

password_generation()