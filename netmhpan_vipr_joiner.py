#!/usr/bin/env python3
#version 1.9

import pandas as pd
from glob import glob

#########
#version comments:
#set a variable with the file containing the vipr file to be used
#vipr = r"path"
#then use the class as data = country_and_year(vipr)
#it will prompt the user to input at least 4 country names and their
#appropriate file path (no r"" needed) as well as the name of the virus
#analysed

#############

class country_and_year:
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

    def __init__(self, vipr_file):
        self.df = pd.read_excel(vipr_file)



        #1st allele
        #input statement to use in Country/Allele columns
        country_1 = input("Country of first allele: ")
        allele_file_1 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_1)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Country/Allele"] = country_1

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{country_1}.csv", index = False)


        #2nd allele
        #input statement to use in Country/Allele columns
        country_2 = input("Country of second allele: ")
        allele_file_2 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_2)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Country/Allele"] = country_2

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{country_2}.csv", index = False)



        #3rd allele
        #input statement to use in Country/Allele columns
        country_3 = input("Country of third allele: ")
        allele_file_3 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_3)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Country/Allele"] = country_3

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{country_3}.csv", index = False)



        #4th allele
        #input statement to use in Country/Allele columns
        country_4 = input("Country of fourth allele: ")
        allele_file_4 = input("Allele file: ")

        #will only work with the output refined from netmchpan
        df_netmhcpan = pd.read_csv(allele_file_4)

        df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
        df_accession_cleaned.columns = ["ID"]


        df_netmhcpan_refined = df_netmhcpan
        df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

        #new column to indicate the country or allele
        #this column will be filled with the input prompted by the user
        df_netmhcpan_refined["Country/Allele"] = country_4

        #year column to be filled with vipr dict
        df_netmhcpan_refined["Year"] = ""


        #DataFrame object to be used in next virp_parser function
        df_country_allele = df_netmhcpan_refined
        df_country_allele.to_csv(f"{country_4}.csv", index = False)



        #5th allele if necessary
          #input statement to use in Country/Allele columns
          #country_5 = input("Country of fifth allele: ")
          #alele_file_5 = input("Allele file: ")

          #will only work with the output refined from netmchpan
          #df_netmhcpan = pd.read_csv(alele_file_5)

          #df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
          #df_accession_cleaned.columns = ["ID"]


          #df_netmhcpan_refined = df_netmhcpan
          #df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

          #new column to indicate the country or allele
          #this column will be filled with the input prompted by the user
          #df_netmhcpan_refined["Country/Allele"] = country_5

          #year column to be filled with vipr dict
          #df_netmhcpan_refined["Year"] = ""


          #DataFrame object to be used in next virp_parser function
          #df_country_allele = df_netmhcpan_refined
          #df_country_allele.to_csv(f"{country_5}.csv", index = False)


        #concatenation of all csv generated from previous function to give as
        #output a final csv file containing all the information from a virus/serotype
        #the aim of this csv file is to have the appropriate data to use for data
        #visualisation with seaborne

        #glob method to list csv files on the folder
        files = glob("*.csv")

        # DataFrame object storing all csv files
        df_overall = pd.concat(map(pd.read_csv, files), ignore_index=True)



        #this part does a dictionary that will be mapped on each of the country/alleles
        #from the output of concatenated_files.csv

        final_name = input("Virus name: ")

        #selection of only useful data
        df_vipr = self.df
        df_vipr = df_vipr[["GenBank Protein Accession", "Collection Date"]]

        #standardisation of the genbank protein accession that is equal to the ID
        #column on the refined netMHCpan output
        df_acc_cleaned = df_vipr["GenBank Protein Accession"].str.extract(r"([A-Z0-9]+)")

        #ViPR does not have an uniform way to display the collection data
        #in order to standardise it, I will only capture the year
        df_vipr["Collection Date"] = df_vipr["Collection Date"].astype("string")
        df_year_cleaned = df_vipr["Collection Date"].str.extract(r"([1-9]\d{3})")

        df_vipr_refined = df_vipr
        df_vipr_refined["GenBank Protein Accession"] = df_acc_cleaned
        df_vipr_refined["Collection Date"] = df_year_cleaned

        #dictionary to map against netMHCpan output
        vipr_dict = dict(df_vipr_refined.values)


        df_virus_final = df_overall
        df_virus_final["Year"] = df_virus_final["ID"].map(vipr_dict)

        df_virus_final.to_csv(f"{final_name} Changes Over Time.csv", index=False)
