import secrets
import string

def generate_password(length, has_uppercase, has_digits, has_special_characters):
    safe_special_characters = "!@#$%^&*-_=+"
    password = ""
    characters = string.ascii_lowercase

    if has_uppercase:
        characters += string.ascii_uppercase
    if has_digits:
        characters += string.digits
    if has_special_characters:
        characters += safe_special_characters

    for i in range(length):
        password += secrets.choice(characters)
    
    return password

print("voici votre mot de passe : ", generate_password(20, True, True, True))







