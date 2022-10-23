README

MSc Bioinformatics with Systems Biology Dissertation

Exploratory analysis of T-cell epitopes
interactions with viruses

Joan Manuel Amaya Cuesta

Supervised by Dr Adrian Shepherd

MSc Bioinformatics with Systems Biology
Birkbeck College, University of London
Malet St, Bloomsbury, London WC1E 7HX, UK


All the code stored in this repository has been written as part of the dissertation 
for the MSc Bioinformatics with Systems Biology.
The different scripts are based on the sections of the dissertation.
NetMHCpan - 4.1 [1] has been used as an epitope prediction tool, and the scripts 
stored in this repository are used for downstream parsing and analysis.

The order of the scripts in order to be used or to follow the dissertation are:
1.	Data Parser (data_parser.py) is the first program used to parse the output from NetMHCpan - 4.1.
2.	Joiner (joiner_mapper) refined the parsed data and map metadata from the ViPR [2] or another 
    suitable database to generate two CSV files ready for data visualisation or epitope analysis.
3.	Epitope Finder (epitope_finder.py) is used for the “Assessment of epitope depletion in zoonotic viruses” section.
4.	Visualiser (changes_over_time.py) uses the data parsed in Joiner to return bar plots showing the 
    overall trends per allele and year. This is part of the “Incursion of Zika Virus in Brazil” section.
5.	Variability (epitopes_variability.py) uses the other CSV file returned in the Joiner program and 
    further analyses the epitope’s variability as a bar plot visualisation. This is part of the 
     “Incursion of Zika Virus in Brazil” section.
6.	MHC-driven (mhc_driven.py) uses the data parsed in the Joiner program and then provides statistical 
    comparisons of two data sets. This is part of the “Comparison of MHC-driven viruses and 
     non-MHC-driven viruses” section.

AUTHOR

Joan Manuel Amaya Cuesta

Copyright:  (c) Joan M. Amaya C., 2022


THANKS

I would like to thank my supervisor Dr Adrian Shepherd for his guidance throughout this dissertation.

Also, I would want to thank Dr Lorraine McElhinney for her support all this time.

REFERENCES
[1] [17] Reynisson, B., Alvarez, B., Paul, S., Peters, B., & Nielsen, M. (2020). 
NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation 
by concurrent motif deconvolution and integration of MS MHC eluted ligand data. 
Nucleic acids research, 48(W1), W449–W454. https://doi.org/10.1093/nar/gkaa379

[2] Pickett, B. E., Sadat, E. L., Zhang, Y., Noronha, J. M., Squires, R. B., Hunt, V., 
Liu, M., Kumar, S., Zaremba, S., Gu, Z., Zhou, L., Larson, C. N., Dietrich, J., Klem, E. B., & Scheuermann, R. H. (2012). 
ViPR: an open bioinformatics database and analysis resource for virology research. 
Nucleic acids research, 40(Database issue), D593–D598. https://doi.org/10.1093/nar/gkr859 


