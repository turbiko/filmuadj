import os
import secrets
import string

from slugify import slugify


def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits  # + string.punctuation
    print(characters)
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    print(random_string)
    return random_string

def filename_creation(instance,filename):
    split_tup = os.path.splitext(filename)
    file_name = slugify(split_tup[0]) + generate_random_string()
    file_extention = split_tup[1]
    result = file_name + file_extention
    print(result)
    return result