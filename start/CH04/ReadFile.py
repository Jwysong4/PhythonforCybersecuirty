#!/usr/bin/env python3
# Sample script that reads from a file
# By 

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
f = open("file_path", "r")

#read file object
print( f.read())

# Close file object
f.close()
