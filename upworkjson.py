import json
import urllib2

data = urllib2.urlopen(
    "https://raw.githubusercontent.com/BurntSushi/nflgame/master/nflgame/players.json"
)
resp = json.loads(data.read())
print(dir(resp))

for x in resp.items():
    full_name = x[1][u"full_name"]
    try:
        position = x[1][u"position"]
        team = x[1][u"team"]
        print("{} - {} ({})".format(full_name, position, team))
    except KeyError:
        continue
