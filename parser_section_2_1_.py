#!/usr/bin/env python3
#version 2.0

import pandas as pd
import re

#******************************************************************************
#this script will use the raw data from NetMHCpan 4.1 and parse it by
#the eluted ligand (EL)
#it returns a csv file with the data parsed for only 1 allelee
#this script belongs to the 2.1.4 Epitope prediction and data analysis of
#the MSc dissertation
#******************************************************************************
df_netmhcpan = input("NetMHCpan file: ")

df = pd.read_table(df_netmhcpan, low_memory=False)

# common columns
df_common = df.iloc[:, 0:3]

#unique columns per
df_1st_allele = df.iloc[:, 3:9]

df_overall_1st = df_common.join(df_1st_allele)
dff = df_overall_1st

#here the script selects the row containing the columns name
dff.columns = dff.iloc[0]
dff = dff.drop(0)

#as only analyses one peptide lenght i.e 9aa those columns are not necessary
dff = dff.drop(columns = ["core", "icore"])

#data type object changed in order to help to manipulate the data later on
dff["EL_Rank"] = dff["EL_Rank"].astype(float)


#columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
dff = dff[["Peptide", "ID", "EL_Rank"]].query("EL_Rank <= 2")
dff = dff.sort_values(by=["EL_Rank"])

#saves the parsed data
dff = dff.reset_index(drop=True)
dff.to_csv("depletion_assessment.csv", index=False)
