import secrets
import string

def generate_password(length):
    characters = string.ascii_lowercase
    password = ""

    for i in range(length):
        password += secrets.choice(characters)
    
    return password

print("voici votre mot de passe : ", generate_password(20))







