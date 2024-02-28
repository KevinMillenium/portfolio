# Data Spec
This is where you will be describing your data spec comprehensively. Please refer to the handout for a couple of examples of good data specs.

Each line in the matches database contains one match in the format:

soloqueueName=Ne©ª©ª accountID=FEE5l7NLXiISD0adW4OmZ6BQLxeP9X-qaPg2V9oroVxrELk matchID=3815703533 queueType=900 timestamp=1615152373554 outcome=Win champion=92 lane=JUNGLE kills=4 deaths=2 assists=3

a. soloqueueName - A string that the player uses as his identity in regular games of League of Legends

b. accountID - The unique identifier for the account associated with soloqueueName

c. matchID - The unique identifier for the match played, the higher the number the more recent it was

d. queueType - The gamemode played for the current match. Ranked solo/duo is the most important queue type in regular games of League of Legends
	400 being normals draft,
	420 being ranked solo/duo,
	430 being normals blind,
	440 being ranked flex,
	any other queue type is not related to Summoner's Rift, the main game mode

e. timestamp - The time when the match was played in Epoch timestamp format

f. outcome - either Win or Fail
	If the account that played in the match won, then the outcome is Win. If they lost, the outcome is Fail

g. champion - The ID associated with the champion they played in the match

h. lane - TOP, JUNGLE, MID, BOTTOM, NONE
	The location where the player played during this match, NONE if playing a gamemade that does not utilize lanes

i. kills - The number of kills the player had this match

j. deaths - The number of deaths the player had this match

k. assists - The number of assists the player had this match

Each player in the players database contains one match in the format:

proName=Neo soloqueueName=Ne©ª©ª position=ADC team=Dignitas tier=CHALLENGER rank=I LP=664 kills=55 deaths=22 assists=73

a. proName - A string that the player uses as his identity in Competitive League of Legends, think of a Tournament instead of a school practice match

b. soloqueueName - A string that the player uses as his identity in regular games of League of Legends

c. position - TOP, JUNGLE, MID, ADC, SUPPORT
	The main role of the player

d. team - The orginization the player is part of

e. tier - Current tier in regular League of Legends. Challenger is top 200 of the region, below that is masters, then diamond -> platinum -> gold -> silver -> bronze -> iron

f. rank - The current rank in the tier from I to IV, where I is the higher than IV
	If the player is in challenger or master, the rank is I because there are no ranks within that tier

g. LP - League Points, the more points a person has the better. tiers between iron and diamond are capped at 100LP, but masters/challenger is limitless