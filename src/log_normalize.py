#!/usr/bin/env python3

from log_normalize_functions import *

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     log_normalize.py
    Project:       Module Development Primer, Part 2
    Description:   log_normalize is a script takes in an input GCT file, checks
                   for its validity in both existence and file type & log 
                   normalizes all its values by utilizing logic and methods in
                   log_normalize_functions. 
    References:    https://github.com/genepattern/genepattern-python  
"""


# Checking for valid file name and extension
# Uses getter method to obtain boolean on file validity
if (get_valid()):
    # If so, reading file into DataFrame in_df
    in_df = read(args.filename)

    # Performing log transform on in_df and setting output DataFrame to out_df
    out_df = transform(in_df)

    # Adjusting index values to remove integer indices column
    out_df.set_index('Name', inplace=True)

    # Converting pandas DataFrame out_df to .gct file
    # Tweaked from the genepattern-python library's write_gct function 
    with open("result.gct", 'w') as file:
        # Writing file and ensuring .gct file's first two formatted rows
        # Column  count subtracted by 1 to account for non-data Description row
        file.write('#1.2\n' + str(len(out_df.index)) + '\t' + 
                   str(len(out_df.columns) - 1) + '\n')
        # Outputting file using proper tab delimeter
        out_df.to_csv(file, sep='\t', mode='w+')

# Else, if only the file type, or extension, is incorrect
# Uses getter method to obtain boolean on filename validity
elif (get_filename_exist()):
    print("Error!")
    print("File type (extension) incorrect, please use a .gct file")

# Else, if only the file name is incorrect
# Uses getter method to obtain boolean on file extension validity
elif (get_valid_ext()):
    print("Error!")
    print("File name incorrect, please use a valid file in the directory")
    
# Else, if both the file extension and name are incorrect
else:
    print("Error!")
    print("File name and extension incorrect, please use a valid" +
         " .gct file in the directory")
