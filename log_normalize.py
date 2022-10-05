#!/usr/bin/env python3

from log_normalize_functions import *
from log_normalize_params import *

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     log_normalize.py
    Project:       Module Development Primer, Part 2
    Description:   log_normalize is a script takes in an input GCT file, checks
                   for its validity in both existence and file type using 
                   log_normalize_command_line, & log normalizes all its values
                   by utilizing logic and methods in log_normalize_functions.          
"""


# Checking for valid file name and extension
if (valid):
    # If so, reading file into DataFrame in_df
    in_df = read(args.filename)

    # Performing log transform on in_df and setting output DataFrame to out_df
    out_df = transform(in_df)

    # Creating an output file result.gct using the now-transformed data points
    out_df.to_csv("result.gct", sep='\t', index=False)

# Else, if only the file type, or extension, is incorrect
elif (file_exist):
    print("Error!")
    print("File type (extension) incorrect, please use a .gct file")

# Else, if only the file name is incorrect
elif (valid_ext):
    print("Error!")
    print("File name incorrect, please use a valid file in the directory")
    
# Else, if both the file extension and name are incorrect
else:
    print("Error!")
    print("File name and extension incorrect, please use a valid" +
         " .gct file in the directory")