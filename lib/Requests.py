import httpx
from .text import *

class Request:
    def __init__(self, url: str, headers=None, params=None):
        self.url = url
        self.head = headers
        self.params = params

    async def get(self):
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                response = await client.get(url=self.url, headers=self.head, params=self.params)
                return response

        except httpx.HTTPError:
            return httpx.Response(status_code=500, content=f"[{BLUE}INFO{WHITE}] Internal Server Error")