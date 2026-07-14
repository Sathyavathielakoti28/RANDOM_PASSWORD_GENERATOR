import string
import secrets


def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Please select at least one character type.")

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password