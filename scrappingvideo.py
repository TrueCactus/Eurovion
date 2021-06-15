# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:11:43 2021

@author: TrueCactus

Script pour scrapper les liens Youtubes des prestations de l'eurovision '
"""




import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re


url='https://eurovisionworld.com/eurovision/songs-videos'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


Dico_Youtube={}
for country in Country_df["Country"]:
    Xpath='//*[@id="{fcountry}"]/div[4]/div/div'.format(fcountry=country.lower().replace(" ","-"))
    link = driver.find_element_by_xpath(Xpath) 
    x=link.get_attribute("outerHTML")
    r1 = re.split(r'data-video-iframe="', x)
    r2=re.split(r';showinfo',r1[1])[0]
    Dico_Youtube[country] = r2
    
    
Link_df=pd.DataFrame.from_dict(Dico_Youtube, orient="index",columns=['Link']).rename_axis('Country').reset_index()
Link_df.to_csv("Youtube_link.csv",index=False)
