#!/usr/bin/env python3
#version 0.9

import pandas as pd

df = pd.read_excel(r'.xlsx')

#*************************************************************************
#initial way to clean the file but this is using the csv file after deleting the first column

#to exctract only the data/columns with important information
cvs = df[df["EL_Rank"] < 2][["Peptide", "EL_Rank"]]
cvs = cvs.sort_values(by=["EL_Rank"])
cvs_total = cvs.count()
print("Overall view", "\n", cvs, "\n")
print("Total Epitopes: ", cvs_total, "\n")


#to identify Strong Binders
cvs_sb = cvs[cvs["EL_Rank"] <= 0.5][["Peptide", "EL_Rank"]]
sb = cvs_sb.count()
print("Strong Binding Peptides", "\n", cvs_sb, "\n")
print("Total number: ", sb, "\n")


#to identify Weak Binders
cvs_wb = cvs[cvs["EL_Rank"] > 0.5][["Peptide", "EL_Rank"]]
wb = cvs_wb.count()
print("Weak Binding Peptides", "\n", cvs_wb, "\n")
print("Total number ", wb, "\n")


#to save the data in an appropriate csv file
#the final csv file is sorted like the txt file!!!
cvs.to_csv("CVS-11 Epitopes.csv", index=False)
cvs_sb.to_csv("CVS-11 SB.csv", index=False)
cvs_wb.to_csv("CVS-11 WB.csv", index=False)

#*************************************************************************

#cleaner of the data that can be done without deleting the first row of the csv/xlsx file

df = pd.read_csv(r"xxxxxxx.csv")

dff = df
dff.columns = dff.iloc[0]
dff = dff.drop(0)

#EL_Rank had to be transformed into float dtype
dff["EL_Rank"] = dff["EL_Rank"].astype(float)

#dff = dff[dff["EL_Rank"] < 2][["Peptide", "EL_Rank"]]

#to aid readability and also to add new columns to analyse
dff = dff[["Pos", "Peptide", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
dff = dff.sort_values(by=["EL_Rank"])
dff = dff.reset_index(drop=True)

#only a file with all the epitopes
dff.to_csv("xxxx Epitopes.csv", index=False)

#from this main clean file the overall count, SB and WB will be count and parsed
xxx_epi = xxx["Peptide"].count()
#xxx_sb = xxx[xxx["EL_Rank"] <= 0.5][["Peptide", "EL_Rank"]]
xxx_sb = dff.query("EL_Rank <= 0.5")
#xxx_wb = xxx[xxx["EL_Rank"] > 0.5][["Peptide", "EL_Rank"]]
xxx_wb = dff.query("EL_Rank > 0.5")

#.describe() not added atm
#dff.iloc[0] this will retrieve the min, min() is not giving a proper output
#must be investigated
#xxx_sb.min()
#xxx_sb.max()
#xxx_wb.min()
#xxx_wb.max()

#to use in plot bar
total_sb = xxx1_sb["Peptide"].count(), xxx2_sb["Peptide"].count()
total_wb = xxx1_wb["Peptide"].count(), xxx2_wb["Peptide"].count()


#*************************************************************************

#multiFASTA version

#this function will use the raw data from NetMHCpan and parse it by the eluted ligand (EL)
#it is meant to use only csv files as xls files are prompting an error when trying to use it
def allele_parser(filename):
    """Return a csv file with the parsed data from netMHCpan"""

    df = pd.read_csv(filename) #r""
    f = open(filename) #r""


    #netMHCpan gives an output with the allele as first row
    #name of the allele extracted to be use for the file name
    line = f.readlines(1)
    p = re.compile(r'(HLA-\w*):(\w*)')
    line = str(line)
    match = p.search(line)
    allele_name = match.group(1) + match.group(2)

    #dff to be used to create multiples csv files in future versions
    dff = df

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
