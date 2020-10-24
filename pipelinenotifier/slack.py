"""Contextmanager for Slackbot notifications
"""
import requests
import json
from contextlib import AbstractContextManager
from .base import *

def send_message(MESSAGE:str, webhook_url: str, username: str):
    """Upload slack data"""
    slack_data = {'text': username + ": " + MESSAGE}
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

class SlackBot(AbstractBot):
    """Base SlackBot
    """
    def __init__(self, project_name: str, username: str, webhook_url: str):
        self.project_name = project_name
        self.username = username
        self.webhook_url = webhook_url
    
    def send_message(self, message):
        """Send slack message"""
        slack_data = {'text': self.username + " | " + self.project_name + ": " + message}
        response = requests.post(
            self.webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

class SlackNotifier(AbstractNotifier, SlackBot):
    """Slackbot that automatically captures messages if started or began.
    """
    def __init__(self, project_name, username, webhook_url):
        super(SlackNotifier, self).__init__(project_name, username, webhook_url)
    