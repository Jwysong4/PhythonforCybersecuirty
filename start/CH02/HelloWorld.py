#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by Jaren 9/29
# ask user for a name
name = input("What is your name?")

#print hello to the user
print( 'Hello ' + name )
print( "Hello {0}".format(name) )
print( f"Hello {name}" )
print( "Hello", name)
message = "Hello " + name
print( message )
name = input("Today is going to be a great day!")
print("Hello", "there", "jaren", sep="$", end="blah")
