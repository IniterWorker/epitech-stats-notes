from profiling.context import Context
from profiling.module import ModuleCollection


class Profile:

    def __init__(self, context, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string reference")
        if not isinstance(context, Context):
            raise TypeError("Context must be a Context reference")
        self.context = context
        self.email = email
        self.moduleCollection = None

    def collect(self):
        self.moduleCollection = ModuleCollection(self.context, self.email)

    def display(self, options: None):
        if options is None:
            options = []
            options.append("context")
            options.append("email")
            options.append("module_collection")
        if "context" in options:
            self.context.display()
        if "email" in options:
            print("Target: " + self.email)
        if self.moduleCollection is None:
            print("No data computed")
            return
        if "grade_stats" in options:
            grade_number = sum(len(x) for x in self.moduleCollection.get_grades()[0:4])
            print("A = " + (len(self.moduleCollection.get_grades()[0]) / grade_number).__str__()
                  + " credits (" + sum(x.get_credits() for x in self.moduleCollection.get_grades()[0]).__str__() + ")")
            print("B = " + (len(self.moduleCollection.get_grades()[1]) / grade_number).__str__()
                  + " credits (" + sum(x.get_credits() for x in self.moduleCollection.get_grades()[1]).__str__() + ")")
            print("C = " + (len(self.moduleCollection.get_grades()[2]) / grade_number).__str__()
                  + " credits (" + sum(x.get_credits() for x in self.moduleCollection.get_grades()[2]).__str__() + ")")
            print("D = " + (len(self.moduleCollection.get_grades()[3]) / grade_number).__str__()
                  + " credits (" + sum(x.get_credits() for x in self.moduleCollection.get_grades()[3]).__str__() + ")")
            print("E = " + (len(self.moduleCollection.get_grades()[4]) / grade_number).__str__()
                  + " credits (" + sum(x.get_credits() for x in self.moduleCollection.get_grades()[4]).__str__() + ")")
            print("- = " + (len(self.moduleCollection.get_grades()[5])).__str__())
            print("Aq = " + (len(self.moduleCollection.get_grades()[6])).__str__())
            print("Ec = " + (len(self.moduleCollection.get_grades()[7])).__str__())
        if "module_collection" in options:
            self.moduleCollection.display()
