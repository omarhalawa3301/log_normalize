#!/usr/bin/env python3

from log_normalize_params import *
import pandas as pd
import numpy as np

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     log_normalize_functions.py
    Project:       Module Development Primer, Part 2
    Description:   log_normalize_functions is a script that contains the logic
                   functions for reading an input GCT file and processing it
                   by performing log normalization onto all its positive
                   values, making all other (non-positive) values 0.
    References:    tiny.cc/gct
"""


def read (gct_file):
    """ Function that reads input GenePattern GCT file into a Pandas DataFrame

    Arguments:
        gct_file (str): path/name (if in same dir) of GCT file to preprocess

    Returns:
        df: a Pandas DataFrame of same data as input GCT file
    """

    # Reading GCT file with a tab delimeter into the Pandas DataFrame df
    # Ignores first two lines, contain no biological information
    df = pd.read_csv(gct_file, delimiter='\t', header=2)

    # Checks for verbosity argument, if turned on, prints DataFrame dimensions
    # Column number subtracted by 2 to exclude non-biological information
    if (args.verbose):
        print("The data frame has " + str(df.shape[0]) + " rows and " 
               + str(df.shape[1] - 2) + " columns.\n") 
    
    return df


def transform (df):
    """ Function that takes in a Pandas DataFrame, performs a log transform
        on all its positive data points, and outputs a new GCT file

    Arguments:
        df (DataFrame): input Pandas DataFrame to process

    Returns:
        new_df: a new Pandas DataFrame that has been transformed
    """
    # Creating a copy of the input DataFrame df to manipulate values of
    new_df = df.copy()

    # Obtaining the column values as a list for iterating
    col_values = new_df.columns.values.tolist()
    # Removing first two columns ("Name" and "Description") in preperation for 
    # numerical data analysis, else text causes errors (in future updates)
    col_values.remove("Name")
    col_values.remove("Description")

    # Obtaining the number of rows for iterating
    rows = new_df.shape[0]

    # Creating counter for non-positive values in DataFrame
    nonpos_counter = 0

    # Iterating through each value of DataFrame through col_values and rows
    for col in col_values:
        for row in range(0, rows):

            # Checking for positive values
            if (new_df.at[row, col] > 0):
                # If so, setting the current value to its own natural log
                new_df.at[row, col] = np.log(new_df.at[row, col])

            # Else, must be non-positive
            else:
                # Setting to 0
                new_df.at[row, col] = 0

                # Checking for verbosity
                if (args.verbose):
                    # Iterating non-positive value counter
                    nonpos_counter += 1

    # Checking for verbosity
    if (args.verbose):
        # Printing non-positive values' count
        print("The data frame contained " + str(nonpos_counter) + " non-positive values.")

    # returning new, now transformed, DataFrame
    return new_df