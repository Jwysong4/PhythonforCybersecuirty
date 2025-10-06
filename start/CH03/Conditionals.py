#!/usr/bin/env python3
# example workign with conditionals
#By 

score = int(input("What was your score? "))
if score > 90: score = 75
    print("You got a A!")
elif score > 80:
    print("You got a B")
elif score > 70:
    print("You got a C")
elif score > 60:
    print("You got a D")
else:
    print("you got an F")