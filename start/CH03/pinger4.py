#!/usr/bin/env python3
# Fourth example of pinging from Python
# By 

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(5 ** 0.5) +1, 2):
        if number % i == 0:
            return False
        return True
    def main():
        sample_numbers = [5, 12, 104743]
        for num in sample_numbers:
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
                try:
                    user_input = int(input("5:"))
                    if is_prime(user_input):
                        print(f"{user_input}is a prime number.")
                    else:
                        print(f"{user_input}is not a prime number.")
                except ValueError:
                    print("please enter a valid integer.")


if __name__ == "__main__":
    main()