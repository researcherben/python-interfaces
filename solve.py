#!/usr/bin/env python3
import logging  # https://docs.python.org/3/library/logging.html
                # https://realpython.com/python-logging-source-code/
import argparse # https://docs.python.org/3.3/library/argparse.html
                # https://realpython.com/command-line-interfaces-python-argparse/
import os

#import sys
# I had been using sys for command-line arguments as per
#       https://realpython.com/python-command-line-arguments/
#       but argparse is the better approach
# I had intended to use sys for for writing to stderr as per
#       https://stackoverflow.com/a/15808105/1164295
#       but logging is the better approach


# docstrings should conform to
# https://google.github.io/styleguide/pyguide.html

"""
"""


# ************ Begin logging configuration ******************
# logging should be configured once (not per module)
# other modules can then reference the configuration


if not os.path.exists('logs'):
    os.makedirs('logs')

# https://gist.github.com/ibeex/3257877
from logging.handlers import RotatingFileHandler

# maxBytes=10000 = 10kB
# maxBytes=100000 = 100kB
# maxBytes=1000000 = 1MB
# maxBytes=10000000 = 10MB
log_size = 10000000
# maxBytes=100000000 = 100MB
# https://gist.github.com/ibeex/3257877
handler_debug = RotatingFileHandler(
    "logs/critical_and_error_and_warning_and_info_and_debug.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_debug.setLevel(logging.DEBUG)
handler_info = RotatingFileHandler(
    "logs/critical_and_error_and_warning_and_info.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_info.setLevel(logging.INFO)
handler_warning = RotatingFileHandler(
    "logs/critical_and_error_and_warning.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_warning.setLevel(logging.WARNING)

# https://docs.python.org/3/howto/logging.html
logging.basicConfig(
    # either (filename + filemode) XOR handlers
    # filename="test.log", # to save entries to file instead of displaying to stderr
    # filemode="w", # https://docs.python.org/dev/library/functions.html#filemodes
    handlers=[handler_debug, handler_info, handler_warning],
    # if the severity level is INFO,
    # the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages
    # and will ignore DEBUG messages
    level=logging.DEBUG,
    format="%(asctime)s|%(filename)-13s|%(levelname)-5s|%(lineno)-4d|%(funcName)-20s|%(message)s"  # ,
    # https://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format/7517430#7517430
    # datefmt="%m/%d/%Y %I:%M:%S %f %p", # https://strftime.org/
)

# https://docs.python.org/3/howto/logging.html
# if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages and will ignore DEBUG messages
# handler.setLevel(logging.INFO)
# handler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

# http://matplotlib.1069221.n5.nabble.com/How-to-turn-off-matplotlib-DEBUG-msgs-td48822.html
# https://github.com/matplotlib/matplotlib/issues/14523
logging.getLogger("matplotlib").setLevel(logging.WARNING)

# ************ end logging configuration ******************

logger = logging.getLogger(__name__)

# ********** begin primary functions *****************



# ********** end primary functions *****************


# ********** end helper functions *****************

if __name__ == "__main__":
    logger.info("[trace]")

    # ********** begin argparse configuration *****************

    theparser = argparse.ArgumentParser(description='do a thing', allow_abbrev=False)

    # required positional argument
    # it is possible to constrain the input to a range; see https://stackoverflow.com/a/25295717/1164295
    theparser.add_argument('N', metavar='nodes_in_graph', type=int, default=21,
                        help='an integer number. Required. Default is 21')

    theparser.add_argument('L', metavar='length', type=int, default=21,
                        help='an integer number. Required. Default is 21')

    theparser.add_argument('W', metavar='width', type=int, default=21,
                        help='an integer number. Required. Default is 21')

    theparser.add_argument('Q', metavar='q', type=str, default="the",
                        help='an integer number. Required. Default is 21')

    theparser.add_argument('d', metavar='d', type=int, default=21,
                        help='an integer number. Required. Default is 21')

    # even though this script is under version control in a git repo,
    # the --version is useful for when the code base is provided to
    # a user outside of git
    theparser.add_argument('--version', action='store_true',
                           help="version of this script")
    # https://semver.org/
    # MAJOR version when you make incompatible API changes,
    # MINOR version when you add functionality in a backwards compatible manner, and
    # PATCH version when you make backwards compatible bug fixes.
    theparser.add_argument('--history', action='store_true',
                           help="history of major versions of this script")

    # ********** end argparse configuration *****************

    args = theparser.parse_args()

    print(args)

    if args.version:
        print("version: 0.1")
        exit()
    if args.history:
        print("version history")
        print("0.1: examplar")
        exit()


    logger.info("user provided "+str(args.N))
    if args.N<0:
        raise Exception("invalid number of nodes")

    # given L and W and Q and D, determine 

