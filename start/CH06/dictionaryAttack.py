#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 10/27
import os
import sys
from passlib.hash import sha512_crypt

#need to import passlib library
#pip install passlib
# functions
#hash the guess
def hash_password(hash_type, salt, password):
    #hash_salt = f"${hash_type}${salt}$"
    my_hash = sha512_crypt.using(rounds=5000).hash(password, salt=salt)
    return my_hash
#load dictionary file
def read_dictionary(file_name):
    #get current directory
    script_path = os.path.abspath( __file__ )
    script_dir = os.path.dirname( script_path )
    #Build file path
    file_path = os.path.join(script_dir , file_name)
    # Create file object
    f = open(file_path, "r")
    #read file object 
    dicitionary_file = f.readlines()
    # Close file object
    f.close()
    return dicitionary_file

# Get hash string
password_hash = input("What is the password hash: ")
# split hash
hash_parts = password_hash.split("$")
hash_type = hash_parts[1]
salt = hash_parts[2]

# Load dictionary file 
dictionary_list = read_dictionary("top10.txt")
# For each line in dictionary 
for guess in dictionary_list:
    guess = guess.strip()
    # hash the guess
    guess_hash = hash_password(hash_type, salt, guess)
    # is it a match
    if guess_hash == password_hash:
        # Print guess and quit
        print(f"Password found: '{guess}'")
        # How to quit script
        sys.exit(0)

print("Password not found")


