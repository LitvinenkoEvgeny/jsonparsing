import json
import urllib2
import sys


class Players(object):
    def __init__(self):
        self.data = urllib2.urlopen(
            "https://raw.githubusercontent.com/BurntSushi/nflgame/master/nflgame/players.json"
        )
        self.resp = json.loads(self.data.read())
        self.filename = sys.argv[1]

    def print_result(self):
        with open(self.filename, "a") as f:
            for x in self.resp.items():

                full_name = x[1][u"full_name"]

                try:
                    team = x[1][u"team"]
                except KeyError:
                    team = "FA"
                try:
                    position = x[1][u"position"]
                except KeyError:
                    position = "unknown"

                f.write(u"{} - {} ({})\n".format(full_name, position, team))


if __name__ == "__main__":
    players = Players()
    players.print_result()
