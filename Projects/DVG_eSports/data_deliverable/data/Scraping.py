from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#change this to where you chrome driver is, download: https://chromedriver.chromium.org/downloads
#Reference: https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a 
driver = webdriver.Chrome('/Users/grass/Desktop/cs1951a/DVG_eSports_final_project/data_deliverable/data/chromedriver')
driver.maximize_window() # For maximizing window


import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3
import numpy as np
import sys 
import time
import os
#--------------------------------------Name to IGN Scraping------------------------------------------------
gamepedia = "https://lol.gamepedia.com/"
trackThePros = "https://www.trackingthepros.com/player/"
path = "/Users/grass/Desktop/cs1951a/DVG_eSports_final_project/data_deliverable/data/LCS 2021 Spring - Player Stats - OraclesElixir.csv" 
with open(path, 'rb') as f:
  df = pd.read_csv(f)
print("Finished reading data!")

soloQids = []
playerNames =[]
position = []
proKills = []
proDeaths = []
proAssists = []
currTeam = []
winRate = []
for player in df['Player']:
    playerNames.append(player)
    #Get soloq_ids

print(playerNames)
for player in playerNames:

    #Open website to scrape

    driver.get(trackThePros + player)
    #wait for page to load
    time.sleep(2)
    #Scrape the soloqname from the cards, want to get only one..

    #Clicks every checkbox EXCEPT soloq
    tweet = driver.find_element_by_id("show_tweet")
    driver.execute_script("arguments[0].click();", tweet)

    reddit = driver.find_element_by_id("show_reddit")
    driver.execute_script("arguments[0].click();", reddit)

    twitch = driver.find_element_by_id("show_twitch")
    driver.execute_script("arguments[0].click();", twitch)
    time.sleep(1)
    stream = driver.find_element_by_id("show_stream")
    driver.execute_script("arguments[0].click();", stream)

    #waits for page to update
    time.sleep(1)
    try:
        soloQid = driver.find_element_by_class_name("soloq_name").text
    except:
        print("Player has no recent match history. Could not retrieve soloQid!")
        soloQids.append("Not Available")
        continue
    
    print(soloQid)
    #Case for non-NA players, cannot get info on them
    trueID = soloQid.split("] ")
    print(trueID)
    if trueID[0] != "[NA":
        soloQids.append("Not Available")
        print("Player does not have history in NA")
    else:
        soloQids.append(trueID[1])

#extracts relevant info from csv
for player in playerNames:
    for row in df.itertuples(index=False):
        if row[0].lower() == player.lower():
            gamesPlayed = row[3]
            currTeam.append(row[1])
            position.append(row[2])
            proKills.append(float(row[6])/gamesPlayed)
            proDeaths.append(float(row[7])/gamesPlayed)
            proAssists.append(float(row[8])/gamesPlayed)
            winRate.append(float(row[4].split('%')[0]))


#saves all to a csv
dict = {'soloQids': soloQids, 'playerNames': playerNames, 'position': position, 'proKills': proKills, 
'proDeaths': proDeaths, 'proAssists': proAssists, 'currTeam': currTeam, 'winRate': winRate}  
       
df = pd.DataFrame(dict) 
    
df.to_csv('IGNScrape.csv', index = False) 