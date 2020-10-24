import requests
import json
from .base import *

def send_message(string, penny=False,embeds=[]):
    obj = {'username': "NEWS", "content": string,"embeds":embeds}
    result = requests.post(penny_discord_url, data=json.dumps(obj), headers={"Content-Type": "application/json"})
    print(result.status_code)

class DiscordBot:
    """Class wrapper for a chatbot in Keybase to work.
    """
    def __init__(self, project_name: str, webhook_url: str, username: str):
        self.project_name = project_name
        self.webhook_url = webhook_url
        self.username = username

    def send_message(self, string: str, penny: bool=False, embeds: list=[]):
        """
            Send messages to Discord Bot.
        """
        obj = {'username': self.username, "content": string,"embeds":embeds}
        response = requests.post(self.webhook_url, data=json.dumps(obj), headers={"Content-Type": "application/json"})

class DiscordNotifier(AbstractNotifier, DiscordBot):
    """
    DIscordBot that automatically messages if started or began.
    """
    def __init__(self, project_name: str, webhook_url: str, username: str):
        super(DiscordNotifier, self).__init__(project_name, webhook_url, username)
