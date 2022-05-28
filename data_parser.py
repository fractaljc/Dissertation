#!/usr/bin/env python3
#version 1.9

import pandas as pd
import re


#******************************************************************************
#this class  will use the raw data from NetMHCpan 4.1 and parse it by
#the eluted ligand (EL)
#it returns a csv file with the data parsed for at least 4 alleles
#data = Parser("xxx.xls") call the instance with the output fron netMHCpan
#data.alleles("xxx.xls")  call to parse the file and save each allele as csv
#******************************************************************************

class Parser:
    """
    explanation.

    Object attributes:
    xxx (str): .
    yyy (str): .
    zzz (list): .

    Object methods:
    __init__(self, output): Create a DataFrame object and
    opens file to perform regex.
    """

    def __init__(self, netmhcpan_output):
        self.df = pd.read_table(netmhcpan_output, low_memory=False)


    def alleles(self, netmhcpan_output):

        self.f = open(netmhcpan_output)
        line = self.f.readlines(1)
        p = re.compile(r'(HLA-\w*):(\w*)')
        line = str(line)
        it = p.finditer(line)
        alleles_list = []

        for match in it:
            alleles_list.append(match.group(1) + match.group(2))


        # common columns
        df_common = self.df.iloc[:, 0:3]
        
        #unique columns per allele
        #1st allele
        df_1st_allele = self.df.iloc[:, 3:9]

        #2nd allele
        df_2nd_allele = self.df.iloc[:, 9:15]

        #3rd allele
        df_3rd_allele = self.df.iloc[:, 15:21]

        #4th allele
        df_4th_allele = self.df.iloc[:, 21:27]

        #5th allele
        df_5th_allele = self.df.iloc[:, 27:33]

        #new DataFrame object with all necessary from an allele
        df_overall_1st = df_common.join(df_1st_allele)
        df_overall_2nd = df_common.join(df_2nd_allele)
        df_overall_3rd = df_common.join(df_3rd_allele)
        df_overall_4th = df_common.join(df_4th_allele)
        df_overall_5th = df_common.join(df_5th_allele)


        #final csv file with 1st allele parsed
        dff = df_overall_1st

        #here the script selects the row containing the columns name
        dff.columns = dff.iloc[0]
        dff = dff.drop(0)

        #as only analyses one peptide lenght i.e 9aa those columns are not necessary
        dff = dff.drop(columns = ["core", "icore"])

        #data type object changed in order to help to manipulate the data later on
        dff["Pos"] = dff["Pos"].astype(int)
        dff["EL_Rank"] = dff["EL_Rank"].astype(float)
        dff["BA_Rank"] = dff["BA_Rank"].astype(float)

        #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
        dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
        dff = dff.sort_values(by=["EL_Rank"])

        #saves the parsed data sorted by EL Rank% only at this moment
        dff = dff.reset_index(drop=True)
        dff.to_csv(f"{alleles_list[0]}.csv", index=False)


        #final csv file with 2nd allele parsed
        dff = df_overall_2nd

        #here the script selects the row containing the columns name
        dff.columns = dff.iloc[0]
        dff = dff.drop(0)

        #as only analyses one peptide lenght i.e 9aa those columns are not necessary
        dff = dff.drop(columns = ["core", "icore"])

        #data type object changed in order to help to manipulate the data later on
        dff["Pos"] = dff["Pos"].astype(int)
        dff["EL_Rank"] = dff["EL_Rank"].astype(float)
        dff["BA_Rank"] = dff["BA_Rank"].astype(float)

        #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
        dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
        dff = dff.sort_values(by=["EL_Rank"])

        #saves the parsed data sorted by EL Rank% only at this moment
        dff = dff.reset_index(drop=True)
        dff.to_csv(f"{alleles_list[1]}.csv", index=False)


        #final csv file with 3rd allele parsed
        dff = df_overall_3rd

        #here the script selects the row containing the columns name
        dff.columns = dff.iloc[0]
        dff = dff.drop(0)

        #as only analyses one peptide lenght i.e 9aa those columns are not necessary
        dff = dff.drop(columns = ["core", "icore"])

        #data type object changed in order to help to manipulate the data later on
        dff["Pos"] = dff["Pos"].astype(int)
        dff["EL_Rank"] = dff["EL_Rank"].astype(float)
        dff["BA_Rank"] = dff["BA_Rank"].astype(float)

        #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
        dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
        dff = dff.sort_values(by=["EL_Rank"])

        #saves the parsed data sorted by EL Rank% only at this moment
        dff = dff.reset_index(drop=True)
        dff.to_csv(f"{alleles_list[2]}.csv", index=False)


        #final csv file with 4th allele parsed
        dff = df_overall_4th
        #here the script selects the row containing the columns name
        dff.columns = dff.iloc[0]
        dff = dff.drop(0)

        #as only analyses one peptide lenght i.e 9aa those columns are not necessary
        dff = dff.drop(columns = ["core", "icore"])

        #data type object changed in order to help to manipulate the data later on
        dff["Pos"] = dff["Pos"].astype(int)
        dff["EL_Rank"] = dff["EL_Rank"].astype(float)
        dff["BA_Rank"] = dff["BA_Rank"].astype(float)

        #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
        dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
        dff = dff.sort_values(by=["EL_Rank"])

        #saves the parsed data sorted by EL Rank% only at this moment
        dff = dff.reset_index(drop=True)
        dff.to_csv(f"{alleles_list[3]}.csv", index=False)


        #only to use if there is more than 5 alleles
        #final csv file with 5th allele parsed
        #dff = df_overall_5th
        #here the script selects the row containing the columns name
        #dff.columns = dff.iloc[0]
        #dff = dff.drop(0)

        #as only analyses one peptide lenght i.e 9aa those columns are not necessary
        #dff = dff.drop(columns = ["core", "icore"])

        #data type object changed in order to help to manipulate the data later on
        #dff["Pos"] = dff["Pos"].astype(int)
        #dff["EL_Rank"] = dff["EL_Rank"].astype(float)
        #dff["BA_Rank"] = dff["BA_Rank"].astype(float)

        #columns of relevance selected and threshold recommended by NetMHCpan-4.1 developers
        #dff = dff[["Pos", "Peptide", "ID", "EL_Rank", "BA_Rank"]].query("EL_Rank <= 2")
        #dff = dff.sort_values(by=["EL_Rank"])

        #saves the parsed data sorted by EL Rank% only at this moment
        #dff = dff.reset_index(drop=True)
        #dff.to_csv(f"{alleles_list[4]}.csv", index=False)

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
