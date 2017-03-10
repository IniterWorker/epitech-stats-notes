import requests
from api import IntranetAPI

class ModuleNotes:
    """
    This class can take all notes of the specified module Code
    """

    def __init__(self, Api, moduleCode, login):
        if not isinstance(Api, IntranetAPI):
            raise TypeError("Force Intranet instance")
        self.req = requests.get(Api.urlFormatedWithUser("notes", login))
        # search only code module
        self.note = [x for x in self.req.json()["notes"] if "codemodule" in x and x["codemodule"] == moduleCode]

    def getNotes(self):
        return self.note