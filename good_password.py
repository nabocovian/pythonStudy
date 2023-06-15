import random

name = input('Hello - ').title()
print(f"Hello, {name}! You've come to the right place for a secure password!")

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

def is_valid(num):
    """
    Check if the input is a valid number.

    Args:
        num (str): The input to be checked.

    Returns:
        bool: True if the input is a valid number, False otherwise.
    """
    if num.isdigit():
        return True
    else:
        return False

def is_yes(txt):
    """
    Check if the input indicates "yes".

    Args:
        txt (str): The input to be checked.

    Returns:
        bool: True if the input indicates "yes", False otherwise.
    """
    if txt.lower() in ['yes', 'y']:
        return True
    else:
        return False

print('Let\'s clarify some details about your password:')
q1 = input('How many passwords do you need?')
if is_valid(q1):
    q1 = int(q1)
else:
    print('Something went wrong...')
q2 = input('What is the length of each password?')
if is_valid(q2):
    q2 = int(q2)
else:
    print('Something went wrong...')
q3 = input('Do you want to use digits?')
if is_yes(q3):
    chars += digits
q4 = input('How about uppercase letters?')
if is_yes(q4):
    chars += uppercase_letters
q5 = input('Do you want to use lowercase letters?')
if is_yes(q5):
    chars += lowercase_letters
q6 = input('What about punctuation?')
if is_yes(q6):
    chars += punctuation
q7 = input('What about ambiguous characters?')
if is_yes(q7):
    for _ in 'il1Lo0O':
        chars = chars.replace(_, '')

def generate_password(length, chars):
    """
    Generate a password of the specified length using the given character set.

    Args:
        length (int): The length of the password.
        chars (str): The characters to be used for generating the password.

    Returns:
        str: The generated password.
    """
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

for i in range(q1):
    print(generate_password(q2, chars))

print(f'Here are your cool passwords, {name}! Take them and stay secure!')
print('If you need me again, feel free to come back! Goodbye!')
