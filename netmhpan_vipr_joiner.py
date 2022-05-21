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

        df_virus_final.to_csv(f"{final_name}.csv", index=False)

        #this part creates new DataFrame objects with the data of the collection year and then
        #absolute number of epitopes per allele/country

        #list of only accessions
        acc_list = df_overall["ID"].unique().tolist()


        #DataFrame object for each country/allele to be counted
        country_allele1 = df_overall[df_overall["Country/Allele"] == country_1]["ID"]
        country_allele2 = df_overall[df_overall["Country/Allele"] == country_2]["ID"]
        country_allele3 = df_overall[df_overall["Country/Allele"] == country_3]["ID"]
        country_allele4 = df_overall[df_overall["Country/Allele"] == country_4]["ID"]
        #country_allele5 = df_overall[df_overall["Country/Allele"] == country_5]["ID"]

        #dictionary to store total allele count per accession
        total_alleles1 = {}
        for i in range(len(acc_list)):
            total_alleles1[acc_list[i]] = country_allele1[country_allele1 == acc_list[i]].count()

        total_alleles2 = {}
        for i in range(len(acc_list)):
            total_alleles2[acc_list[i]] = country_allele2[country_allele2 == acc_list[i]].count()

        total_alleles3 = {}
        for i in range(len(acc_list)):
            total_alleles3[acc_list[i]] = country_allele3[country_allele3 == acc_list[i]].count()

        total_alleles4 = {}
        for i in range(len(acc_list)):
            total_alleles4[acc_list[i]] = country_allele4[country_allele4 == acc_list[i]].count()

        #total_alleles5 = {}
        #for i in range(len(acc_list)):
            #total_alleles5[acc_list[i]] = country_allele5[country_allele5 == acc_list[i]].count()


        df_summary = self.df
        df_summary = df_summary[["Virus Type", "Collection Date", "GenBank Protein Accession"]]
        df_summary["GenBank Protein Accession"] = df_acc_cleaned
        df_summary["Collection Date"] = df_year_cleaned
        df_summary[country_1] = df_summary["GenBank Protein Accession"].map(total_alleles1)
        df_summary[country_2] = df_summary["GenBank Protein Accession"].map(total_alleles2)
        df_summary[country_3] = df_summary["GenBank Protein Accession"].map(total_alleles3)
        df_summary[country_4] = df_summary["GenBank Protein Accession"].map(total_alleles4)
        #df_summary[country_5, "Alleles"] = df_summary["GenBank Protein Accession"].map(total_alleles5)

        #data must be reshaped in order to get informational graphics
        df_total_alleles = pd.melt(df_summary, id_vars=["Virus Type", "GenBank Protein Accession", "Collection Date"],
               var_name="Country/Allele",
               value_name="Epitopes")

        #final csv file with the data for a particular serotype or virus
        #this file will be used for data visualisation
        df_total_alleles = df_total_alleles.reset_index(drop=True)
        df_total_alleles.to_csv(f"{final_name}_over_time.csv", index=False)
