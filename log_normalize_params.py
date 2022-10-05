#!/usr/bin/env python3

import argparse as ap
from os.path import exists

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     log_normalize_params.py
    Project:       Module Development Primer, Part 2
    Description:   log_normalize_params is a script that contains parameter
                   implementation for filename and verbosity through argparse.
    References:    tiny.cc/gct
"""

# Adding argumenta to script for verbosity and input file name
parser = ap.ArgumentParser(description='GCT file log normalizer.')

# Verbose argument, either True or False
parser.add_argument("-v", "--verbose", help="increase output verbosity.",
                    action="store_true")

# Filename argument, 
parser.add_argument('filename')

# Parsing arguments for future calls within script to utilize
args = parser.parse_args()

# Verifying verbosity status
if (args.verbose):
    print("Verbosity turned on.")
    print()


# Setting input file's name to variable name
name = args.filename

# Validating existent file name
file_exist = exists(name)
# Validating correct file type (through ".gct" extension)
valid_ext = name.endswith(".gct")
# Boolean AND value of both checks
valid = file_exist and valid_ext
