from abc import abstractmethod 
import requests
from datetime import datetime
import traceback

class AbstractBot:
    @abstractmethod
    def send_message(self):
        pass

class AbstractNotifier:
    """Slackbot that automatically captures messages if started or began.
    """
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

    def get_current_time(self) -> str:
        return str((datetime.now().time().hour + 10) % 24) + ':' + datetime.now().time().minute.__str__()
        