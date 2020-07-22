import random
import string

def string_gen():
    letters = string.ascii_lowercase
    result = "".join(random.choice(letters)
    for i in range(5))  
    return result

print(string_gen())