#!/usr/bin/env python3
"""
Program:   Visualiser
File:      changes_over_time.py

Version:    V1.0
Date:       01.10.22
Function:   returns two sets of bar plots, one with the overall graphics
            of all alleles, and other with each individual allele plotted

Copyright:  (c) Joan M. Amaya C., 2022
Author:     Joan Manuel Amaya Cuesta

--------------------------------------------------------------------------
Description:
============
Script used and referenced in 2.2.4 Epitope prediction and data analysis
 (Zika incursion in Brazil) of my Bioinformatics dissertation.
This program uses the csv file "changes_over_time.csv" created with
joiner_mapper in order to create two png file with barplots,
one with the overall trend in
all years and another one with each individual allele plotted.

data = visualiser("xxx_over_time.csv") call the csv file

--------------------------------------------------------------------------
Usage:
======
csv files created on joiner_mapper

--------------------------------------------------------------------------
Revision History:
=================
V1.0   june 2022
V3.3   23.10.22 Original   By: JMAC
"""
#*************************************************************************
# Import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#******************************************************************************

class visualiser:
    """
    Inspects the data from the joiner_mapper output and creates two png files
    with barplot useful for data visualisation.

    Object attributes:
    __init__(self, virus_parsed): opens _over_time.csv file and returns
                                  two png files.

    Object methods:
    __init__(self, virus_parsed): using the _over_time.csv file uses the data
    to create two png files with barplots, one with the overall
    trend of all alleles, and other with each allele plotted.

    """

    def __init__(self, virus_parsed):
        self.df = pd.read_csv(virus_parsed)

        virus_name = input("Virus name: ")

        x_size = 16
        y_size = 7
        plt.figure(figsize = (x_size, y_size))
        sns.barplot(x = "Collection Date", y = "Epitopes",
                    hue = "Allele", data = self.df,
                    ci = 95, errwidth= 3, palette = "tab10")

        plt.ylim(self.df["Epitopes"].min() - 5, self.df["Epitopes"].max() + 5)


        plt.title(f"{virus_name} Changes Over Time", fontsize = 20)
        plt.xlabel("Year of collection", fontsize = 15)
        plt.ylabel("Number of epitopes", fontsize = 15)

        plt.savefig(f"{virus_name}")

        plt.show()

        sns.catplot(x="Collection Date", y="Epitopes", col="Allele",
                    data = self.df, kind="bar", ci = 95, palette = "ocean")
        plt.ylim(self.df["Epitopes"].min() - 5, self.df["Epitopes"].max() + 5)

        plt.savefig(f"{virus_name} by allele")
