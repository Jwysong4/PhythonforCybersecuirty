#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By 
import hashlib
import requests
def SHA1(msg):
    return hashlib.sha1(msg.encode()).hexdigest()
def test_password(prefix):
    url = "https://api.pwnedpasswords.com/range/"+ prefix
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    #save resonse to varaible
    raw_text= response.text
    #split on crlf
    raw_list = raw_text.split("\r\n")
    #seperate on :, save to dictionary
    raw_dict = {}
    for item in raw_list:
        split_result = item.split(":")
        raw_dict[split_result[0]]= split_result[1]
    #return to dictionary
    return raw_dict
#ask user for password
password = input("Password: ")

#hash the password
pass_hash = SHA1(password)
pass_hash = pass_hash.upper()

#split the password
hash_prefix = pass_hash[0:5]
hash_suffix = pass_hash[5:]

#call api
results = test_password(hash_prefix)

#search your results
if hash_suffix in results.keys():
    print(f"Password is bad, it has been found {results[hash_suffix]} times")
else:
    print("Password is safe")
