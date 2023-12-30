from .Requests import Request
from bs4 import BeautifulSoup
from lib.text import *
import random

with open("useragents.txt", "r") as user:
    user_agent = user.read().split('\n')

async def reputation(phone_number):
    r = await Request(url="https://www.tellows.fr/num/%2B{}".format(phone_number), headers={"user-agent": random.choice(user_agent)}).get()

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        reputation = soup.find("div", {"class": "col-lg-9"}).findAll("h1")

        try:
            info = f"\n [{GREEN}>{WHITE}] Reputation: {reputation[0].text.strip()}"

        except Exception:
            info = f"\n [-] No reputation found "

        print(info)

    else:
        pass