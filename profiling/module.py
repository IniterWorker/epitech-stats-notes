import requests


class Module:
    def __init__(self, verbose, module, notes):
        self.module = module
        self.notes = notes
        self.verbose = verbose
        self.position = 0

    def get_position(self) -> int:
        return self.position

    def get_code(self) -> str:
        return self.module["codemodule"]

    def get_notes(self) -> float:
        return self.notes

    def get_credits(self) -> int:
        return 0 if self.module["credits"] < 0 else self.module["credits"]

    def get_module_url(self, context):
        return 1
        # requests.get(context.get_api().url_formated_with_user("notes", context.))

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
        # print(self.module)
        print("Note:")
        for item in self.notes:
            print("Title: %s Note: %s" % (item['title'], str(item['final_note'])))
            # print(self.notes)


class ModuleCollection:
    """
    This class can take all notes of the specified module Code
    """
    CURRENT = 5
    ACQUIS = 6
    ECHEC = 7
    E = 4
    D = 3
    C = 2
    B = 1
    A = 0

    def __init__(self, context, email):
        self.verbose = context.is_verbose()
        self.req = requests.get(context.get_api().url_formated_with_user("notes", email))
        self.modules = []
        self.count = 0
        self.grade = [[], [], [], [], [], [], [], []]
        self.grade_credits = [0, 0, 0, 0, 0, 0, 0, 0]
        self.grade_ratio = []
        for x in self.req.json()["modules"]:
            module = Module(self.verbose, x.copy(), [y for y in self.req.json()["notes"] if
                                                     "codemodule" in y and y["codemodule"] == x[
                                                         "codemodule"]])
            self.count += 1
            if x["grade"] == "-":
                self.grade[self.CURRENT].append(module)
                self.grade_credits[self.CURRENT] += module.get_credits()
            elif x["grade"] == "Acquis":
                self.grade[self.ACQUIS].append(module)
                self.grade_credits[self.ACQUIS] += module.get_credits()
            elif x["grade"] == "E":
                self.grade[self.E].append(module)
                self.grade_credits[self.E] += module.get_credits()
            elif x["grade"] == "D":
                self.grade[self.D].append(module)
                self.grade_credits[self.D] += module.get_credits()
            elif x["grade"] == "C":
                self.grade[self.C].append(module)
                self.grade_credits[self.C] += module.get_credits()
            elif x["grade"] == "B":
                self.grade[self.B].append(module)
                self.grade_credits[self.B] += module.get_credits()
            elif x["grade"] == "A":
                self.grade[self.A].append(module)
                self.grade_credits[self.A] += module.get_credits()
            else:
                self.grade[self.ECHEC].append(module)
                self.grade_credits[self.ECHEC] += module.get_credits()
            self.modules.append(module)

        self.__calc_AE_number()
        self.__calc_ratio()

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

    """
    This method take only the letters grades
    :return the number of [A - E] grades
    """
    def __calc_AE_number(self):
        self._ae_number = sum(len(x) for x in self.get_grades()[0:4])

    """
    This method take only the letters grades
    """
    def __calc_ratio(self):
        for i in range(0, 4):
            self.grade_ratio.append(len(self.get_grades()[i]) / self._ae_number)

    def get_module_with(self, grade):
        return self.grade[grade]

    def get_ratio_with(self, grade):
        if grade > 4:
            return 0
        return self.grade_ratio[grade]

    def get_credits_with(self, grade):
        return self.grade_credits[grade]

    def get_letter_with(self, grade) -> str:
        if grade is self.CURRENT:
            return "-"
        elif grade is self.ECHEC:
            return "Echec"
        elif grade is self.ACQUIS:
            return "Acquis"
        elif grade is self.A:
            return "A"
        elif grade is self.B:
            return "B"
        elif grade is self.C:
            return "C"
        elif grade is self.D:
            return "D"
        elif grade is self.E:
            return "E"

