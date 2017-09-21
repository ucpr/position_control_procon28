# -*- coding: utf-8 -*-

import urllib2
import json


def main():
    #こいつはpython2です.
    url = "localhost:5000"
    res = urllib2.urlopen(url)
    content = json.loads(res.read().decode("utf-8"))

    cv = content[0]["cv"]
    print("x:" + str(cv["x"]), "y:" + str(cv["z"]))

    hcrs = content[1]["hcrs"]
    print("distance:" + str(hcrs["distance"]))

if __name__ == "__main__":
    main()
