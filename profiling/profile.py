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

            for i in range(0, 4):
                print("%s (ratio= %2f) with %d credit(s)" % (self.moduleCollection.get_letter_with(i),
                                                             self.moduleCollection.get_ratio_with(i),
                                                             self.moduleCollection.get_credits_with(i)))
        if "module_collection" in options:
            self.moduleCollection.display()
