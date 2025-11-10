# paste code here
import requests

url = "http://api.open-notify.org/astros.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
#convert to python object
astros = response.json()

#print number of people 
print(f"There are currently {astros['number']} people in space")

#first person in space
print("The first person in space is{0}, on craft {1}".format( 
    astros["people"][0]["name"], 
    astros['people'][0]["craft']" ))

                                            
#second person in space

second_person = astros ["people"][1]
print("The second person in space is {0}, on craft{1}".format
    (second_person["name'], 
    second_person["craft"]))


    #loop through all astronauts
    for person in astros["people"]:
        print("{0} is on {1}".format(
            person["name"],
            person["craft"]
        ))