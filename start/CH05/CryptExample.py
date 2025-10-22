#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Jaren 10/22

# install cryptography library
#pip instal crytography
from cryptography.fernet import Fernet

from end.CH05.CryptExample import fernet_create_key
#create function
#Fernet create key
def fermet_create_key():
    key = Fernet.generate_key()
    return key
#Fernet encrypt
def fernet_encrypt(key, plain_text):
    key_b = key.encode()
    plain_text_b = plain_text.encode()
    cipher_text_b = Fernet( key_b) .encrypt( plain_text_b )
    return cipher_text_b
#fernet Decrypt
def fernet_decrypt(key, cipher_text):
    key_b = key.encode()
    cipher_text_b = cipher_text.encode()
    plain_text_b = Fernet(key_b).decrypt(cipher_text_b)
    return plain_text_b

# Ask what to do
print("*" * 80)
print("Welcome to Fernet Encrpytion")
print("this script can create keys, encrypt, or decrypt")
task = input("what would you like to do (c/e/d)? ")[0].lower()


#if encrpyt 
if task == "e":

# get key and data 
    enc_key = input("what is the key: ")
plain_text = input("what is the message: ")
# call encrypt function
cipher_text_b = fernet_encrypt(enc_key, plain_text)
#print out results 
print("Your encrypted message is")
print(f"'{cipher_text_b.decode()}'")
# if decrypt 
elif task == "d":
#get key and data 
enc_key = input("what is the key: ")
cipher_text = input("what is the encrypted message")
# call decrpt function
plain_text_b = fernet_decrypt(enc_key, cipher_text)
#print out results
print("Your decrypted message is")
print(f"'{plain_text_b.decode()}'")

#if create key
elif task == "c":
#call create function
enc_key = fernet_create_key()
#print out results
enc_key = enc_key.decode()
print(f"Encryption key '{enc_key}' ")
else:
print("please answer c/e/d")


