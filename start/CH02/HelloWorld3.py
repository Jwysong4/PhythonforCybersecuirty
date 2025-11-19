#!/usr/bin/env python3
# A more complex "Hello World" script in python with Inputs
# Created 

import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True, use_uppercase=True):
    chars = list(string.ascii_lowercase)
    if use_uppercase:
        chars += list(string.ascii_lowercase)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?/")
    if not chars:
        raise ValueError("No character types selected!")
    password = ''.join(random.choice(chars) for _ in range (length))
    return password

if __name__ == "__main__":
    print("Generated password:", generate_password(length=16))
