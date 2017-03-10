import requests
from config import Configure

class ModuleNotes:
    """
    This class can take all notes of the specified module Code
    """

    host = "https://intra.epitech.eu/"
    user_api = "/user/"
    notes_api = "notes/?format=json"

    def __init__(self, config, moduleCode, login):
        if not isinstance(config, Configure):
            raise TypeError("Force Configure instance")
        if config.getAuth() == "None":
            raise ValueError("Please check auth key")
        self.req = requests.get(self.urlAuthEncode(login, config.getAuth()) + ModuleNotes.notes_api)
        # search only code module
        self.note = [x for x in self.req.json()["notes"] if "codemodule" in x and x["codemodule"] == moduleCode]

    def urlAuthEncode(self, login, auth):
        return ModuleNotes.host + auth + ModuleNotes.user_api + login + "/"

    def getNotes(self):
        return self.note