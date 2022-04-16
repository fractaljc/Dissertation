#!/usr/bin/env python3
#version 0.1

import pandas as pd

df_virus_country1 = pd.read_csv(r"  .csv")
df_virus_country2 = pd.read_csv(r"  .csv")
df_virus_country3= pd.read_csv(r"  .csv")

df_year = pd.read_excel(r" .xls")

#new DataFrame which only stores the accession identifier (ID)
#for skeleton
country1 = df_virus_country1["ID"]
country2 = df_virus_country2["ID"]
country3 = df_virus_country3["ID"]
country4 = df_virus_country4["ID"]


#new data frame object with the data of the collection year and them
#absolute number of epitopes per alleles/df_country

df_year = df_year[["Virus Type", "Collection Date", "GenBank Protein Accession"]].sort_values("Collection Date")
df_year["country1-Epitopes"] = [country1[country1 == "gb_AHI43686_ncb"].count(),
                    country1[country1 == "gb_ACW82988_ncb"].count(),
                    country1[country1 == "gb_ACW82987_ncb"].count(),
                    country1[country1 == "gb_AHI43685_ncb"].count(),
                    country1[country1 == "gb_ACW82989_ncb"].count(),
                    country1[country1 == "gb_ADA60760_ncb"].count(),
                    country1[country1 == "gb_AHI43687_ncb"].count(),
                    country1[country1 == "gb_ACW82990_ncb"].count(),
                    country1[country1 == "gb_ACW82992_ncb"].count(),
                    country1[country1 == "gb_ADA60761_ncb"].count(),
                    country1[country1 == "gb_ACW82991_ncb"].count(),
                    country1[country1 == "gb_ACW82993_ncb"].count(),
                    country1[country1 == "gb_ACW82994_ncb"].count(),
                    country1[country1 == "gb_ACW82996_ncb"].count(),
                    country1[country1 == "gb_ACW82997_ncb"].count(),
                    country1[country1 == "gb_ACW82995_ncb"].count(),
                    country1[country1 == "gb_ACW82998_ncb"].count()]

df_year["country2-Epitopes"] = [country2[country2 == "gb_AHI43686_ncb"].count(),
                    country2[country2 == "gb_ACW82988_ncb"].count(),
                    country2[country2 == "gb_ACW82987_ncb"].count(),
                    country2[country2 == "gb_AHI43685_ncb"].count(),
                    country2[country2 == "gb_ACW82989_ncb"].count(),
                    country2[country2 == "gb_ADA60760_ncb"].count(),
                    country2[country2 == "gb_AHI43687_ncb"].count(),
                    country2[country2 == "gb_ACW82990_ncb"].count(),
                    country2[country2 == "gb_ACW82992_ncb"].count(),
                    country2[country2 == "gb_ADA60761_ncb"].count(),
                    country2[country2 == "gb_ACW82991_ncb"].count(),
                    country2[country2 == "gb_ACW82993_ncb"].count(),
                    country2[country2 == "gb_ACW82994_ncb"].count(),
                    country2[country2 == "gb_ACW82996_ncb"].count(),
                    country2[country2 == "gb_ACW82997_ncb"].count(),
                    country2[country2 == "gb_ACW82995_ncb"].count(),
                    country2[country2 == "gb_ACW82998_ncb"].count()]

df_year["country3-Epitopes"] = [country3[country3 == "gb_AHI43686_ncb"].count(),
                    country3[country3 == "gb_ACW82988_ncb"].count(),
                    country3[country3 == "gb_ACW82987_ncb"].count(),
                    country3[country3 == "gb_AHI43685_ncb"].count(),
                    country3[country3 == "gb_ACW82989_ncb"].count(),
                    country3[country3 == "gb_ADA60760_ncb"].count(),
                    country3[country3 == "gb_AHI43687_ncb"].count(),
                    country3[country3 == "gb_ACW82990_ncb"].count(),
                    country3[country3 == "gb_ACW82992_ncb"].count(),
                    country3[country3 == "gb_ADA60761_ncb"].count(),
                    country3[country3 == "gb_ACW82991_ncb"].count(),
                    country3[country3 == "gb_ACW82993_ncb"].count(),
                    country3[country3 == "gb_ACW82994_ncb"].count(),
                    country3[country3 == "gb_ACW82996_ncb"].count(),
                    country3[country3 == "gb_ACW82997_ncb"].count(),
                    country3[country3 == "gb_ACW82995_ncb"].count(),
                    country3[country3 == "gb_ACW82998_ncb"].count()]

df_year["country4-Epitopes"] = [country4[country4 == "gb_AHI43686_ncb"].count(),
                    country4[country4 == "gb_ACW82988_ncb"].count(),
                    country4[country4 == "gb_ACW82987_ncb"].count(),
                    country4[country4 == "gb_AHI43685_ncb"].count(),
                    country4[country4 == "gb_ACW82989_ncb"].count(),
                    country4[country4 == "gb_ADA60760_ncb"].count(),
                    country4[country4 == "gb_AHI43687_ncb"].count(),
                    country4[country4 == "gb_ACW82990_ncb"].count(),
                    country4[country4 == "gb_ACW82992_ncb"].count(),
                    country4[country4 == "gb_ADA60761_ncb"].count(),
                    country4[country4 == "gb_ACW82991_ncb"].count(),
                    country4[country4 == "gb_ACW82993_ncb"].count(),
                    country4[country4 == "gb_ACW82994_ncb"].count(),
                    country4[country4 == "gb_ACW82996_ncb"].count(),
                    country4[country4 == "gb_ACW82997_ncb"].count(),
                    country4[country4 == "gb_ACW82995_ncb"].count(),
                    country4[country4 == "gb_ACW82998_ncb"].count()]

#data must be reshaped in order to get informational graphics
df_overall1 = pd.melt(df_year, id_vars=["Virus Type", "GenBank Protein Accession", "Collection Date"],
               value_vars=["Colombia", "England", "Finland", "A0201"],
               var_name="Country/Allele",
               value_name="Epitopes")


df_overall1 = df_overall.reset_index(drop=True)

#for each one of the different viruses will be created a DataFrame object
#and then they will be appended on a final DataFrame containing all
#meaningful data of all viruses or serotypes

df_overall = pd.concat([df_overall1, df_overall2])

df_overall.to_csv("Virusx Changes Over Time.csv", index=False)
