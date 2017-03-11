import requests
from api import IntranetAPI


class ModuleNotes:
    """
    This class can take all notes of the specified module Code
    """

    def __init__(self, Api, moduleCode, login):
        if login is None:
            raise ValueError("Login incompatible None element")
        if not isinstance(Api, IntranetAPI):
            raise TypeError("Force Intranet instance")
        self.req = requests.get(Api.urlFormatedWithUser("notes", login))
        # search only code module
        self.note = [x for x in self.req.json()["notes"] if "codemodule" in x and x["codemodule"] == moduleCode]

    """
    This method can be call to average the total notes
    """
    def average(self):
        return sum(item['final_note'] for item in self.note) / len(self.note)

    """
    This method can be call to filtering the current dictionary
    """
    def filtering(self, fct):
        self.note = [x for x in self.note if fct(x)]

    """
    This method can be call to get dictionary
    """
    def getNotes(self):
        return self.note