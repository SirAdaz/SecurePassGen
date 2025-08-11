import secrets
import string

safe_special_characters = "!@#$%^&*-_=+" # caractères sécurisés

def generate_password(length, has_uppercase, has_digits, has_special_characters):
    password = "" # mot de passe généré
    characters = string.ascii_lowercase # caractères disponibles

    if has_uppercase: # si l'utilisateur veut des majuscules
        characters += string.ascii_uppercase
    if has_digits: # si l'utilisateur veut des chiffres
        characters += string.digits
    if has_special_characters: # si l'utilisateur veut des caractères spéciaux
        characters += safe_special_characters

    for i in range(length): # génération du mot de passe
        password += secrets.choice(characters)
    
    return password

print("voici votre mot de passe : ", generate_password(20, True, True, True)) # appel de la fonction







