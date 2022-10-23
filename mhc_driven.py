#!/usr/bin/env python3
"""
Program:   MHC-driven
File:      mhc_driven.py

Version:    V1.0
Date:       23.10.22
Function:   returns p-values results for both sets of viruses assessed

Copyright:  (c) Joan M. Amaya C., 2022
Author:     Joan Manuel Amaya Cuesta

--------------------------------------------------------------------------
Description:
============
Script used and referenced in 2.3.4 Epitope prediction and data analysis
 (Comparison of MHC-driven viruses and non-MHC-driven viruses) of my
 Bioinformatics dissertation.
This program uses the csv file created with joiner_mapper but instead of
changes_over_time.csv will use individual csv file for each viral species.
Therefore no class have been done for this script
Will return the p values of the comparisons made for each data set.
The first data set is the Rabdhoviridae and the second is the Ancient/Novels
data set.


--------------------------------------------------------------------------
Usage:
======
csv files created on joiner_mapper

--------------------------------------------------------------------------
Revision History:
=================
V0.1   August 2022
V1.0   23.10.22 Original   By: JMAC
"""
#*************************************************************************
# Import libraries

import pandas as pd
import scipy.stats as stats
from scipy.stats import normaltest
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

#******************************************************************************
#Rabdhoviridae data set

#human
df_rabies_human = pd.read_csv("rabies_human_alleles.csv")
df_eblv2_human = pd.read_csv("eblv2_human_alleles.csv")

#other mammals
df_eblv2_bat = pd.read_csv("eblv2_bat_alleles.csv")
df_rabies_non_human = pd.read_csv("rabies_non_human_alleles.csv")
df_dolphin = pd.read_csv("Dolphin_alleles.csv")
df_indiana = pd.read_csv("indiana_vesiculovirus_alleles.csv")

#non-mammalian
#birds
df_ycb = pd.read_csv("Yellow-Crowned Bishop_alleles.csv")
df_grrenbul = pd.read_csv("Little Greenbul_alleles.csv")
df_bird = pd.read_csv("Bird_alleles.csv")

#fish
df_fish = pd.read_csv("Fish_alleles.csv")
df_perch = pd.read_csv("Perch_alleles.csv")
df_carp = pd.read_csv("Carp_alleles.csv")

#arthropods
df_cockroach = pd.read_csv("Cockroach_alleles.csv")
df_beetle = pd.read_csv("Beetle_alleles.csv")
df_fruitfly = pd.read_csv("Fruitfly_alleles.csv")
df_moth = pd.read_csv("Moth_alleles.csv")
df_threehopper = pd.read_csv("Treehopper_alleles.csv")
df_asptbug = pd.read_csv("Adler Spittlebug_alleles.csv")
df_tick = pd.read_csv("Tick_alleles.csv")
df_wasp = pd.read_csv("Wasp_alleles.csv")
df_fairyfly = pd.read_csv("Fairyfly_alleles.csv")
df_aphid = pd.read_csv("Aphid_alleles.csv")

#Platyhelminthes
df_tapeworm = pd.read_csv("Tapeworm_alleles.csv")

#plants
df_lettuce = pd.read_csv("lettuce_bv_associated_varicosavirus_alleles.csv")
df_papaya = pd.read_csv("papaya_cytorhabdovirus_alleles.csv")
df_rice = pd.read_csv("rice_cytorhabdovirus_alleles.csv")
df_orange = pd.read_csv("Orange_alleles.csv")
df_tomato = pd.read_csv("Tomato_alleles.csv")

#main script once all data have been parsed
mammalian = pd.concat([df_rabies_human["Epitopes"],
                       df_eblv2_human["Epitopes"],
                       df_eblv2_bat["Epitopes"],
                       df_rabies_non_human["Epitopes"],
                       df_dolphin["Epitopes"], df_indiana["Epitopes"]],
                      ignore_index=True)

