if __name__ == "__main__":
   import sys; sys.dont_write_bytecode = True
   from lib import beautiful
   beautiful

   import asyncio
   from lib.cli import parser
   asyncio.run(parser())