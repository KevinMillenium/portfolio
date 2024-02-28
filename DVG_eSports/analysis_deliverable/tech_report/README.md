# Tech Report

# A defined hypothesis or prediction task, with clearly stated metrics for success. #

Is there a linear relationship between a player’s average kills, average deaths, and average assists in non-professional play and win rate in professional play? If at least one of these statistics fits the model well (measured by R-Squared), that will be a success.

# Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? How did you measure success or failure? Why that metric/value? What challenges did you face evaluating the model? Did you have to clean or restructure your data? #

We used both simple regressions for each statistic and also a multiple regression for all statistics. We used regressions because we wanted to figure out what the most important statistics that affect win rate are across all players. As players ourselves, we know that there are different types of successful players (e.g., players that focus on more kills, players that focus on less deaths, and players that focus on more assists) and we wanted to see if these statistics matter and if they do, how much they matter. We considered doing hypothesis testing but that didn’t make as much sense as a prediction because we’re trying to predict if a statistic affects win rate and not test statements about a population. We could have, but we figured prediction with linear regression made the most sense and is the popular test for a scenario like this.

We are measuring success and failure by R-Squared, the popular way for measuring the strength of a linear relationship between a dependent and independent variable; it determines how well a model fits the data. If no statistics have a significant linear relationship (high R-Squared), we’d call it a failure. If at least one has a significant linear relationship, we’d call it a success. There wasn’t really a challenge in evaluating the model because the models were pretty straightforward; the difficulty was in making and visualizing the model.

We did have to clean and restructure our data throughout our analysis. For example, because we used different websites for different statistics (e.g., non-professional and professional), we had to change variables so we could query them on their respective APIs. There was also just general housekeeping (e.g., accounting for players switching regions) to get our clean, restructured .db file. 

# What is your interpretation of the results? Do accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results? #
 
Interpretation of results: None of the factors are significant. Deny the hypothesis.

Why you got the accuracy/success metric you have: The high p-values in all of the constants are due to the constants not being significant enough to prove they have an effect on professional play win rate. 

How do you react to the results: Not surprising, there are much many factors that can affect a person’s performance on the professional stage that can’t be attributed to games played in a non-professional setting.

Are you confident in the results: No, there has to be more cleaning done since the matches taken include “fun” matches where the pro player doesn’t worry about performance (URF/ARAM).

The simple regression R-Squared value for average kills is .753. The multiple regression p-value is .978 .

The simple regression R-Squared value for average deaths is .850. The multiple regression p-value is .180.

The simple regression R-Squared value for average assists is .808. The multiple regression p-value is .473.

The simple regression R-Squared value for tier is .707. The multiple regression p-value is 0.880.

The simple regression R-Squared value for win rate is .787. The multiple regression p-value is .320.


# For your visualization, why did you pick this graph? What alternative ways might you communicate the result? Were there any challenges visualizing the results, if so, what where they? Will your visualization require text to provide context or is it standalone (either is fine, but it's recognize which type your visualization is)? #

We picked a scatter plot with a line of best fit because it’s the graph used for regression. Each point on the scatter plot is an individual player’s statistic and winrate. The line of best fit for all the points is the line that best expresses the relationship between the statistic and win rate across all the players. The line visualizes the marginal increase or decrease in win rate from a marginal increase in a statistic. We also picked a pie chart to visualize our multiple regression results. Each slice of the pie would represent how much a statistic out of all the statistics affects win rate. I don’t think there would have been good alternative ways to visualize the simple regression results. We could have visualized the multiple regression with a 3D model but that was beyond the scope of our abilities. There are alternatives to a pie chart such as a bar chart but we figured the pie chart made the most sense because we are representing parts of a whole. There were no challenges beyond debugging in visualizing the results. I don’t think our visualization requires text but it will certainly be helpful to label the axes and slices.
 
# Full results + graphs (at least 1 stats/ml test and at least 1 visualization). Depending on your model/test/project we would ideally like you to show us your full process so we can evaluate how you conducted the test! #

Please see the repository.

# If you did a statistics test, are there any confounding trends or variables you might be observing? #

Kills, deaths, assists all influence each other. Players with high kills most likely have low deaths, and high assists. Team statistics (because these are professional players) also influence win rate because a player can play good or bad but if the team is bad they’ll lose and if the team is good they’ll win. Role is also an important confounding variable because not all players in our data play the same role. For example, the ADC role typically gets more kills and support roles typically get more assists. We originally were also going to consider ELO and LP but didn’t because those are influenced by kills, deaths, assists, and win rate. We also were going to consider gold but didn’t because gold is affected by the duration of the game  more than a player’s performance.

# If you did a machine learning model, why did you choose this machine learning technique? Does your data have any sensitive/protected attributes that could affect your machine learning model? #

We didn’t use a machine learning model.

# Discussion of visualization/explaining your results on a poster and a discussion of future directions. #

We plan to make a simple poster with our prediction task at the top, our simple linear regression models, simple regression R-Squared values, and multiple regression p-values in the middle, and our interpretation of the results at the bottom. I think our project has been relatively straightforward and is a good starting point for the big potential data science can have on not just LoL, but all of Esports. Future directions include adding more statistics (in and out of game), experimenting with different combinations of statistics, scraping more players, and incorporating machine learning. There’s a lot that goes into the success of a player and how much they win.

