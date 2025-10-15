#!/usr/bin/env python3
# example workign with Functions
#By 


#Basic Function Example
def func1():
    print("I am a function")


# Function that adds 2 numbers
def add_two_nums(num_one, num_two):
    num_one = int(num_one)
    num_two = int(num_two)
    print(num_one + num_two)

#Function that does exponets
def exponent(number, power = 2):
    print(number ** power)

#Function that returns a value
def cube_number(number_one):
    value = number_one ** 3
    return value

func1()
add_two_nums(5,7)
add_two_nums(num_one=9, num_two=3)
add_two_nums(num_two=15, num_one=6)
exponent(7,4)
exponent(3)
return_val = cube_number(5)
print(return_val)


add_two_nums("5", 6)

