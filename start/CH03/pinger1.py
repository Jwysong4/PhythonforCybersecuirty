#!/usr/bin/env python3
# First example of pinging from Python
# By Jaren 10/06/25

# Import things
import os
import platform

def ping_address(ip_address):
    # Find current OS
    current_os = platform.system().lower()
# Build ping command
# If windows
if current_os == "windows":
    ping_cmd = "ping -n 1 -w 2 " + ip_address + " > nul"
else: 
    ping_cmd = "ping -c 1 -W 2 " + ip_address + " > /dev/null 2>&1"

ping_cmd = "ping -c 1 -W 2 " + ip_address + " > /dev/null 2>&1"
print(ping_cmd) 
exit_code = os.system( ping_cmd )
return exit_code

# Execute ping command


# Assign IP to variable
Ip_prefix = "192.168.0."

#start loop
for final_octet in range(254):
    ip_addr = ip_prefix = str(final_octet =1)

    #call function
    exit_code = ping_addresses(ip_addr)

# Print results
if exit_code == 0:
    print(f"{ip_addr} is online")
else:
    print(f"{ip_addr} is NOT online")