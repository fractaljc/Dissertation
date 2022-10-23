#!/usr/bin/env python3
"""
Program:   Variability
File:      epitopes_variability.py

Version:    V1.0
Date:       23.10.22
Function:   returns a bar plots in png format with all the information
            of the epitope variability of the Zika incursion in Brazil

Copyright:  (c) Joan M. Amaya C., 2022
Author:     Joan Manuel Amaya Cuesta

--------------------------------------------------------------------------
Description:
============
Script used and referenced in 2.2.4 Epitope prediction and data analysis
 (Zika incursion in Brazil) of my Bioinformatics dissertation.
This program uses the csv file created with joiner_mapper but instead of
changes_over_time.csv will use the csv file with all the joint data. Will returns
a png file with barplots showing the total number of unique epitopes, recurrents
and news

data = variability("zikav.csv") call the csv file

--------------------------------------------------------------------------
Usage:
======
csv files created on joiner_mapper

--------------------------------------------------------------------------
Revision History:
=================
V0.1   Ausgust 2022
V1.0   23.10.22 Original   By: JMAC
"""
#*************************************************************************
# Import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#******************************************************************************
class variability:
    """
    This script in unique for the Zika incursion.
    Will use the csv file generated with joiner_mapper
    with all the joint data of the alleles, also, will remove
    bad quality data and create a png file with barplots
    of all the epitope variability information

    Object attributes:
    __init__(self, df_zika_incursion): calls the specific data for this case.

    Object methods:
    __init__(self, df_zika_incursion): reads the csv .
    """


    def __init__(self, df_zika_incursion):
        self.df = pd.read_csv(df_zika_incursion)

        #in order to calculate the intermitent recurring epitopes
        #each year will be separated in different dataframe objects
        #and then filtered
        df_2015 = self.df[self.df["Year"] == 2015]
        df_2016 = self.df[self.df["Year"] == 2016]
        df_2017 = self.df[self.df["Year"] == 2017]
        df_2018 = self.df[self.df["Year"] == 2018]

        #2016 did have lots of bad quality artefacts
        #many sequences had more than 5 X
        #in order to avoid a wrong count these sequences will be removed
        df_2016["Peptide"] = df_2016["Peptide"].str.extract(r"([^X]{9})")

        #total per year

        df_total_2015 = df_2015["Peptide"].drop_duplicates().nunique()
        df_total_2016 = df_2016["Peptide"].drop_duplicates().nunique()
        df_total_2017 = df_2017["Peptide"].drop_duplicates().nunique()
        df_total_2018 = df_2018["Peptide"].drop_duplicates().nunique()

        #recurrents
        #as we are calculating only the recurrent epitopes
        #all duplications must be removed on each year
        df_unique_2015 = df_2015["Peptide"].drop_duplicates()
        df_unique_2016 = df_2016["Peptide"].drop_duplicates()
        df_unique_2017 = df_2017["Peptide"].drop_duplicates()
        df_unique_2018 = df_2018["Peptide"].drop_duplicates()

        df_recurrent_15_16 = df_unique_2015[df_unique_2015.isin(df_unique_2016)]
        df_recurrent_16_17 = df_recurrent_15_16[df_recurrent_15_16.isin(df_unique_2017)]
        df_recurrent_17_18 = df_recurrent_16_17[df_recurrent_16_17.isin(df_unique_2018)]

        df_recurrent_16 = df_recurrent_15_16.count()
        df_recurrent_17 = df_recurrent_16_17.count()
        df_recurrent_18 = df_recurrent_17_18.count()

        #observed in one year only
        df_only_15_16 = df_unique_2015[~df_unique_2015.isin(df_unique_2016)]
        df_only_16_17 = df_only_15_16[~df_only_15_16.isin(df_unique_2017)]
        df_only_17_18 = df_only_16_17[~df_only_16_17.isin(df_unique_2018)]

        df_only_16 = df_only_15_16.count()
        df_only_17 = df_only_16_17.count()
        df_only_18 = df_only_17_18.count()

        #dataframes for visualisation
        df_total = pd.DataFrame({"Total" : [df_total_2015, df_total_2016,
                                            df_total_2017, df_total_2018]})
        df_recurrents = pd.DataFrame({"Recurrents" : [0, df_recurrent_16, df_recurrent_17,
                                                      df_recurrent_18]})
        df_news = pd.DataFrame({"New" : [0, df_only_16, df_only_17, df_only_18]})
        df_years = pd.DataFrame({"Year" : [2015, 2016, 2017, 2018]})
        df_epitope_counts = pd.concat([df_years, df_total, df_recurrents, df_news], axis = 1)

        df_epitope_variability = pd.melt(df_epitope_counts, id_vars = ["Year"],
                                 var_name = "Analysis",
                                 value_name = "Epitopes")

        x_size = 16
        y_size = 7
        plt.figure(figsize = (x_size, y_size))

        ax = sns.barplot(x="Year", y="Epitopes", data=df_epitope_variability,
                 palette = "viridis", hue = 'Analysis')

        plt.title("Epitopes variability", fontsize = 20)
        plt.xlabel("Year", fontsize = 15)
        plt.ylabel("Number of epitopes", fontsize = 15)
        plt.legend(fontsize=15)

        plt.savefig("epitope_variability")
