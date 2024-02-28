import pandas as pd
import sqlite3

connection = sqlite3.connect("analysis_deliverable/statistics/finaldata1.db")
cursor = connection.cursor()
cursor.execute("SELECT matches.soloqueueName as name, players.position as position, AVG(matches.kills) as avg_kills, AVG(matches.assists) as avg_assists, AVG(matches.deaths) as avg_deaths, players.winrate as winrate FROM matches, players WHERE matches.soloqueueName = players.soloqueueName GROUP BY matches.soloqueueName;")
data = cursor.fetchall()

names = []
position = []
avg_kills = []
avg_assists = []
avg_deaths = []

winrate = []
for x in data:
    names.append(x[0])
    position.append(x[1])
    avg_kills.append(int(x[2]))
    avg_assists.append(int(x[3]))
    avg_deaths.append(int(x[4]))
    winrate.append(int(x[5]))

dict = {'name': names, 'position': position, 'Kills': avg_kills, 'Assists': avg_assists, 'Deaths': avg_deaths, 'Winrate': winrate}

df = pd.DataFrame(dict) 
    
df.to_csv('graph_data.csv', index = False) 