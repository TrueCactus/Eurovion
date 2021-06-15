# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:20:43 2021

@author: TrueCactus
"""


import numpy as np
import pandas as pd
from pycountry_convert import country_name_to_country_alpha3


Eurovision_tot=pd.read_csv("Resultat_totaux.csv")
Eurovision_Jury=pd.read_csv("Resultat_jury.csv")
df_tr = Eurovision_tot.transpose()
Jury_tr=Eurovision_Jury.transpose()
Jury_tr=Jury_tr.rename_axis('Country').reset_index()
Jury_tr=Jury_tr.rename(columns=Jury_tr.iloc[0]).drop(Jury_tr.index[0])

def Country_Code (Country) :
    
    try :
      country_name_to_country_alpha3(Country)
      return country_name_to_country_alpha3(Country)
    except:
        # Return missing value
        return np.nan

Eurovision_tot=Eurovision_tot["Country"]
Eurovision_tot["Country_code"]=Eurovision_tot["Country"].apply(Country_Code)

Jury_tr["Country-code"]=Jury_tr["Country"].apply(Country_Code)
Jury_tr.to_csv("Resultat_jury_transpose.csv",index=False)


Coontry_df=Eurovision_tot[["Country","Country_code"]]
Coontry_df.to_csv("Code_country.csv",index=False)


df_tr = df_tr.rename_axis('Country').reset_index()
df_tr["Country_Code"]=df_tr["Country"].apply(Country_Code)

df_tr=df_tr.rename(columns=df_tr.iloc[0]).drop(df_tr.index[0])
df_tr.rename(columns={np.nan: 'Country_code'},inplace=True)
df_tr.to_csv("Resultat_totaux_transpose.csv",index=False)

button=[]
for item in Euro_tr.columns[1:-1] :
    dico=dict (
                    label=item,
                    method="update",
                    args = [{'z': [ Euro_tr[item] ] }],)
    button.append(dico)
    
    
d = {'UK': [0]}
df = pd.DataFrame(data=d)    
df.to_csv("uk.csv",index=False)
