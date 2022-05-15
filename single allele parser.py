#!/usr/bin/env python3
#version 1.1

import pandas as pd
import re


#*************************************************************************
#this function will use the raw data from NetMHCpan 4.1 and parse it by the eluted ligand (EL)
#it returns a csv file with the data parsed for only one allele

def allele_parser(filename):
    """Return a csv file with the parsed data from netMHCpan"""

    df = pd.read_table(filename) #r"" or just "" if it is in the same folder

    f = open(filename) #r""


    #netMHCpan gives an output with the allele as first row
    #name of the allele extracted to be use for the file name
    line = f.readlines(1)
    p = re.compile(r'(HLA-\w*):(\w*)')
    line = str(line)
    match = p.search(line)
    allele_name = match.group(1) + match.group(2)

    #dff to be used to create multiples csv files in future versions
    dff = df.reset_index()

    #here the script selects the row containing the columns name
    dff.columns = dff.iloc[0]
    dff = dff.drop(0)

    #data type object changed in order to help to manipulate the data later on
    dff["Pos"] = dff["Pos"].astype(int)
    dff["EL_Rank"] = dff["EL_Rank"].astype(float)
    dff["BA_Rank"] = dff["BA_Rank"].astype(float)


    #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
    dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
    dff = dff.sort_values(by=["EL_Rank"])

    #saves the parsed data sorted by EL Rank% only at this moment
    dff = dff.reset_index(drop=True)

    return dff.to_csv(f"{allele_name}.csv", index=False)

#*************************************************************************

#to extract number of sequences
dff["ID"].unique()

#to extract number of epitopes per sequence/year
dff["ID"].value_counts() #df_x.groupby('ID').size() another way

#count of epitopes on all sequences
dff["Peptide"].value_counts()

#to see occurrence of each epitope as overall
df_x = pd.read_csv("X Epitopes.csv")
df_x["Peptide"].value_counts()

#to obtain the strongest binder per sequence/year
df_country.groupby("ID")["EL_Rank"].min().sort_values()

#to display epitopes and el_rank% per seq/year and sorted by min
df_country.groupby("ID")[["Peptide", "EL_Rank"]].min().sort_values(by="EL_Rank")

#all sb epitopes but must be checked because it is giving as output all of them
df_country.groupby("Peptide")["EL_Rank"].min().sort_values()
