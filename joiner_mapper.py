#!/usr/bin/env python3
"""
Program:   Joiner
File:      joiner_mapper.py

Version:    V3.3
Date:       23.10.22
Function:   returns two csv files ready to be used for epitope analysis
            or data visualization with Seaborn

Copyright:  (c) Joan M. Amaya C., 2022
Author:     Joan Manuel Amaya Cuesta

--------------------------------------------------------------------------
Description:
============
Script used and referenced in the methods section my
Bioinformatics dissertation.
This program will clean and prepare the parsed files from data_parser.py
because when NetMHCpan 4.1 analyse the sequences adds characters to the
accession number of the sequence. Therefore theses extra characters
must be deleted. After this, the ViPR file (or any other excel file with
the metadata of the sequences retrieved), is refined in order to be
appropriately mapped.
The script returns two csv files. One with all the joined data ready for
epitope analysis, and other csv file with the count of the total number of
epitopes per sequence and year ready for data visualisation with Seaborn.

data = Joiner(r"path_of_ViPR_file.csv") call the instance with the metadata
data.four_alleles(): call to join and map only four alleles
data.five_alleles(): call to join and map only five alleles

In all cases two csv files will be given as output

--------------------------------------------------------------------------
Usage:
======
csv files created on data_parser and excel file from ViPR or any other database

--------------------------------------------------------------------------
Revision History:
=================
V1.0   june 2022
V3.3   23.10.22 Original   By: JMAC
"""
#*************************************************************************
# Import libraries

import pandas as pd
from glob import glob

#******************************************************************************

