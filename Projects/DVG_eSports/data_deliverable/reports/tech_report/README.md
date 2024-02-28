# Tech Report
This is where you can type out your tech report.

### Our Data ###
***Where is the data from?***
    - We collected our data from Oracles Elixir(spreadsheet with current LCS players), lol.gamepedia.com (to get player solo queue IDs) and  the official Riot API (to get performance stats from their match history)

***How did you collect your data?***
    - Oracles Elixir allowed us to simply download a CSV which we used to get the team and players in a list. Once we had the names of players, we scraped gamepedia to get their solo queue ids. Once we had the list of solo queue ids, we queried the Riot API to get their match history and their performance for (Kills/Death/Assists) along with their respective roles in each match.

***Is the source reputable?***
    -  Yes. Oracles Elixir is widely recognized a the "premier source for advanced League of Legends esports stats". Gamepedia is also reliable as unlike other wikis, they do not allow random users to make changes and the information on the wiki is sourced by official sites. Though Gamepedia does not update soloqueue IDs very quickly, so some of the data scrapped is actually depricated. Finally, the Riot API is very credible as it is officially provided by the developers of League of Legends.

***How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?***
    - Our sample is relatively small, as the full roster of professional players in a tournament season is only about 40 players. We currently have less than that due to some data collection errors. We don't think this would exhibit much sampling bias the players we failed to collect did not have something in common in terms of their performance stats, in other words, we did not collect certain players at random.

***Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)***
    - The players we chose to collect are players who compete in LCS, the top level of professional League of Legends in the United States and Canada. Different regions have different play styles so our analysis may only pertain to the North American region.

### Is our data enough to answer: "Does a professional player’s KDA and WL ratio in non-professional play predict how he/she will perform in professional play?"  ###

We currently have the data we need to answer the above, but only for a limited sample size. We have the match history (with respective stats) and the performance stats for the last LCS season (LCS Spring 2021) for most LCS players. We have the ability to get the last 100 matches for a player (though we are only collecting the last 40 matches because it takes a long time to collect the match history for each player). We currently only have the match history for one soloqueue account for each professional player (most players have multiple soloqueue accounts). To improve our analysis, we have to include the stats for all accounts associated with a player (or at least their most used soloqueue account).

In addition, some soloqueue accounts for certain players have no ranked game history for the current session further decreasing the amount of data points. We plan to remedy this by collecting the match history from a previous season, but we have yet to figure out how to do so. Furthermore, the Gamepedia wiki has not updated the regions associated with certain soloqueue IDs so looking up the IDs on the Riot API causes errors as IDs are treated differently based on the region they belong to. As such, we currently throw away data for players that have recently changed the region associated with their soloqueue ID.

#### Challenges and Observations ####

After doing our data collection, we have reduced the scope of our initial  idea. Originally we wanted to get the match history for a player before they were professionals to see if their past soloqueue performance was a good predictor for their competative careers. We believe the original idea is unfeasable as pros play thousands of games and many current pros have been pros for a long time, so finding data so far in the past would be very difficult.

We believe analyzing the performance of pros outside of competative play to predict their performance in LCS tournaments is an equally interesting project and is feasible with the data we have available. 


We ***highly encourage you to use markdown syntax to organize and clean your reports*** since it will make it a lot more comprehenisble for the TA grading your project.