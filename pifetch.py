#!/usr/bin/python3

import requests
import json

url = "https://api.pi.delivery/v1/pi?start={}&numberOfDigits=1000"

with open("pydigits.json", "w") as f:
    for i in range(0, 10000):
        print(url.format(i*1000))
        r = requests.get(url.format(i*1000))
        f.write(json.dumps(r.json()))
        f.write("\n")


