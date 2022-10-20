from textwrap import indent
from charset_normalizer import CharsetMatches
import requests
import json

#this is where you would put your api key

chests = r.json()["items"]  #gets chests
print(json.dumps(r.json(), indent = 2))

for c in chests:
    if c["name"] == "Silver Chest" :
        print("Silver CHEST!!!")
    # elif c["name"] == "Silver Chest" :
        
    # elif c["name"] == "Golden Chest" :

    # elif c["name"] == "Gold Crate" :

    # elif c["name"] == "Magical Chest" :

    # elif c["name"] == "Giant Chest" :

    # elif c["name"] == "Legendary Chest" :

    # elif c["name"] == "Lightning Chest" :

    # elif c["name"] == "Mega Lightning Chest" :

    # elif c["name"] == "Legendary King's Chest" :

    # elif c["name"] == "Plentiful Gold Crate" :

    # elif c["name"] == "Overflowing Gold Crate" :

    # elif c["name"] == "Super Magical Chest" :

    # elif c["name"] == "Royal Wild Chest" :

    #Have not completed this updated version yet