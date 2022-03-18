#!/usr/bin/env python3
#version 0.1

import pandas as pd

df = pd.read_excel(r'C:\Users\Joan\Documents\Dissertation\PPLAV\NetMHCpan\CVS-11.xlsx')

--------------------------------------
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

------------------------------------------------------------------

#cleaner of the data that can be done without deleting the first row of the csv/xlsx file

df = pd.read_csv(r"xxxxxxx.csv")

dff = df
dff.columns = dff.iloc[0]
dff = dff.drop(0)

#EL_Rank had to be transformed into float dtype
dff["EL_Rank"] = dff["EL_Rank"].astype(float)
dff = dff[dff["EL_Rank"] < 2][["Peptide", "EL_Rank"]]
dff = dff.sort_values(by=["EL_Rank"])
dff = dff.reset_index(drop=True)

#only a file with all the epitopes
dff.to_csv("xxxx Epitopes.csv", index=False)

#from this main clean file the overall count, SB and WB will be count and parsed
xxx_epi = xxx["Peptide"].count()
xxx_sb = xxx[xxx["EL_Rank"] <= 0.5][["Peptide", "EL_Rank"]]
xxx_wb = xxx[xxx["EL_Rank"] > 0.5][["Peptide", "EL_Rank"]]

#.describe() not added atm
xxx_sb.min()
xxx_sb.max()
xxx_wb.min()
xxx_wb.max()
