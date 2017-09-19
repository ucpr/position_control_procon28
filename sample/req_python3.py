import urllib.request
import json


def main():
    url = "localhost:5000"
    res = urllib.request.urlopen(url)
    content = json.loads(res.read().decode("utf-8"))

    cv = content[0]["cv"]
    hcrs = content[1]["hcrs"]

    print("x:" + str(cv["x"]), "z:" + str(cv["z"]))
    print("distance:" + str(hcrs["distance"]))

if __name__ == "__main__":
    main()
