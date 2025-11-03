#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By 
#name@domain.tld
import os


#ask which file to open
log_file = input("Which file to analyze? ")

#get current directory
script_path = os.path.abspath( __file__ )
script_dir = os.path.dirname( script_path )
#Build file path
file_path = os.path.join(script_dir , log_file )

#open log file
f= open(file_path, "r")

#read file line by line
while True:
    line = f.readline()
    if not line:
        break
    #look for 404
    if "404" in line:
        if "administrator" in line:
            if "%" in line:
        #print line
                print(line)


#close file
f.close()