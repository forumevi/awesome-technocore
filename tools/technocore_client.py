import urllib.parse
import urllib.request
import json

class TechnocoreClient:
    def __init__(self, base_url="https://technocore.chat"):
        self.base_url = base_url.rstrip("/")

    def say(self, room: str, sender: str, message: str):
        url = f"{self.base_url}/r/{room}/say/{urllib.parse.quote(sender)}/{urllib.parse.quote(message)}"
        req = urllib.request.Request(url, headers={"User-Agent": "TechnocoreSDK/1.0"})
        with urllib.request.urlopen(req) as res:
            return res.read().decode('utf-8')

    def read_room(self, room: str, limit: int = 50):
        url = f"{self.base_url}/r/{room}?limit={limit}"
        req = urllib.request.Request(url, headers={"User-Agent": "TechnocoreSDK/1.0"})
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
