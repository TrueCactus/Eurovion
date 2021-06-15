# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:37:13 2021

@author: TrueCactus
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Le tableau (javascript) des résultats n'est pas accessible via BeautifulSoup, Selenium est donc requis.

#ouvrir la session Chrome via Selenium :
url='http://eurovisionworld.com/eurovision/2021'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

#Resultat totaux
#Le tableau des resultats totaux est visible lorsque le bouton "Total" est enclenché.
python_button = driver.find_element_by_xpath('//*[@id="scoreboard"]/div[1]/button[1]') # Selenium va chercher le bouton.
python_button.click() #Selenium clique dessus
soup = BeautifulSoup(driver.page_source) # On peut maintenant acceder à la version "Total" du tableau.
tables = soup.find_all('table')
dfs = pd.read_html(str(tables))
Resultat_Eurovision_totaux=dfs[4].iloc[:,2:].rename(columns={'Unnamed: 2': 'Country','Unnamed: 3': 'Result_tot'})
Resultat_Eurovision_totaux

#Resultat télé
#Le tableau des resultats télé est visible lorsque le bouton "Tele" est enclenché.
python_button = driver.find_element_by_xpath('//*[@id="scoreboard"]/div[1]/button[2]')
python_button.click()
soup = BeautifulSoup(driver.page_source)
tables = soup.find_all('table')
dfs = pd.read_html(str(tables))
Resultat_Eurovision_tele=dfs[4].iloc[:,2:].rename(columns={'Unnamed: 2': 'Country','Unnamed: 3': 'Result_tot'})
Resultat_Eurovision_tele


#Resultat Jury
#Le tableau des resultats du Jury est visible lorsque le bouton "Jury" est enclenché.
python_button = driver.find_element_by_xpath('//*[@id="scoreboard"]/div[1]/button[3]')
python_button.click()
soup = BeautifulSoup(driver.page_source)
tables = soup.find_all('table')
dfs = pd.read_html(str(tables))
Resultat_Eurovision_jury=dfs[4].iloc[:,2:].rename(columns={'Unnamed: 2': 'Country','Unnamed: 3': 'Result_tot'})
Resultat_Eurovision_jury


#Pays Votants (mauvaise liste)
Xpath='//*[@id="pageright"]/div[7]/div/div'
Pays_Votant=driver.find_elements_by_xpath(Xpath)
Liste_Pays_Votants=Pays_Votant[0].text.split("\n")


    
#Pays Votants (bonne liste)  
url_pays_votants="https://eurovisionworld.com/eurovision/2021/event#participants"
Xpath='//*[@id="page"]/div[2]/main/article/div[3]/div[1]'
driver.get(url_pays_votants)
Pays_Votant=driver.find_element_by_xpath(Xpath)
Liste_Pays_Votants=Pays_Votant.text.split("\n")
Liste_Columns= ["Country","Result_tot"]+Liste_Pays_Votants
for table in [Resultat_Eurovision_totaux,Resultat_Eurovision_tele,Resultat_Eurovision_jury]:
    table.columns = Liste_Columns
    

#Enregistrement des tables    
Resultat_Eurovision_totaux.to_csv("Resultat_totaux.csv",index=False)
Resultat_Eurovision_tele.to_csv("Resultat_tele.csv",index=False)
Resultat_Eurovision_jury.to_csv("Resultat_jury.csv",index=False)


driver.close()