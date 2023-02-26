# HomeLifeHub by github.com/n0nexist
# Enumeration of Home&Life Hub routers from ZyXEL Communications Corp
import sys
import json
import requests


# Parses json from request
def parsejson(url):
    r = requests.get(url)
    result = json.loads(r.text)
    for x in result:
        print(f"{x} -> {result[x]}")    

# Logo
print("HomeLifeHub.py Enumeration script by n0nexist.github.io")

# Gets target from cmdline args
target = ""
try:
    target = sys.argv[1]
except:
    # Prints usage and exits with code 1
    print(f"Usage -> {sys.argv[0]} (router's ip address)")
    exit(1)
    
# Enumerates target
print(f"Enumerating '{target}'...\n")


# /getBasicInformation
print("> BASIC INFORMATION")
parsejson(f"http://{target}/getBasicInformation")

    
# /getRSAPublickKey
print("\n> RSA PUBLIC KEY")
parsejson(f"http://{target}/getRSAPublickKey")