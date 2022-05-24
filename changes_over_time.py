#!/usr/bin/env python3
#version 1.0

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#******************************************************************************
#data = "path or filename"
#visualiser(data)
#******************************************************************************

class visualiser:
    """
    explanation.

    Object attributes:
    xxx (str): .
    yyy (str): .
    zzz (list): .

    Object methods:
    __init__(self, input): .
    """

    def __init__(self, virus_parsed):
        self.df = pd.read_csv(virus_parsed)

        virus_name = input("Virus name: ")

        x_size = 16
        y_size = 7
        plt.figure(figsize = (x_size, y_size))
        sns.barplot(x = "Collection Date", y = "Epitopes", hue = "Country/Allele",
                                data = self.df, ci = 95, errwidth= 3, palette = "tab10")
        plt.ylim(self.df["Epitopes"].min() - 5, self.df["Epitopes"].max() + 5)


        plt.title(f"{virus_name} Changes Over Year", fontsize = 20)
        plt.xlabel("Year of collection", fontsize = 15)
        plt.ylabel("Number of epitopes", fontsize = 15)

        plt.savefig(f"{virus_name}")

        plt.show()
