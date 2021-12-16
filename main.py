from words import words
from words import letters
import random

special_characters = ["!", "#", "$", "%", "&", "?", "@"]
numbers = "1234567890"


# filters out words that contain a dash or space
def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def create_password(length, caps, nums, specials):
    password = ""
    length_acquired = False
    fill_needed = length - nums
    while not length_acquired:
        word = get_valid_word()
        if len(word) <= fill_needed and fill_needed >= 3:
            password = password + word
            fill_needed = length - nums - len(password)
            if fill_needed == 0:
                length_acquired = True
        elif fill_needed < 3:
            password = password + random.choice(letters)
            fill_needed = length - nums - len(password)
            if fill_needed == 0:
                length_acquired = True
    # adds the specified amount of special characters to the password, and replaces letters
    i = 0
    while i < specials:
        random_num = random.randint(0, len(password) - 1)
        if password[random_num] not in special_characters:
            password = password.replace(password[random_num], random.choice(special_characters), 1)
            i += 1

    # capitalizes random letters in the password
    i = 0
    while i < caps:
        random_num = random.randint(0, len(password) - 1)
        if password[random_num] not in special_characters and password[random_num] not in numbers and password[random_num].islower():
            password = password.replace(password[random_num], password[random_num].upper(), 1)
            i += 1

    # adds the specified amount of numbers to the end of the password
    i = 0
    while i < nums:
        password = password + str(random.randint(0, 9))
        i += 1

    print("Password: " + password)


def run_program():
    print("Enter the specifications for your password")
    password_length = int(input("# of Characters: "))
    password_caps = int(input("# of Capital Letters: "))
    password_nums = int(input("# of Numbers: "))
    password_specials = int(input("# of Special Characters: "))

    if password_specials + password_caps + password_nums > password_length:
        print("Error: # of capital letters, numbers, and special characters exceeds the length of password")
        print("Increase length of password or decrease the # of capital letters, numbers, or special characters\n")
        run_program()
    else:
        create_password(password_length, password_caps, password_nums, password_specials)

run_program()
