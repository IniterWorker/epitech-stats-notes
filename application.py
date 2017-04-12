#!/usr/bin/env python3

import argparse

from config import Configure
from config.api import IntranetAPI
from profiling import Context, Profile

verbose = True

if __name__ == "__main__":
    conf = Configure()
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-v', '--verbose', type=bool)
    parser.add_argument('-u', '--user', type=str)
    parser.add_argument('-a', '--auth', type=str)
    parser.add_argument("-d", "--display-options", nargs='+', action='append',
                        help='display_options element (default: all display)\n'
                             'options:'
                             'context'
                             ' email'
                             ' grade_stats'
                             ' module_collection')
    parser.add_argument('modules', metavar='ModuleCode', type=str, nargs='+',
                        help='an str for the accumulator')


    args = parser.parse_args()
    if args.auth is not None:
        print("Save new auto login: " + args.auth)
        conf.set_auto_login(args.auth)

    api = IntranetAPI(conf)
    context = Context(api, dict({verbose: args.verbose}))
    profile = Profile(context, args.user)
    profile.collect()
    profile.display(args.display_options[0] if args.display_options is not None else None)


