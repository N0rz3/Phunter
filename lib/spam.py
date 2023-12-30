from .Requests import *
import random
from .text import *

with open("useragents.txt", "r") as user:
    user_agent = user.read().split('\n')

async def spamcalls(p_n):
    print(f"\n [{GREEN}>{WHITE}] Spamcalls")

    url = f"https://spamcalls.net/en/number/{p_n}"

    r = await Request(url, headers={'user-agent': random.choice(user_agent)}).get()

    if r.status_code == 200:
        print(f"  └── {RED}!{WHITE} Spammer")

    else:
        print(f"  └── {GREEN}>{WHITE} Not spammer")