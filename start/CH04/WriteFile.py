#!/usr/bin/env python3
# Sample script that writes to a file
# By Jaren 10/15

import os
#get current directory
script_path = os.path.abspath( __file__ )
script_dir = os.path.dirname( script_path )
#Build file path
file_path = os.path.join(script_dir , "testfile.txt")



# Create file object
f = open("file_path", "w")

# Write to file object
f.write("My name is Jaren\n")
f.write("I like football\n")
f.write("Hello World\n")

# Close file object
f.close()
