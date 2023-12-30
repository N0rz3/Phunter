from .Requests import Request
from bs4 import BeautifulSoup
from .text import *
import random

with open("useragents.txt", 'r') as user:
    agent = user.read().split('\n')

async def free(phone_number):
    r = await Request("https://free-lookup.net/{}".format(phone_number), headers={'user-agent': random.choice(agent)}).get()

    html_body = BeautifulSoup(r.text, "html.parser")
    list_info = html_body.findChild("ul", class_="report-summary__list").findAll("div")

    info_dict = {
        k.text.strip(): info.text.strip() if info.text.strip() else "Not found"
        for _, (k, info) in enumerate(zip(list_info[::2], list_info[1::2]))
    }

    print(f"\n [{GREEN}>{WHITE}] Free-lookup")

    for key, value in info_dict.items():
        if value != "Not found":
            print(f"  ├── {key}: {value}")

        else:
            continue