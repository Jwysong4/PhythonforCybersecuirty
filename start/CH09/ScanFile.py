#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By 11/19/25
import os
import configparser
import hashlib
import requests
import sys
#functions

#check for report
def vt_get_report(api_key, file_hash):
    url = "https://www.virustotal.com/api/v3/files/" + file_hash
    payload={}
    headers = {
    'accept' : 'application/json',
    'x-apikey': api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload, )
    if response.status_code == 200:
        results = response.json()
        return results
    

#upload file for scan
def vt_upload_file(api_key, file_path):
    pass
#check scan status
def vt_get_scan_status(api_key, url):
    pass
#get API key
def get_api_key(key_name):
    #get location of secret files
    home_dir = os.path.expanduser("~")
    secrets_file = os.path.join(home_dir, "secrets.ini")
    #create configparser object, load file 
    config = configparser.ConfigParser()
    config.read(secrets_file)
    #get key and return
    api_key = config["APIkeys"][key_name]
    return api_key
# hash the file 
# from https://www.geeksforgeeks.org/python/python-program-to-find-hash-of-file/
def hash_file(file_path):
    pass
def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()
#get file to scan 
target_file = input("which file to scan? ")
#get file hash
file_hash = hash_file(target_file)
#get report
token = get_api_key("virustotal")
file_report = vt_get_report(token, file_hash)
#if report 
if file_report:
# print results and quit
    data = file_report["data"]
    attributes = data["attributes"]
    last_stats = attributes["last_analysis_stats"]
    print("-"* 80)
    print("file_results")
    print(f"\tmalicious: {last_stats['malicious']}")
    print(f"\tsuspicious: {last_stats['suspicious']}")
    print(f"\tundetected: {last_stats['undetected']}")
    sys.exit()
#else 
else:
    print("file not scanned")
#upload file 

#wait 30 seconds 


#check scan status 

#print results and quit 



