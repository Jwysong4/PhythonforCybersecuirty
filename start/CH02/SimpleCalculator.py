#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 10/01 by jaren
# Get two numbers from user
first_num = float( input("First number = ") )
operation = input("What is the operation (+,-,*,/,**,//,%) ")
second_num = float(input("Second number = ") )


# Add numbers and print answer
if operation == "+": 
    print(f"{first_num} + {second_num} = ", 
    first_num + second_num)
if operation == "-":
     print(f"{first_num} - {second_num} = ", 
     first_num - second_num)
if operation == "*":
     print(f"{first_num} * {second_num} = ", 
    first_num * second_num)
    if operation == "**":
    print(f"{first_num} ** {second_num} = ", 
    first_num ** second_num)
 if operation == "//":
    print(f"{first_num} // {second_num} = ", 
    first_num // second_num)
 if operation == "%":
     print(f"{first_num} % {second_num} = ", 
    first_num % second_num)
print("Done")
