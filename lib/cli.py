import argparse
from .lookup import lookup
from .account import Amazon
from .annuaire import Annuaire
from .text import *
from .verify import *
import time

async def parser():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        '-t', '--target',
        nargs='?',
        type=str,
        default=None,
        help='get info by phone number'
    )

    parse.add_argument(
        '-a', '--amazon',
        nargs='?',
        type=str,
        default=None,
        help='get confirmation whether Amazon linked by phone number'
    )

    parse.add_argument(
        '-p', '--person',
        nargs='?',
        type=str,
        default=None,
        help='get owner of phone number with inversed annual (Page Blanche)'
    )

    parse.add_argument(
        '-f', '--file',
        nargs='?',
        type=str,
        default=None,
        help='get info by a file containing phone numbers'
    )

    parse.add_argument(
        '-v', '--verify',
        action='store_true',
        help='check your version, update(s), services...'
    )

    parse.add_argument(
        '-o', '--output',
        nargs='?',
        type=str,
        default=None,
        help='give a file to save the output (only with args: --amazon/-a , --person/-p)'
    )

    args = parse.parse_args()

    if args.file:
        start = time.time()

        with open(args.file, 'r') as file:
            if args.file.endswith(".txt"):
                nums = file.read().split('\n')
                checked = 0
                for num in nums:
                    await lookup(num)
                    checked += 1
            else:
                print(f"[{RED}!{WHITE}] Please enter a .txt file")
                exit()

        end = round(time.time() - start, 2)

        print(f"""\n
{RED}{"═"*80}{WHITE}

                                    {RED}~{WHITE}Summary{RED}~{WHITE}

        Number of targets: {checked}
        Operation finished in (seconds): {end}s
""")
        exit()

    elif args.target:
        await lookup(args.target)
        exit()
    
    elif args.amazon:
        if args.output:
            Amazon.amazon(args.amazon, output=True, file=args.output)

        else:
            Amazon.amazon(args.amazon)

        exit()

    elif args.person:
        if args.output:
            Annuaire.annuaire(args.person, output=True, file=args.output)

        else:
            Annuaire.annuaire(args.person)

        exit()

    elif args.verify:
        await check_update()
        await test_url()

        exit()

    else:
        exit()