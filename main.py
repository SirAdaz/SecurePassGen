import secrets
import string

def generate_password(length):
    safe_special_characters = "!@#$%^&*()-_=+"
    password = ""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + safe_special_characters

    for i in range(length):
        password += secrets.choice(characters)
    
    return password

print("voici votre mot de passe : ", generate_password(20))







