import requests
# import pandas as pd
import json
import csv

user_agent = 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
headers = {'User-Agent': user_agent}

url = 'http://china.nba.com/static/data/league/playerlist.json'
res = requests.get(url, headers = headers)
text = json.loads(res.text) # 等同于r=requests.get(url,headers=headers).json()

players = text['payload']['players']

print(players)

keys = ["code",
        "country",
        "countryEn",
        "displayAffiliation",
        "displayName",
        "displayNameEn",
        "dob",
        "draftYear",
        "experience",
        "firstInitial",
        "firstName",
        "firstNameEn",
        "height",
        "jerseyNo",
        "lastName",
        "lastNameEn",
        "leagueId",
        "playerId",
        "position",
        "schoolType",
        "weight"
        ]

file = open('nba.csv', 'w')

writer = csv.DictWriter(file, keys)

writer.writeheader()

for player in players:
    writer.writerow(player['playerProfile'])

file.close()