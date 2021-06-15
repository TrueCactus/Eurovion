# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:49:20 2021

@author: TrueCactus
"""
#import librairies
import numpy as np
import plotly.express
import streamlit as st
import pandas as pd
from pycountry_convert import country_name_to_country_alpha3
import plotly.express as px
import plotly.graph_objects as go

def Country_Code (Country) :
    return country_name_to_country_alpha3(Country)

#import Data
Eurovision_tot=pd.read_csv("Resultat_totaux_latlong.csv")
Euro_tr_complete=pd.read_csv("Resultat_totaux_transpose.csv")
Euro_tr=Euro_tr_complete.iloc[1:,:]
Country_df=pd.read_csv("Code_country.csv")
Youtube_link=pd.read_csv("Youtube_link.csv")
Euro_jury_tr=pd.read_csv("Resultat_jury_transpose.csv").iloc[1:,:]
Point_jury=pd.read_csv("Resultat_jury.csv")
df_uk=pd.read_csv("uk.csv")


link = '[GitHub](http://github.com)'


st.sidebar.write("Menu")
st.sidebar.button("Distribution des points")
st.sidebar.button("Prestations")
st.sidebar.button("Royaume Uni")

url1="http://localhost:8501/#distribution-g-ographique-des-points"
url2="http://localhost:8501/#prestation-lors-de-la-final"
url3="http://localhost:8501/#prestation-lors-de-la-final"




#affichage titre
st.header("Eurovion : les résultats ")
st.subheader("Distribution géographique des points :")

#Mettre le bouton radio à l'horizontal
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

col1, col2,col3 = st.beta_columns([0.2,0.6,0.2]) 
choix=col2.radio('Points', ["Total","Jury","Tele"])  
    
    
# #Creation buttons 
# col1, col2,col3,col4,col5 = st.beta_columns([0.2,0.2,0.2,0.2,0.2])  
# b1 = col2.button("Total", key="1")
# b2 = col3.button("Jury", key="2")
# b3 = col4.button("Télé", key="3")

# total=st.checkbox("Total")
# jury=st.checkbox("Jury")
# tele=st.checkbox("Télé")




col_swe = 'red'

#Creation Graphes Total
Graphes=[]
for country in Euro_tr.columns[1:-1] :

    Graphe=go.Figure(data=go.Choropleth(
    locations=Euro_tr['Country_code'], # Spatial coordinates
    z = Euro_tr[country], # Data to be color-coded
    locationmode = "ISO-3",
    colorbar_title = "Points donnés",
    autocolorscale= False,
    colorscale="viridis",
    text=Euro_tr['Country'],
   ))
    
    
    Graphe.update_layout(
    title_text = "Total :Points donnés à {fcountry} qui a remporté {fpoints} points".format(fcountry = country, fpoints = Eurovision_tot['Result_tot'][Eurovision_tot["Country"]==country].values[0]),
    margin={"r":55,"t":55,"l":55,"b":55},
    height=500,
    )
    #geo_scope="europe" )
    
    Graphe.update_geos(
    center=dict(lon= 23, lat= 54),
    lataxis_range=[31.0529,-40.4296], lonaxis_range=[-24, 88.2421],
    projection_scale=3
    #fitbounds="locations"
    )
    
    
    Graphe.add_traces(go.Choropleth(locations=Country_df['Country_code'][Country_df["Country"]==country],
                            z = [1],
                            colorscale = [[0, col_swe],[1, col_swe]],
                            colorbar=None,
                            showscale = False))
    
    Graphes.append(Graphe)
    
    
#Creation Graphes Jury
Graphes_jury=[]
for country in Euro_jury_tr.columns[1:-1] :

    Graphe=go.Figure(data=go.Choropleth(
    locations=Euro_jury_tr['Country-code'], # Spatial coordinates
    z = Euro_jury_tr[country], # Data to be color-coded
    locationmode = "ISO-3",
    colorbar_title = "Points donnés",
    autocolorscale= False,
    colorscale="viridis",
    text=Euro_jury_tr['Country'],
   ))
    
    
    Graphe.update_layout(
    title_text = "Jury :Points donnés à {fcountry} qui a remporté {fpoints} points".format(fcountry = country, fpoints = Point_jury['Result_tot'][Point_jury["Country"]==country].values[0]),
    margin={"r":55,"t":55,"l":55,"b":55},
    height=500,
    )
    #geo_scope="europe" )
    
    Graphe.update_geos(
    center=dict(lon= 23, lat= 54),
    lataxis_range=[31.0529,-40.4296], lonaxis_range=[-24, 88.2421],
    projection_scale=3
    #fitbounds="locations"
    )
    
    
    Graphe.add_traces(go.Choropleth(locations=Country_df['Country_code'][Country_df["Country"]==country],
                            z = [1],
                            colorscale = [[0, col_swe],[1, col_swe]],
                            colorbar=None,
                            showscale = False))
    
    Graphes_jury.append(Graphe)    
    
    
    
    
    
    
  
    
    
#creation liste selection des pays à choisir
col12, col22 = st.beta_columns([0.2,0.8])    
Pays=list(Euro_tr.columns[1:-1])
Selection_Pays = col12.selectbox('',(Pays))  

#Affichage des graphes selon selectione et bouttons :

# Par défaut et button Total actif
if choix=="Total":
#if (b2==False and b3==False) or b1 :
    for country in Pays :
        if Selection_Pays== country :
            col22.plotly_chart(Graphes[Pays.index(country)])
      
#Button Jury actif   
if choix =="Jury":           
#if b2 :
    for country in Pays :
        if Selection_Pays== country :
            col22.plotly_chart(Graphes_jury[list(Euro_jury_tr.columns[1:-1]).index(country)])      


st.subheader("Prestation lors de la final !") 
col13, col23,col33 = st.beta_columns([0.2,0.6,0.2])

# Affichage video youtube selon selection



for country in Pays :
    if Selection_Pays== country :
      col23.subheader("{fcountry} : Visionnez la prestastion".format(fcountry=country))
      col23.video(data=Youtube_link['Link'][Youtube_link["Country"]==country].values[0])
   
 
    
    
st.empty()

st.subheader("Des points pour le Royaume-Uni !")    
form = st.form(key='my_form')
point_form=form.radio('Combien de points souhaitez vous donnez au Royaume Uni ?', list(range(1, 13)))
submit_button = form.form_submit_button(label='donner') 


if point_form==4 :
    st.write("bravo 4 points" )
    df_uk['UK'][0]+=4
    df_uk.to_csv("uk.csv",index=False)
    
    
if point_form==12 :
    st.balloons()
    st.write("bravo 12 points" )
    df_uk['UK'][0]+=12
    df_uk.to_csv("uk.csv",index=False)
    
    
    
st.write("Les gens qui sont venus ici ont donnés un total de {fpoints} points au Royaum Uni".format(fpoints=df_uk['UK'][0]))   
