from os.path import expanduser
from os.path import exists
from os import makedirs
import json
import io


class Configure:
    """
    Configuration Manager
    ~/.stats-notes/.auth
    if not exists create a new file and directory in the Home directory
    """
    defaultNameDirectory = ".stats-notes"
    defaultPathDirectory = (expanduser("~") + "/" + defaultNameDirectory)
    defaultNameFile = ".auth"
    defaultPathFile = (defaultPathDirectory + "/" + defaultNameFile)

    def __init__(self):
        self._json_data = None
        if not exists(Configure.defaultPathDirectory):
            makedirs(Configure.defaultPathDirectory)
        if exists(Configure.defaultPathFile):
            with open(Configure.defaultPathFile) as f:
                self._json_data = json.load(f)
        else:
            self._json_data = {
                "auth": {
                    "token": None
                }
            }
            self.save()

    def getAuth(self):
        return self._json_data["auth"]["token"].__str__()

    def setAuth(self, value):
        self._json_data["auth"]["token"] = value

    def save(self):
        with open(Configure.defaultPathFile, 'w+') as f:
            json.dump(self._json_data, f)
