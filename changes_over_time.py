#!/usr/bin/env python3
#version 0.9

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#******************************************************************************


#******************************************************************************

df = pd.read_csv("xxx.csv")

x_size = 16
y_size = 7
plt.figure(figsize = (x_size, y_size))
sns.barplot(x = "Collection Date", y = "Epitopes", hue = "Country/Allele", data = df, ci = 95, errwidth= 3, palette = "tab10")
plt.ylim(df["Epitopes"].min()-5, df["Epitopes"].max()+5)
plt.show()
