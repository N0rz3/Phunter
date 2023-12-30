from .text import *
from .Requests import Request
import random
import json

with open("useragents.txt", 'r') as user:
    agent = user.read().split('\n')

def version():
    with open('config.json', 'r') as json_file:
        j = json.load(json_file)

        v = j['version']

        print(f"[{BLUE}INFO{WHITE}] Your version is: " + v)

        return v

async def check_update():
    v = version()

    r = await Request("https://raw.githubusercontent.com/N0rz3/Phunter/master/config.json").get()

    file = json.load(r)
    v_ = file['version']

    if v != v_:
        print(f"[{RED}-{WHITE}] Your version isn't up to date")
        print(f"[{BLUE}INFO{WHITE}] You are advised to reinstall the tool\n=> https://github.com/N0rz3/Phunter")

    else:
        print(f"[{GREEN}>{WHITE}] Your version is up to date")


async def test_url():
    list_url = [
        "https://free-lookup.net",
        "https://www.tellows.fr",
        "https://spamcalls.net/en"
    ]

    print(f"\n[{BLUE}INFO{WHITE}] Test responses services...")

    for url in list_url:
        r = await Request(url, headers={'user-agent': random.choice(agent)}).get()

        if r.status_code == 200:
            name = str(url).replace("https://", "").replace("www.", "").replace("fr", "").replace("en", "").replace(".net", "").replace("ee-", "").replace(".", "").replace("/", "")

            print(f"  ├── [{GREEN}{r.status_code}{WHITE}] {name}")

        else:
            print(f"  ├── {RED}{r.status_code}{WHITE} {name}")