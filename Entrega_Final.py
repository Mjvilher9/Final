# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

crimes1 = pd.read_csv("Crimes_-_2001_to_present_Part1.csv")
crimes2 = pd.read_csv("Crimes_-_2001_to_present_Part2.csv")



crimes1.describe()
crimes1.head()
crimes1.info()


# 1 ¿En qué año hay más probabilidad de crimenes? 

byyear = crimes1.groupby("Year")
byyear["Year"].count()

byyear=crimes1.groupby("Year")
x = byyear["Year"].count()
y = byyear["Year"].count().sum()

x/y

# R/. 2002 = 8%

Year_diag = crimes1['Year']
sd = sns.distplot(Year_diag, hist=True)
plt.savefig('Year.png')

crimes2 = pd.DataFrame(pd.read_csv("Crimes_-_2001_to_present_Part2.csv"))
crimes2

Xtab = pd.crosstab(crimes2.Year,crimes2.District,margins=True)

Xtab

pd.crosstab(crimes1.Year, crimes1.District)
sns.jointplot(x= "Year", y= "District", data=crimes2)
plt.savefig("D1.png")




# 2. ¿Cuál es la probabilidad que ocurra un crimen de narcóticos en la calle?

loc = crimes.groupby('LocationDescription')
loc['LocationDescription'].count()
# R//. STREET                                             249516
x = loc['LocationDescription'].count()
y = loc['LocationDescription'].count().sum()


z = x/y  
z
# R//. STREET                                             0.238083


loc2 = crimes.groupby('PrimaryType')
loc2['PrimaryType'].count()
# R//. PROSTITUTION                        0.006709

a = loc2['PrimaryType'].count()
b = loc2['PrimaryType'].count().sum()

c = a/b
c
# R//. PROSTITUTION                        0.006709



crimes2 = pd.DataFrame(pd.read_csv("Crimes_-_2001_to_present_Part2.csv"))
crimes2

Xtab = pd.crosstab(crimes2.LocationDescription,crimes2.PrimaryType,margins=True)

Xtab

#R//.STREET = 5504 PROSTITUTION 

pd.crosstab(crimes1.LocationDescription, crimes1.PrimaryType)
sns.jointplot(x= "LocationDescription", y= "PrimaryType", data=crimes2)
plt.savefig("L1.png")