non_mammalian = pd.concat([df_ycb["Epitopes"], df_grrenbul["Epitopes"],
                           df_bird["Epitopes"], df_fish["Epitopes"],
                           df_perch["Epitopes"], df_carp["Epitopes"],
                           df_cockroach["Epitopes"], df_beetle["Epitopes"],
                           df_fruitfly["Epitopes"], df_moth["Epitopes"],
                           df_threehopper["Epitopes"], df_asptbug["Epitopes"],
                           df_tick["Epitopes"], df_wasp["Epitopes"],
                           df_fairyfly["Epitopes"], df_tapeworm["Epitopes"],
                           df_aphid["Epitopes"], df_lettuce["Epitopes"],
                           df_papaya["Epitopes"], df_rice["Epitopes"],
                           df_orange["Epitopes"], df_tomato["Epitopes"]],
                          ignore_index=True)


#test of normality
stat, p = normaltest(mammalian)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')

#test of normality
stat, p = normaltest(non_mammalian)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')

#first comparison between mammalian and non-mammalian viruses
rabdoa_overall = ttest_ind(mammalian, non_mammalian)

#individual alleles comparison
#HLA-A0101
mammalian_a1 = pd.concat([df_rabies_human[df_rabies_human["Allele"] ==
                                          "HLA-A0101"]["Epitopes"],
                       df_eblv2_human[df_eblv2_human["Allele"] ==
                                      "HLA-A0101"]["Epitopes"],
                       df_eblv2_bat[df_eblv2_bat["Allele"] ==
                                    "HLA-A0101"]["Epitopes"],
                       df_rabies_non_human[df_rabies_non_human["Allele"] ==
                                           "HLA-A0101"]["Epitopes"],
                       df_dolphin[df_dolphin["Allele"] ==
                                  "HLA-A0101"]["Epitopes"],
                       df_indiana[df_indiana["Allele"] ==
                                  "HLA-A0101"]["Epitopes"]],
                      ignore_index=True)

