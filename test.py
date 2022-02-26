import math
import sys
from os import rename
import requests
import json
import html_to_json

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet("World"))
# print (greet('Thomas'))
# r = requests.get("https://theprogrm.com/the-progrm-2-2022-week-8-22-1/")
# print(r.status_code)

# Save the page content as sample.html
