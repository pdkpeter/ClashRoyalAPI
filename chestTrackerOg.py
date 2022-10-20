# from textwrap import indent
# from charset_normalizer import CharsetMatches
import requests
import json
from datetime import datetime, timedelta, time

#this is where you would put the API key

chests = r.json()["items"] 
chests_hours = 0
first = dict() 
last_index = 0 
for c in chests:
  if c["index"] > 8:
    filler_chests = c["index"] - last_index - 1 
    chests_hours += filler_chests / 240.0 * 180 * 3 # Every 240 chests 180 are silver
    chests_hours += filler_chests / 240.0 * 52 * 8 # Every 240 chests 52 are golden
    chests_hours += filler_chests / 240.0 * 8 * 12 # Every 240 chests 8 are giant/magical
  last_index = c["index"] 
  if c["name"] == "Silver Chest":
    chests_hours += 3
  elif c["name"] == "Golden Chest":
    chests_hours += 8
  elif c["name"] == "Giant Chest": 
    chests_hours += 12
  elif c["name"] == "Magical Chest":
    chests_hours += 12
  elif c["name"] == "Epic Chest":
    chests_hours += 12
  elif c["name"] == "Legendary Chest":
    chests_hours += 24
  elif c["name"] == "Super Magical Chest":
    chests_hours += 24
  if c["name"] not in first:
    first[c["name"]] = chests_hours
first = sorted(first.items(), key=lambda x: x[1]) # Sort by time
now = datetime.now() #current time
for n in first: 
  print("Next %s: %s" % (n[0], (now + timedelta(hours=n[1])).strftime("%a, %d %b %Y %H:%M"))) #prints chest and time
