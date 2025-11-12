#!/usr/bin/env python3
# Script that tells us how many people there are in space
#By 

import requests

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}


    response =requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Heres a dad joke for you:")
        print(data["joke"])
    else:
        print(f"Failed to fetch joke. Status code: {response.status_code}")
if __name__ == "__main__":
    get_dad_joke()
