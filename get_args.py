##
## Get commandline arguments
##

from sys import stderr as error
from sys import stdout as out
from sys import exit
from re import compile

def print_usage(output, bin_name):
    print("%s: Usage:\n" % bin_name, file=output)
    print("\t-h/--help\tPrint usage", file=output)
    print("\t-u\t\tUser name", file=output)
    print("\t-m\t\tModule name (form : 'B-NAME-CODE')", file=output)

def get(argv):

    user_name = ""
    module_name = ""

    i = 1
    module_regex = compile("^[A-Z]{1}-[A-Z]{2,}-[0-9]{2,}$")
    name_regex = compile("^[a-z\-0-9]*\.[a-z\-0-9]*$")
    while i < len(argv):
        try:
            if argv[i] == "-u":
                i += 1
                user_name = argv[i]
                if not name_regex.fullmatch(user_name):
                    print("Error: Invalid User name", file=error)
                    print_usage(error, argv[0])
                    exit(84)
            elif argv[i] == "-m":
                i += 1
                module_name = argv[i]
                if not module_regex.fullmatch(module_name):
                    print("Error: Invalid module name", file=error)
                    print_usage(error, argv[0])
                    exit(84)
            else:
                if argv[i] == "-h" or argv[i] == "--help":
                    output = out
                    exit_value = 0
                else:
                    output = error
                    exit_value = 84
                print_usage(output, argv[0])
                exit(exit_value)
        except IndexError:
            print_usage(error, argv[0])
            exit(84)
        i += 1
    if len(user_name) == 0 or len(module_name) == 0:
        print("Error: User name or Module name is missing", file=error)
        print_usage(error, argv[0])
    return user_name, module_name
