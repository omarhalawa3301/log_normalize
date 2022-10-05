#!/usr/bin/env python3

import os
import sys
from subprocess import call

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     log_normalize_command_line.py
    Project:       Module Development Primer, Part 2
    Description:   log_normalize_command_line is a script that implements
                   command line calling for script integration into a module.
"""


WORKING_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
ROOT = os.path.join(WORKING_DIR, '..')
TASKLIB = os.path.join(ROOT, 'src/')
INPUT_FILE_DIRECTORIES = os.path.join(ROOT, 'data/')

command_line = "python3 "+TASKLIB+"log_normalize.py "\
                + INPUT_FILE_DIRECTORIES+"all_aml_train.gct"\
                + " -v"
print("About to call the module using the command line:", command_line)

call(command_line, shell=True)