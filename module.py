import requests
from api import IntranetAPI

class Module:

    def __init__(self, verbose, module, notes):
        self.module = module
        self.notes = notes
        self.verbose = verbose

    def getCode(self):
        return self.module["codemodule"]

    def getNotes(self):
        return self.notes

    def average_pitch(self):
        notes = [y["final_note"] for y in self.notes if "final_note" and "title" and str(y["title"]).find("Pitch") != -1]
        if self.verbose:
            print(notes)
        notes_len = len(notes)
        notes_sum = sum(notes)
        return notes_sum / notes_len

    def average_project(self):
        notes = [y["final_note"] for y in self.notes if "final_note" and "title" and str(y["title"]).find("Pitch") == -1]
        if self.verbose:
            print(notes)
        notes_len = len(notes)
        notes_sum = sum(notes)
        return notes_sum / notes_len

    def average(self):
        notes = [y["final_note"] for y in self.notes if "final_note"]
        if self.verbose:
            print(notes)
        notes_len = len(notes)
        notes_sum = sum(notes)
        return notes_sum / notes_len


class GrabeModules:
    """
    This class can take all notes of the specified module Code
    """

    def __init__(self, verbose, Api, login):
        self.verbose = verbose
        if login is None:
            raise ValueError("Login incompatible None element")
        if not isinstance(Api, IntranetAPI):
            raise TypeError("Force Intranet instance")
        self.req = requests.get(Api.urlFormatedWithUser("notes", login))
        self.modules = []
        for x in self.req.json()["modules"]:
            self.modules.append(Module(verbose, x.copy(), [y for y in self.req.json()["notes"] if "codemodule" in y and y["codemodule"] == x["codemodule"]]))

    def getModules(self):
        return self.modules

    def getModuleCode(self, code):
        code = str(code)
        return [x for x in self.modules if x.getCode() == code][0]
