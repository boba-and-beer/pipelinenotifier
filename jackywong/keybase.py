"""
Notify bot for Keybase
"""
import requests
import json
from contextlib import AbstractContextManager
from datetime import datetime

class KeyBaseBotSimple:
    """Class wrapper for a chatbot in Keybase to work.
    """
    def __init__(self, project_name: str, webhook_url: str):
        self.project_name = project_name
        self.webhook_url = webhook_url

    def send_message(self, message: str, include_time: bool=True):
        """Send Keybase message"""
        current_time = str((datetime.now().time().hour + 10) % 24) + ':' + datetime.now().time().minute.__str__()
        if include_time:
            response = requests.post(self.webhook_url, data=f"{current_time}: {self.project_name} | " + message)
        else:
            response = requests.post(self.webhook_url, data=f"{self.project_name} | " + message)
        
        if response.status_code != 200:
            raise ValueError(
                'Request to keybase returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

class KeyBaseBot(AbstractContextManager, KeyBaseBotSimple):
    """
    KeyBaseBot that automatically messages if started or began.
    """
    def __init__(self, project_name: str, webhook_url: str):
        super(KeyBaseBot, self).__init__(project_name, webhook_url)

    def __enter__(self):
        self.send_message("Began.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.send_message("Finished successfully.")
        else:
            if hasattr(traceback, 'print_last'):
                self.send_message(str(exc_type) + str(exc_value) + str(traceback.print_last()))
            else:
                self.send_message(str(exc_type) + str(exc_value))
