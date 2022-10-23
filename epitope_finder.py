#!/usr/bin/env python3
"""
Program:   Epitope Finder
File:      epitope_finder.py

Version:    V1.1
Date:       11.08.22
Function:   returns DataFrame information from the parsed file from data_parser

Copyright:  (c) Joan M. Amaya C., 2022
Author:     Joan Manuel Amaya Cuesta

--------------------------------------------------------------------------
Description:
============
Script used and referenced in the section 2.1.4 Epitope prediction and data
analysis of my Bioinformatics dissertation. 
This script returns three types of information based on the query input
of the user. The user either can input the whole epitope from EIDB to find
the exact match or can input residues 3 to 7 in order to find mutations.
All return will be printed in the shell
data = Parser("parsed_file.csv") call the instance with the parsed output
data.epitope(): call to retrieve only matching epitopes
data.year(): call to retrieve epitope and its year
data.all_info(): call to retrieve all available data in the csv file

--------------------------------------------------------------------------
Usage:
======
csv files created on ViPR joiner

--------------------------------------------------------------------------
Revision History:
=================
V0.5   june 2022
V1.1   11.08.22 Original   By: JMAC
"""
#*************************************************************************
# Import libraries

import pandas as pd
import re

#*************************************************************************

class Epitope_finder:

    """
    This script that has been used the section 2.1.4 Epitope prediction and
    data analysis of my Bioinformatics dissertation.
    The script will retrieve the information depending on
    the query typed and is intended to be used only with the parsed
    csv file of the Data Parser program or the csv file from the ViPR Joiner.
    The query can be the exact epitope to find or any amino acid but it is
    recommended to target residues 3 to 7 in order to find suitable mutations
    The output will be printed in the shell

    Object attributes:
    parsed_file (file): parsed csv file.

    Object methods:
    __init__(self, parsed_file): opens csv file previously created and
    prompts the user to type the epitope or amino acids that wants to find
    in case that is a mutated epitope.

    epitope(self): return the unique set of matches

    year(self): return epitopes and years

    all_info(self): return all available data

    """

    def __init__(self, parsed_file):
        self.df = pd.read_csv(parsed_file)

        #query to find the epitope from IEDB or a mutation
        query = input("Please enter epitope to find: ")
        self.df_query = self.df[self.df["Peptide"].str.match(f".*{query}.*") == True]

    def epitope(self):

        print(self.df_query["Peptide"].unique())

    def year(self):

        print(self.df_query[["Peptide", "Year"]])

    def all_info(self):

        print(self.df_query)
