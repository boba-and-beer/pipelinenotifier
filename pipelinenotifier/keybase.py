"""KeyBase Notifier. A small difference between Keybase and the other notifiers is that Keybase has poorer User interface. 
This means you may want to include more details.
"""
from .base import *

class KeyBaseBot:
    """Class wrapper for a chatbot in Keybase to work.
    """
    def __init__(self, project_name: str, username: str, webhook_url: str):
        self.project_name = project_name
        self.webhook_url = webhook_url

    def send_message(self, message: str, include_time: bool=True):
        """Send Keybase message"""
        if include_time:
            current_Time = self.get_current_time()
            response = requests.post(self.webhook_url, data=f"{current_time}: {self.project_name} | " + message)
        else:
            response = requests.post(self.webhook_url, data=f"{self.project_name} | " + message)
        
        if response.status_code != 200:
            raise ValueError(
                'Request to keybase returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

class KeyBaseNotifier(KeyBaseBot, AbstractNotifier):
    """
    KeyBaseNotifier that automatically messages if started or began.
    """
    def __init__(self, project_name: str, username: str, webhook_url: str):
        super(KeyBaseNotifier, self).__init__(project_name, username, webhook_url)
