#!/usr/bin/env python3
# Third example of pinging from Python
# By 

number = int(input(":"))
divisor = int(input(": "))

def is_divisible(number, divisor):
    return number % divisor == 0
if is_divisible(number, divisor):
    print("Is divisible")