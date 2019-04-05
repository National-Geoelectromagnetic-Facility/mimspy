#!/opt/local/bin/python3.6

# ************************************************************************
#  File Name: err_logger.py
#
#  Created By: Brady Fry (frybr)
#
#  Purpose:  This script tests the error logging function.  This allows the
#  logging of uncaught errors.
# ************************************************************************

# ***********************************************************************/
# imports
# ***********************************************************************/
import os
import sys
import logging
import traceback
from pathlib import Path

from _version import __version__
# ***********************************************************************/
# global variables
# ***********************************************************************/
errflepth = ''
# _version = '0.1.5'
__program__ = "NIMSpy"


def log_except_hook(*exc_info):
    global errflepth

    text = "".join(traceback.format_exception(*exc_info))
    logging.basicConfig(filename=errflepth, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.error("{} v{} Unhandled exception: \n{}".format(__program__, __version__, text))


def main():
    global errflepth
    sys.excepthook = log_except_hook
    home = str(Path.home())
    print(home)
    errflepth = os.path.join(
        home, 'Dropbox/Air2-Air3-DropBox/surveys/Earthscope/nimspy_logs/myapp.log')
    print(errflepth)

    None()
    print('Hello World')


# ***********************************************************************/
#                            __name__
# Needed to define main function in python program
# ***********************************************************************/
if __name__ == "__main__":
    main()
