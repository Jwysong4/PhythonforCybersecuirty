#!/usr/bin/env python3
# First example of pinging from Python
# By Jaren 10/06/25

# Import things
import os
import platform

# Assign IP to variable
Ip_addr = "127.0.0.1"

# Find current OS
current_os = platform.system().lower()

# If windows
if current_os == "windows":
    ping_cmd = "ping -n 1 -w 2 " + Ip_addr + " > nul"
else: 
    ping_cmd = "ping -c 1 -W 2 " + Ip_addr + " > /dev/null 2>&1"

#print(ping_cmd)


# Build ping command
ping_cmd = "ping -c 1 -W 2 " + Ip_addr + " > /dev/null 2>&1"
print(ping_cmd) 

# Execute ping command
exit_code = os.system( ping_cmd )
# Print results
print( exit_code )
if exit_code == 0:
    print(f"{Ip_addr} is online")
else:
    print(f"{Ip_addr} is NOT online")

#
