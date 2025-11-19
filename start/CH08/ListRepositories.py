#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By 
import os
import configparser

#function get Api key
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

#Get key and print to screen
token = get_api_key("github")
print(token)
   
