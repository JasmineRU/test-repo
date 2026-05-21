import requests
import json #json module added

response = requests.get("https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json")
if response.status_code == 200: #successful connection code number
    jsonData1 = response.json()
    songs = jsonData1["feed"]["results"]
    artistList = []
    songNames = [] #creates lists to hold data
    for song in songs:
        artistList.append(song["artistName"])
        songNames.append(song["name"]) #iterates through dictionary, addes reqquested element to respective list
    print("Names of Top 100 Artists:", artistList)


    print("\nTitles of Top 100 Songs:", songNames)
else:
    print("Failed to connect to API")
    
