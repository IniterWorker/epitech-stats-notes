#!/usr/bin/env python3.4

import argparse
from config import Configure
from module import GrabeModules
from api import IntranetAPI

verbose = True

if __name__ == "__main__":
    conf = Configure()
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-v', '--verbose', type=bool)
    parser.add_argument('-u', '--user', type=str)
    parser.add_argument('-a', '--auth', type=str)
    parser.add_argument('modules', metavar='ModuleCode', type=str, nargs='+',
                        help='an str for the accumulator')

    args = parser.parse_args()
    if args.auth is not None:
        print("Save new auto login: " + args.auth)
        conf.set_auto_login(args.auth)
    api = IntranetAPI(conf)
    modules = GrabeModules(args.verbose, api, args.user)
    for moduleCode in args.modules:
        print("Name Module: " + moduleCode)
        print("Project Average: " + modules.getModuleCode(str(moduleCode)).average_project().__str__())
        print("Pitch Average: " + modules.getModuleCode(str(moduleCode)).average_pitch().__str__())
        print("General Average: " + modules.getModuleCode(str(moduleCode)).average().__str__())
        print("---------------")


