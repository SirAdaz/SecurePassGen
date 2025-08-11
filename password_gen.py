import secrets
import string

SAFE_SPECIAL_CHARACTERS = "!@#$%^&*-_=+"  # caractères sécurisés

def generate_password(length, has_uppercase, has_digits, has_special_characters):
    characters = string.ascii_lowercase  # toujours présent
    password_chars = []  # on stocke dans une liste pour pouvoir mélanger

    # Ajout des catégories activées
    if has_uppercase:
        characters += string.ascii_uppercase
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if has_digits:
        characters += string.digits
        password_chars.append(secrets.choice(string.digits))
    if has_special_characters:
        characters += SAFE_SPECIAL_CHARACTERS
        password_chars.append(secrets.choice(SAFE_SPECIAL_CHARACTERS))

    # Compléter jusqu'à atteindre la longueur demandée
    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))

    # Mélanger pour éviter un ordre prévisible
    secrets.SystemRandom().shuffle(password_chars)

    # Retourner en string
    return ''.join(password_chars)
