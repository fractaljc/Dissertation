#!/usr/bin/env python3
#version 0.1

from pandas import DataFrame, read_csv
import pandas as pd

df = pd.read_excel(r'C:\Users\Joan\Documents\Dissertation\PPLAV\NetMHCpan\CVS-11.xlsx')

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