non_mammalian_a1 = pd.concat([df_ycb[df_ycb["Allele"] ==
                                     "HLA-A0101"]["Epitopes"],
                       df_grrenbul[df_grrenbul["Allele"] ==
                                   "HLA-A0101"]["Epitopes"],
                       df_bird[df_bird["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_fish[df_fish["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_perch[df_perch["Allele"] ==
                                "HLA-A0101"]["Epitopes"],
                       df_carp[df_carp["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_cockroach[df_cockroach["Allele"] ==
                                    "HLA-A0101"]["Epitopes"],
                       df_beetle[df_beetle["Allele"] ==
                                 "HLA-A0101"]["Epitopes"],
                       df_fruitfly[df_fruitfly["Allele"] ==
                                   "HLA-A0101"]["Epitopes"],
                       df_moth[df_moth["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_threehopper[df_threehopper["Allele"] ==
                                      "HLA-A0101"]["Epitopes"],
                       df_asptbug[df_asptbug["Allele"] ==
                                  "HLA-A0101"]["Epitopes"],
                       df_tick[df_tick["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_wasp[df_wasp["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_fairyfly[df_fairyfly["Allele"] ==
                                   "HLA-A0101"]["Epitopes"],
                       df_tapeworm[df_tapeworm["Allele"] ==
                                   "HLA-A0101"]["Epitopes"],
                       df_aphid[df_aphid["Allele"] ==
                                "HLA-A0101"]["Epitopes"],
                       df_lettuce[df_lettuce["Allele"] ==
                                  "HLA-A0101"]["Epitopes"],
                       df_papaya[df_papaya["Allele"] ==
                                 "HLA-A0101"]["Epitopes"],
                       df_rice[df_rice["Allele"] ==
                               "HLA-A0101"]["Epitopes"],
                       df_orange[df_orange["Allele"] ==
                                 "HLA-A0101"]["Epitopes"],
                       df_tomato[df_tomato["Allele"] ==
                                 "HLA-A0101"]["Epitopes"]],
                      ignore_index=True)

#result
rabdoa1 = ttest_ind(mammalian_a1, non_mammalian_a1)


#HLA-A0201
mammalian_a2 = pd.concat([df_rabies_human[df_rabies_human["Allele"] ==
                                          "HLA-A0201"]["Epitopes"],
                       df_eblv2_human[df_eblv2_human["Allele"] ==
                                      "HLA-A0201"]["Epitopes"],
                       df_eblv2_bat[df_eblv2_bat["Allele"] ==
                                    "HLA-A0201"]["Epitopes"],
                       df_rabies_non_human[df_rabies_non_human["Allele"] ==
                                           "HLA-A0201"]["Epitopes"],
                       df_dolphin[df_dolphin["Allele"] ==
                                  "HLA-A0201"]["Epitopes"],
                       df_indiana[df_indiana["Allele"] ==
                                  "HLA-A0201"]["Epitopes"]],
                      ignore_index=True)

non_mammalian_a2 = pd.concat([df_ycb[df_ycb["Allele"] ==
                                     "HLA-A0201"]["Epitopes"],
                       df_grrenbul[df_grrenbul["Allele"] ==
                                   "HLA-A0201"]["Epitopes"],
                       df_bird[df_bird["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_fish[df_fish["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_perch[df_perch["Allele"] ==
                                "HLA-A0201"]["Epitopes"],
                       df_carp[df_carp["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_cockroach[df_cockroach["Allele"] ==
                                    "HLA-A0201"]["Epitopes"],
                       df_beetle[df_beetle["Allele"] ==
                                 "HLA-A0201"]["Epitopes"],
                       df_fruitfly[df_fruitfly["Allele"] ==
                                   "HLA-A0201"]["Epitopes"],
                       df_moth[df_moth["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_threehopper[df_threehopper["Allele"] ==
                                      "HLA-A0201"]["Epitopes"],
                       df_asptbug[df_asptbug["Allele"] ==
                                  "HLA-A0201"]["Epitopes"],
                       df_tick[df_tick["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_wasp[df_wasp["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_fairyfly[df_fairyfly["Allele"] ==
                                   "HLA-A0201"]["Epitopes"],
                       df_tapeworm[df_tapeworm["Allele"] ==
                                   "HLA-A0201"]["Epitopes"],
                       df_aphid[df_aphid["Allele"] ==
                                "HLA-A0201"]["Epitopes"],
                       df_lettuce[df_lettuce["Allele"] ==
                                  "HLA-A0201"]["Epitopes"],
                       df_papaya[df_papaya["Allele"] ==
                                 "HLA-A0201"]["Epitopes"],
                       df_rice[df_rice["Allele"] ==
                               "HLA-A0201"]["Epitopes"],
                       df_orange[df_orange["Allele"] ==
                                 "HLA-A0201"]["Epitopes"],
                       df_tomato[df_tomato["Allele"] ==
                                 "HLA-A0201"]["Epitopes"]],
                      ignore_index=True)

#result
rabdoa2 = ttest_ind(mammalian_a2, non_mammalian_a2)

#HLA-A0301

mammalian_a3 = pd.concat([df_rabies_human[df_rabies_human["Allele"] ==
                                          "HLA-A0301"]["Epitopes"],
                       df_eblv2_human[df_eblv2_human["Allele"] ==
                                      "HLA-A0301"]["Epitopes"],
                       df_eblv2_bat[df_eblv2_bat["Allele"] ==
                                    "HLA-A0301"]["Epitopes"],
                       df_rabies_non_human[df_rabies_non_human["Allele"] ==
                                           "HLA-A0301"]["Epitopes"],
                       df_dolphin[df_dolphin["Allele"] ==
                                  "HLA-A0301"]["Epitopes"],
                       df_indiana[df_indiana["Allele"] ==
                                  "HLA-A0301"]["Epitopes"]],
                      ignore_index=True)

non_mammalian_a3 = pd.concat([df_ycb[df_ycb["Allele"] ==
                                     "HLA-A0301"]["Epitopes"],
                       df_grrenbul[df_grrenbul["Allele"] ==
                                   "HLA-A0301"]["Epitopes"],
                       df_bird[df_bird["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_fish[df_fish["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_perch[df_perch["Allele"] ==
                                "HLA-A0301"]["Epitopes"],
                       df_carp[df_carp["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_cockroach[df_cockroach["Allele"] ==
                                    "HLA-A0301"]["Epitopes"],
                       df_beetle[df_beetle["Allele"] ==
                                 "HLA-A0301"]["Epitopes"],
                       df_fruitfly[df_fruitfly["Allele"] ==
                                   "HLA-A0301"]["Epitopes"],
                       df_moth[df_moth["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_threehopper[df_threehopper["Allele"] ==
                                      "HLA-A0301"]["Epitopes"],
                       df_asptbug[df_asptbug["Allele"] ==
                                  "HLA-A0301"]["Epitopes"],
                       df_tick[df_tick["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_wasp[df_wasp["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_fairyfly[df_fairyfly["Allele"] ==
                                   "HLA-A0301"]["Epitopes"],
                       df_tapeworm[df_tapeworm["Allele"] ==
                                   "HLA-A0301"]["Epitopes"],
                       df_aphid[df_aphid["Allele"] ==
                                "HLA-A0301"]["Epitopes"],
                       df_lettuce[df_lettuce["Allele"] ==
                                  "HLA-A0301"]["Epitopes"],
                       df_papaya[df_papaya["Allele"] ==
                                 "HLA-A0301"]["Epitopes"],
                       df_rice[df_rice["Allele"] ==
                               "HLA-A0301"]["Epitopes"],
                       df_orange[df_orange["Allele"] ==
                                 "HLA-A0301"]["Epitopes"],
                       df_tomato[df_tomato["Allele"] ==
                                 "HLA-A0301"]["Epitopes"]],
                      ignore_index=True)

#result
rabdoa3 = ttest_ind(mammalian_a3, non_mammalian_a3)

#HLA-A1101
mammalian_a11 = pd.concat([df_rabies_human[df_rabies_human["Allele"] ==
                                           "HLA-A1101"]["Epitopes"],
                       df_eblv2_human[df_eblv2_human["Allele"] ==
                                      "HLA-A1101"]["Epitopes"],
                       df_eblv2_bat[df_eblv2_bat["Allele"] ==
                                    "HLA-A1101"]["Epitopes"],
                       df_rabies_non_human[df_rabies_non_human["Allele"] ==
                                           "HLA-A1101"]["Epitopes"],
                       df_dolphin[df_dolphin["Allele"] ==
                                  "HLA-A1101"]["Epitopes"],
                       df_indiana[df_indiana["Allele"] ==
                                  "HLA-A1101"]["Epitopes"]],
                      ignore_index=True)

non_mammalian_a11 = pd.concat([df_ycb[df_ycb["Allele"] ==
                                      "HLA-A1101"]["Epitopes"],
                       df_grrenbul[df_grrenbul["Allele"] ==
                                   "HLA-A1101"]["Epitopes"],
                       df_bird[df_bird["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_fish[df_fish["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_perch[df_perch["Allele"] ==
                                "HLA-A1101"]["Epitopes"],
                       df_carp[df_carp["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_cockroach[df_cockroach["Allele"] ==
                                    "HLA-A1101"]["Epitopes"],
                       df_beetle[df_beetle["Allele"] ==
                                 "HLA-A1101"]["Epitopes"],
                       df_fruitfly[df_fruitfly["Allele"] ==
                                   "HLA-A1101"]["Epitopes"],
                       df_moth[df_moth["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_threehopper[df_threehopper["Allele"] ==
                                      "HLA-A1101"]["Epitopes"],
                       df_asptbug[df_asptbug["Allele"] ==
                                  "HLA-A1101"]["Epitopes"],
                       df_tick[df_tick["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_wasp[df_wasp["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_fairyfly[df_fairyfly["Allele"] ==
                                   "HLA-A1101"]["Epitopes"],
                       df_tapeworm[df_tapeworm["Allele"] ==
                                   "HLA-A1101"]["Epitopes"],
                       df_aphid[df_aphid["Allele"] ==
                                "HLA-A1101"]["Epitopes"],
                       df_lettuce[df_lettuce["Allele"] ==
                                  "HLA-A1101"]["Epitopes"],
                       df_papaya[df_papaya["Allele"] ==
                                 "HLA-A1101"]["Epitopes"],
                       df_rice[df_rice["Allele"] ==
                               "HLA-A1101"]["Epitopes"],
                       df_orange[df_orange["Allele"] ==
                                 "HLA-A1101"]["Epitopes"],
                       df_tomato[df_tomato["Allele"] ==
                                 "HLA-A1101"]["Epitopes"]],
                      ignore_index=True)

#result
rabdoa11 = ttest_ind(mammalian_a11, non_mammalian_a11)

#HLA-A2402

mammalian_a24 = pd.concat([df_rabies_human[df_rabies_human["Allele"] ==
                                           "HLA-A2402"]["Epitopes"],
                       df_eblv2_human[df_eblv2_human["Allele"] ==
                                      "HLA-A2402"]["Epitopes"],
                       df_eblv2_bat[df_eblv2_bat["Allele"] ==
                                    "HLA-A2402"]["Epitopes"],
                       df_rabies_non_human[df_rabies_non_human["Allele"] ==
                                           "HLA-A2402"]["Epitopes"],
                       df_dolphin[df_dolphin["Allele"] ==
                                  "HLA-A2402"]["Epitopes"],
                       df_indiana[df_indiana["Allele"] ==
                                  "HLA-A2402"]["Epitopes"]],
                      ignore_index=True)

non_mammalian_a24 = pd.concat([df_ycb[df_ycb["Allele"] ==
                                      "HLA-A2402"]["Epitopes"],
                       df_grrenbul[df_grrenbul["Allele"] ==
                                   "HLA-A2402"]["Epitopes"],
                       df_bird[df_bird["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_fish[df_fish["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_perch[df_perch["Allele"] ==
                                "HLA-A2402"]["Epitopes"],
                       df_carp[df_carp["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_cockroach[df_cockroach["Allele"] ==
                                    "HLA-A2402"]["Epitopes"],
                       df_beetle[df_beetle["Allele"] ==
                                 "HLA-A2402"]["Epitopes"],
                       df_fruitfly[df_fruitfly["Allele"] ==
                                   "HLA-A2402"]["Epitopes"],
                       df_moth[df_moth["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_threehopper[df_threehopper["Allele"] ==
                                      "HLA-A2402"]["Epitopes"],
                       df_asptbug[df_asptbug["Allele"] ==
                                  "HLA-A2402"]["Epitopes"],
                       df_tick[df_tick["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_wasp[df_wasp["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_fairyfly[df_fairyfly["Allele"] ==
                                   "HLA-A2402"]["Epitopes"],
                       df_tapeworm[df_tapeworm["Allele"] ==
                                   "HLA-A2402"]["Epitopes"],
                       df_aphid[df_aphid["Allele"] ==
                                "HLA-A2402"]["Epitopes"],
                       df_lettuce[df_lettuce["Allele"] ==
                                  "HLA-A2402"]["Epitopes"],
                       df_papaya[df_papaya["Allele"] ==
                                 "HLA-A2402"]["Epitopes"],
                       df_rice[df_rice["Allele"] ==
                               "HLA-A2402"]["Epitopes"],
                       df_orange[df_orange["Allele"] ==
                                 "HLA-A2402"]["Epitopes"],
                       df_tomato[df_tomato["Allele"] ==
                                 "HLA-A2402"]["Epitopes"]],
                      ignore_index=True)

rabdoa24 = ttest_ind(mammalian_a24, non_mammalian_a24)

#all results for this data set are printed
print("Overall: ", rabdoa_overall)
print("A01:01: ", rabdoa1)
print("A02:01: ", rabdoa2)
print("A03:01: ", rabdoa3)
print("A11:01: ", rabdoa11)
print("A24:02: ", rabdoa24)

#******************************************************************************
#Ancient and novel data set

#human
df_rabies_human = pd.read_csv(r"C:\Users\Joan\Documents\Dissertation\Multispp\Analysis\Total alleleles\rabies_human_alleles.csv")
df_eblv2_human = pd.read_csv(r"C:\Users\Joan\Documents\Dissertation\Multispp\Analysis\Total alleleles\eblv2_human_alleles.csv")
df_zika = pd.read_csv("zika_alleles.csv")
df_dengue = pd.read_csv("denv3_alleles.csv")
df_lassafever = pd.read_csv("lassafever_alleles.csv")

#Ancient
df_marsellevirus = pd.read_csv("brazil_marsellevirus_alleles.csv")
df_oanv1 = pd.read_csv("oanv1_alleles.csv")
df_oanv2 = pd.read_csv("oanv2_alleles.csv")
df_panv1 = pd.read_csv("panv1_alleles.csv")
df_panv2 = pd.read_csv("panv2_alleles.csv")
df_spiny = pd.read_csv("spiny_alleles.csv")
df_tibetan_iceglacier = pd.read_csv("tibetan_iceglacier_alleles.csv")
df_tibetan_riverwater = pd.read_csv("tibetan_riverwater_amended_alleles.csv")

human = pd.concat([df_rabies_human, df_eblv2_human,
                   df_zika, df_dengue,
                   df_lassafever], ignore_index=True)

ancient = pd.concat([df_marsellevirus, df_oanv1,
                     df_oanv2, df_panv1,
                     df_panv2, df_spiny,
                     df_tibetan_iceglacier, df_tibetan_riverwater],
                    ignore_index=True)

human = human[["Allele", "Epitope normalised"]]
human = human.dropna()
ancient = ancient[["Allele", "Epitope normalised"]]

#test of normality
stat, p = normaltest(human["Epitope normalised"])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')

#test of normality
stat, p = normaltest(ancient["Epitope normalised"])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')

#Mann-Whitney U test
ancients_overall = stats.mannwhitneyu(x = human["Epitope normalised"],
                                      y = ancient["Epitope normalised"],
                   alternative = 'two-sided')

ancients_side = stats.mannwhitneyu(x = human["Epitope normalised"],
                                   y = ancient["Epitope normalised"],
                   alternative = 'greater')

#comparison for each allele

#HLA-A0101

human_a1 = pd.concat([human[human["Allele"] ==
                            "HLA-A0101"]["Epitope normalised"]],
                      ignore_index=True)

ancient_a1 = pd.concat([ancient[ancient["Allele"] ==
                                "HLA-A0101"]["Epitope normalised"]],
                      ignore_index=True)

ancients_a1 = stats.mannwhitneyu(x = human_a1,
                                 y = ancient_a1, alternative = 'two-sided')


#HLA-A0201

human_a2 = pd.concat([human[human["Allele"] ==
                            "HLA-A0201"]["Epitope normalised"]],
                      ignore_index=True)

ancient_a2 = pd.concat([ancient[ancient["Allele"] ==
                                "HLA-A0201"]["Epitope normalised"]],
                      ignore_index=True)

stats.mannwhitneyu(x = human_a2, y = ancient_a2, alternative = 'two-sided')


#HLA-A0301

human_a3 = pd.concat([human[human["Allele"] ==
                            "HLA-A0301"]["Epitope normalised"]],
                      ignore_index=True)

ancient_a3 = pd.concat([ancient[ancient["Allele"] ==
                                "HLA-A0301"]["Epitope normalised"]],
                      ignore_index=True)

ancients_a3 = stats.mannwhitneyu(x = human_a3,
                   y = ancient_a3, alternative = 'two-sided')


#HLA-A1101

human_a11 = pd.concat([human[human["Allele"] ==
                             "HLA-A1101"]["Epitope normalised"]],
                      ignore_index=True)

ancient_a11 = pd.concat([ancient[ancient["Allele"] ==
                                 "HLA-A1101"]["Epitope normalised"]],
                      ignore_index=True)

stats.mannwhitneyu(x = human_a11, y = ancient_a11, alternative = 'two-sided')

#HLA-A2402

human_a24 = pd.concat([human[human["Allele"] ==
                             "HLA-A2402"]["Epitope normalised"]],
                      ignore_index=True)

ancient_a24 = pd.concat([ancient[ancient["Allele"] ==
                                 "HLA-A2402"]["Epitope normalised"]],
                      ignore_index=True)

ancients_a24 = stats.mannwhitneyu(x = human_a24,
                   y = ancient_a24, alternative = 'two-sided')

#all results for this data set are printed
print("Overall: ", ancients_overall)
print("Overall greater side: ", ancients_side)
print("A01:01: ", ancients_a1)
print("A02:01: ", ancients_a2)
print("A03:01: ", ancients_a3)
print("A11:01: ", ancients_a11)
print("A24:02: ", ancients_a24)
