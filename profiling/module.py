import requests


class Module:
    def __init__(self, verbose, module, notes):
        self.module = module
        self.notes = notes
        self.verbose = verbose

    def get_code(self):
        return self.module["codemodule"]

    def get_notes(self):
        return self.notes

    def get_credits(self) -> int:
        return self.module["credits"]

    def average_pitch(self):
        notes = [y["final_note"] for y in self.notes if
                 "final_note" and "title" and str(y["title"]).find("Pitch") != -1]
        if self.verbose:
            print(notes)
        notes_len = len(notes)
        notes_sum = sum(notes)
        return notes_sum / notes_len

    def average_project(self):
        notes = [y["final_note"] for y in self.notes if
                 "final_note" and "title" and str(y["title"]).find("Pitch") == -1]
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

    def display(self):
        print("ModuleCode: " + self.get_code())
        print("Grade:" + self.module["grade"])
        print(self.module)
        print("Note:")
        print(self.notes)


class ModuleCollection:
    """
    This class can take all notes of the specified module Code
    """

    def __init__(self, context, email):
        self.verbose = context.is_verbose()
        self.req = requests.get(context.get_api().url_formated_with_user("notes", email))
        self.modules = []
        self.count = 0
        self.grade = [[], [], [], [], [], [], [], []]
        for x in self.req.json()["modules"]:
            module = Module(self.verbose, x.copy(), [y for y in self.req.json()["notes"] if
                                                                "codemodule" in y and y["codemodule"] == x[
                                                                    "codemodule"]])
            self.count += 1
            if x["grade"] == "-":
                self.grade[5].append(module)
            elif x["grade"] == "Acquis":
                self.grade[6].append(module)
            elif x["grade"] == "E":
                self.grade[4].append(module)
            elif x["grade"] == "D":
                self.grade[3].append(module)
            elif x["grade"] == "C":
                self.grade[2].append(module)
            elif x["grade"] == "B":
                self.grade[1].append(module)
            elif x["grade"] == "A":
                self.grade[0].append(module)
            else:
                self.grade[7].append(module)
            self.modules.append(module)

    def get_count(self) -> int:
        return self.count

    def display(self):
        for x in self.modules:
            x.display()

    def get_modules(self):
        return self.modules

    def get_grades(self):
        return self.grade

    def get_module_code(self, code) -> Module:
        code = str(code)
        return [x for x in self.modules if x.get_code() == code][0]
