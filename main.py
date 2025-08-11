import secrets
import string

def generate_password():
    characters = string.ascii_lowercase
    password = ""

    for i in range(20):
        password += secrets.choice(characters)
    
    return password

print("voici votre mot de passe : ", generate_password())







