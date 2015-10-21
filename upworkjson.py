import json
import urllib2


class Players(object):
    def __init__(self):
        self.data = urllib2.urlopen(
            "https://raw.githubusercontent.com/BurntSushi/nflgame/master/nflgame/players.json"
        )
        self.resp = json.loads(self.data.read())

    def print_result(self):
        for x in self.resp.items():
            full_name = x[1][u"full_name"]
            try:
                position = x[1][u"position"]
                team = x[1][u"team"]
                print("{} - {} ({})".format(full_name, position, team))
            except KeyError:
                continue


if __name__ == "__main__":
    players = Players()
    players.print_result()
