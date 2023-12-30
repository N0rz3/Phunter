import phonenumbers
import json
from phonenumbers import carrier
from .reputation import *
from .free_lookup import free
from .spam import spamcalls

from lib.text import *

async def lookup(phone_number):
    print()
    parsed = phonenumbers.parse(phone_number)

    operator = carrier.name_for_number(parsed, "fr")
    line = phonenumbers.number_type(parsed)

    if line == phonenumbers.PhoneNumberType.FIXED_LINE:
        ligne = f" [{GREEN}>{WHITE}] Line type: Fixed"

    elif line == phonenumbers.PhoneNumberType.MOBILE:
        ligne = f" [{GREEN}>{WHITE}] Line type: Mobile"

    else:
        ligne = " [-] Line not found"

    possible = phonenumbers.is_possible_number(parsed)
    valid = phonenumbers.is_valid_number(parsed)

    with open("lib/country.json", "r") as file:
        read = json.load(file)

    d = 0
    countrys = []

    for country, code in read.items():
        d += 1 

        if phone_number.startswith(code):
            countrys.append(country)

            if d == 153:
                break
            else:
                continue
        else:
            continue

    print(f"{WHITE}📞 Phone number: {BLUE}{phone_number}{WHITE}")

    if possible == True:
        pos = {"possible": "✔️"}
    else:
        pos = {"possible": "❌"}

    if valid == True:
        val = {"valid": "✔️"}
    else:
        val = {"valid": "❌"}

    print(f" [{GREEN}>{WHITE}] Possible: {pos['possible']}")
    print(f" [{GREEN}>{WHITE}] Valid: {val['valid']}")
    print()

    if operator != "":
        print(f" [{GREEN}>{WHITE}] Operator: {operator}")
    else:
        print(f" [-] Not Operator")
    try:
        print(f" [{GREEN}>{WHITE}] Possible location: " + str(countrys).replace("[", "").replace("]", "").replace("'", ""))
    except:
        print(f" [-] Not location")

    print(ligne)

    await reputation(phone_number)

    await free(str(phone_number).replace("+", ""))

    await spamcalls(p_n=phone_number)