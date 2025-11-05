#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most frequent users
# By 

#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By 
import os
import re

#ask which file to open
log_file = input("Which file to analyze? [access.log]? ")

#get current directory
script_path = os.path.abspath( __file__ )
script_dir = os.path.dirname( script_path )
#Build file path
file_path = os.path.join(script_dir , log_file )

#open log file
with open(file_path, "r") as f:
    log_lines = f.readlines()

#Setup regex pattern
search_pattern = r"^(\d+\.\d+\.\d+.\d+)\ "
result_dict = {}

#loop through log
for line in log_lines:
    #search for the pattern
    match = re.search(search_pattern, line)
    if match:
        result=match.group(1)
        if result in result_dict.keys():
            result_dict[result] += 1
        else:
            result_dict[result] = 1

print(result_dict)

#sort by most frequent
for w in sorted(result_dict, key=result_dict.get, reverse=False):
    print(w, result_dict[w])




