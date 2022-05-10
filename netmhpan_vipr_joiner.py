#!/usr/bin/env python3
#version 0.9

import pandas as pd
from glob import glob

#########
#version comments:
#allele_country() #will be used as many times as countrys/alleles have been done on netmhcpan
#overall_virus() #r"path" must be checked, otherwise will give error
#vipr_parser() #ViPR display excel, r"path" be checked, otherwise will give error
                #input is taking correctly the path without r"

#############

#this function will clean the id column from netmhcpan refined output to stardardise the accession as
#vipr function to then country/allele columns that will be filled with an input chosen by the operator,
#this will be followed by the addition of an empty year column in order to return a DataFrame object
#with the selected country or allele

def allele_country(filename):

    #input statement to use in Country/Allele columns
    country = input("Country allele: ")

    #will only work with the output refined from netmchpan
    df_netmhcpan = pd.read_csv(filename)

    df_accession_cleaned = df_netmhcpan["ID"].str.extract(r"([A-Z0-9]+)")
    df_accession_cleaned.columns = ["ID"]


    df_netmhcpan_refined = df_netmhcpan
    df_netmhcpan_refined["ID"] = df_accession_cleaned["ID"]

    #new column to indicate the country or allele
    #this column will be filled with the input prompted by the user
    df_netmhcpan_refined["Country/Allele"] = country

    #year column to be filled with vipr dict
    df_netmhcpan_refined["Year"] = ""


    #DataFrame object to be used in next virp_parser function
    df_country_allele = df_netmhcpan_refined

    return df_country_allele.to_csv(f"{country}.csv", index = False)

#*************************************************************************

#function to concatenate all csv generated from previous function to give as
#output a final csv file containing all the information from a virus/serotype
#the aim of this csv file is to have the appropriate data to use for data visualisation with seaborne
def overall_virus(path):

    #input statement to name the csv file that has the concatenation of all csv files in the folder
    name = input("filename: ")

    #glob method to list csv files on the folder
    files = glob("*.csv")

    # DataFrame object storing all csv files
    df_overall = pd.concat(map(pd.read_csv, files), ignore_index=True)


    return df_overall.to_csv(f"{name}.csv", index=False)

#*************************************************************************

#the aim of this function is to do a dictionary that will be mapped on each of the country/alleles
#from the output of overall_virus function

def vipr_parser(filename):
    df_vipr = pd.read_excel(filename)

    csv_to_fill = input("File with NaN years: ")
    final_name = input("Virus name: ")

    #selection of only useful data
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


    df_virus_final = pd.read_csv(csv_to_fill)
    df_virus_final["Year"] = df_virus_final["ID"].map(vipr_dict)

    return df_virus_final.to_csv(f"{final_name} Changes Over Time.csv", index=False)