class Joiner:
    """
    Script to map metadata from ViPR or other suitable database where the
    sequences were retrieved, to join the metadata with the prediction data
    generated with NetMHCpan - 4.1.
    It is meant to use the output from Data Parser program (data_parser.py).
    The script will first clean the characters added by NetMHCpan - 4.1 when
    analysing the sequences and making it suitable to be mapped with the years,
    virus species and accession number (the metadata) of the ViPR file.
    Will return two csv files, one with all alleles concatenated with all
    the information and other csv file with the count of total number of epitopes
    per sequence and year.

    Object attributes:
    __init__(self, vipr_file): opens and create a DataFrame object from
    a ViPR file or any other excel file with metadata.


    Object methods:
    __init__(self, vipr_file): Create a DataFrame object using the metadata
    information of the sequences. In general the file to be used is an excel
    file downloaded from ViPR but can be used any other file from a suitable
    database.

    four_alleles(self): cleans and join parsed file and then map the metadata
    against the accession number of the sequence. Returns two csv files with
    the information of four alleles.

    five_alleles(self): same task as above but its usage is for five alleles.

    """

    def __init__(self, vipr_file):
        self.df = pd.read_excel(vipr_file)


    def four_alleles(self):
        #This part of the script will start to refine the output
        #produced on Data Parser program (data_parser.py)
        #because when NetMHCpan 4.1 analysed the sequences
        #adds characters to the accession number and
        #therefore this extra characters must be deleted
        #in order to map correctly the metadata from ViPR
        #or any other database which holds the sequences


        #1st allele
        #input statement to use in Allele column
        allele_1 = input("First allele: ")
        allele_file_1 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_1)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_1

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_1}.csv", index = False)


        #2nd allele
        #input statement to use in Country/Allele columns
        allele_2 = input("Second allele: ")
        allele_file_2 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_2)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_2

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_2}.csv", index = False)


        #3rd allele
        #input statement to use in Country/Allele columns
        allele_3 = input("Third allele: ")
        allele_file_3 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_3)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_3

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_3}.csv", index = False)


        #4th allele
        #input statement to use in Country/Allele columns
        allele_4 = input("Fourth allele: ")
        allele_file_4 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_4)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_4

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_4}.csv", index = False)


        #concatenation of all csv generated from previous function to give as
        #output a final csv file containing all
        #the information from a virus/serotype
        #the aim of this csv file is to have
        #the appropriate data to use for data
        #visualisation with seaborne

        #glob method to list csv files on the folder
        files = glob("*.csv")

        # DataFrame object storing all csv files
        df_overall = pd.concat(map(pd.read_csv, files), ignore_index=True)


        #this part does a dictionary that will be mapped
        #on each of the alleles
        #from the output of concatenated_files.csv

        final_name = input("Virus name: ")

        #selection of only useful data
        df_vipr = self.df
        df_vipr = df_vipr[["GenBank Protein Accession", "Collection Date"]]

        #standardisation of the genbank protein accession
        #that is equal to the ID column on the refined netMHCpan output

        df_acc_cleaned = df_vipr["GenBank Protein Accession"].str.extract(
            r"([A-Z0-9]+)")

        #ViPR does not have an uniform way to display the collection data
        #in order to standardise it, I will only capture the year
        df_vipr["Collection Date"] = df_vipr["Collection Date"].astype(
            "string")
        df_year_cleaned = df_vipr["Collection Date"].str.extract(
            r"([1-9]\d{3})")

        df_vipr_refined = df_vipr
        df_vipr_refined["GenBank Protein Accession"] = df_acc_cleaned
        df_vipr_refined["Collection Date"] = df_year_cleaned

        #dictionary to map against netMHCpan output
        vipr_dict = dict(df_vipr_refined.values)


        df_virus_final = df_overall
        df_virus_final["Year"] = df_virus_final["ID"].map(vipr_dict)

        df_virus_final.to_csv(f"{final_name}.csv", index=False)

        #this part creates new DataFrame objects with the data of
        #the collection year and then
        #absolute number of epitopes per allele

        #list of only accessions
        acc_list = df_overall["ID"].unique().tolist()

        #DataFrame object for each allele to be counted
        allele1 = df_overall[df_overall["Allele"] == allele_1]["ID"]
        allele2 = df_overall[df_overall["Allele"] == allele_2]["ID"]
        allele3 = df_overall[df_overall["Allele"] == allele_3]["ID"]
        allele4 = df_overall[df_overall["Allele"] == allele_4]["ID"]

        #dictionary to store total allele count per accession
        total_alleles1 = {}
        for i in range(len(acc_list)):
            total_alleles1[acc_list[i]] = allele1[allele1
                                                  == acc_list[i]].count()

        total_alleles2 = {}
        for i in range(len(acc_list)):
            total_alleles2[acc_list[i]] = allele2[allele2
                                                  == acc_list[i]].count()

        total_alleles3 = {}
        for i in range(len(acc_list)):
            total_alleles3[acc_list[i]] = allele3[allele3
                                                  == acc_list[i]].count()

        total_alleles4 = {}
        for i in range(len(acc_list)):
            total_alleles4[acc_list[i]] = allele4[allele4
                                                  == acc_list[i]].count()



        df_summary = self.df
        df_summary = df_summary[["Virus Type", "Collection Date",
                                 "GenBank Protein Accession"]]
        df_summary["GenBank Protein Accession"] = df_acc_cleaned
        df_summary["Collection Date"] = df_year_cleaned
        df_summary[allele_1] = df_summary["GenBank Protein Accession"].map(
            total_alleles1)
        df_summary[allele_2] = df_summary["GenBank Protein Accession"].map(
            total_alleles2)
        df_summary[allele_3] = df_summary["GenBank Protein Accession"].map(
            total_alleles3)
        df_summary[allele_4] = df_summary["GenBank Protein Accession"].map(
            total_alleles4)


        #data must be reshaped in order to get informational graphics
        df_total_alleles = pd.melt(df_summary,
                                   id_vars=["Virus Type",
                                            "GenBank Protein Accession",
                                                        "Collection Date"],
               var_name="Allele",
               value_name="Epitopes")

        #final csv file with the data for a particular serotype or virus
        #this file will be used for data visualisation
        df_total_alleles = df_total_alleles.reset_index(drop=True)
        df_total_alleles.to_csv(f"{final_name}_over_time.csv", index=False)



    def five_alleles(self):
        #This part of the script will start to refine the output
        #produced on Data Parser program (data_parser.py)
        #because when NetMHCpan 4.1 analysed the sequences
        #adds characters to de accession number and
        #therefore this extra characters must be deleted
        #in order to map correctly the metadata from ViPR
        #or any other database which holds the sequences


        #1st allele
        #input statement to use in Allele column
        allele_1 = input("First allele: ")
        allele_file_1 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_1)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_1

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_1}.csv", index = False)


        #2nd allele
        #input statement to use in Country/Allele columns
        allele_2 = input("Second allele: ")
        allele_file_2 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_2)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_2

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_2}.csv", index = False)


        #3rd allele
        #input statement to use in Country/Allele columns
        allele_3 = input("Third allele: ")
        allele_file_3 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_3)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_3

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_3}.csv", index = False)


        #4th allele
        #input statement to use in Country/Allele columns
        allele_4 = input("Fourth allele: ")
        allele_file_4 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_4)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_4

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_4}.csv", index = False)



        #5th allele
        #input statement to use in Allele columns
        allele_5 = input("Fifth allele: ")
        alele_file_5 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(alele_file_5)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Allele"] = allele_5

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{allele_5}.csv", index = False)


        #concatenation of all csv generated from previous function to give as
        #output a final csv file containing all
        #the information from a virus/serotype
        #the aim of this csv file is to have
        #the appropriate data to use for data
        #visualisation with seaborne

        #glob method to list csv files on the folder
        files = glob("*.csv")

        # DataFrame object storing all csv files
        df_overall = pd.concat(map(pd.read_csv, files), ignore_index=True)


        #this part does a dictionary that will be mapped
        #on each of the alleles
        #from the output of concatenated_files.csv

        final_name = input("Virus name: ")

        #selection of only useful data
        df_vipr = self.df
        df_vipr = df_vipr[["GenBank Protein Accession", "Collection Date"]]

        #standardisation of the genbank protein accession
        #that is equal to the ID column on the refined netMHCpan output

        df_acc_cleaned = df_vipr["GenBank Protein Accession"].str.extract(
            r"([A-Z0-9]+)")

        #ViPR does not have an uniform way to display the collection data
        #in order to standardise it, I will only capture the year
        df_vipr["Collection Date"] = df_vipr["Collection Date"].astype(
            "string")
        df_year_cleaned = df_vipr["Collection Date"].str.extract(
            r"([1-9]\d{3})")

        df_vipr_refined = df_vipr
        df_vipr_refined["GenBank Protein Accession"] = df_acc_cleaned
        df_vipr_refined["Collection Date"] = df_year_cleaned

        #dictionary to map against netMHCpan output
        vipr_dict = dict(df_vipr_refined.values)


        df_virus_final = df_overall
        df_virus_final["Year"] = df_virus_final["ID"].map(vipr_dict)

        df_virus_final.to_csv(f"{final_name}.csv", index=False)

        #this part creates new DataFrame objects with the data of
        #the collection year and then
        #absolute number of epitopes per allele

        #list of only accessions
        acc_list = df_overall["ID"].unique().tolist()

        #DataFrame object for each allele to be counted
        allele1 = df_overall[df_overall["Allele"] == allele_1]["ID"]
        allele2 = df_overall[df_overall["Allele"] == allele_2]["ID"]
        allele3 = df_overall[df_overall["Allele"] == allele_3]["ID"]
        allele4 = df_overall[df_overall["Allele"] == allele_4]["ID"]
        allele5 = df_overall[df_overall["Allele"] == allele_5]["ID"]

        #dictionary to store total allele count per accession
        total_alleles1 = {}
        for i in range(len(acc_list)):
            total_alleles1[acc_list[i]] = allele1[allele1
                                                  == acc_list[i]].count()

        total_alleles2 = {}
        for i in range(len(acc_list)):
            total_alleles2[acc_list[i]] = allele2[allele2
                                                  == acc_list[i]].count()

        total_alleles3 = {}
        for i in range(len(acc_list)):
            total_alleles3[acc_list[i]] = allele3[allele3
                                                  == acc_list[i]].count()

        total_alleles4 = {}
        for i in range(len(acc_list)):
            total_alleles4[acc_list[i]] = allele4[allele4
                                                  == acc_list[i]].count()

        total_alleles5 = {}
        for i in range(len(acc_list)):
            total_alleles5[acc_list[i]] = allele5[allele5
                                                  == acc_list[i]].count()


        df_summary = self.df
        df_summary = df_summary[["Virus Type", "Collection Date",
                                 "GenBank Protein Accession"]]
        df_summary["GenBank Protein Accession"] = df_acc_cleaned
        df_summary["Collection Date"] = df_year_cleaned
        df_summary[allele_1] = df_summary["GenBank Protein Accession"].map(
            total_alleles1)
        df_summary[allele_2] = df_summary["GenBank Protein Accession"].map(
            total_alleles2)
        df_summary[allele_3] = df_summary["GenBank Protein Accession"].map(
            total_alleles3)
        df_summary[allele_4] = df_summary["GenBank Protein Accession"].map(
            total_alleles4)
        df_summary[allele_5] = df_summary["GenBank Protein Accession"].map(
            total_alleles5)


        #data must be reshaped in order to get informational graphics
        df_total_alleles = pd.melt(df_summary,
                                   id_vars=["Virus Type",
                                            "GenBank Protein Accession",
                                                        "Collection Date"],
               var_name="Allele",
               value_name="Epitopes")

        #final csv file with the data for a particular serotype or virus
        #this file will be used for data visualisation
        df_total_alleles = df_total_alleles.reset_index(drop=True)
        df_total_alleles.to_csv(f"{final_name}_over_time.csv", index=False)
