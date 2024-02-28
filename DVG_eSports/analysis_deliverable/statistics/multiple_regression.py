import numpy as np
import pandas as pd
import random
import statsmodels.api as sm
import matplotlib.pyplot as plt

from statsmodels.tools import eval_measures
import seaborn as sns

from util import load_file, load_file1, calculate_r_squared, split_data_randomly, train_test_split

def multiple_regression(X_test, X_train, y_test, y_train):
    """
    A multiple linear regression using StatsModel
    Inputs:
    - X_train, X_test, y_train, y_test: lists of training and testing values

    Outputs:
    - The Mean Squared Error value when applying the model on the training
    dataset (training_MSE)
    - The Mean Squared Error value when applying the model on the testing
    dataset (testing_MSE)
    - The R-Squared value when applying the model on the *training* dataset
    (training_R2)
    """
    # Placeholder - your function should update these three variables and
    # return the correct values for these three variables!
    training_MSE, testing_MSE, testing_R2 = 0, 0, 0

    # TODO: Use StatsModels to create the Linear Model and Output R-squared
    X_train = sm.add_constant(X_train)
    X_test = sm.add_constant(X_test)
    model = sm.OLS(y_train, X_train)

    # TODO: Prints out the Report
    results = model.fit()
    print(results.summary())

    # TODO: print R-squared, test MSE & train MSE
    y_prediction = results.predict(X_train) # for calculating train MSE
    y_prediction_test = results.predict(X_test)
    training_MSE = eval_measures.mse(y_prediction, y_train, axis=0)
    testing_MSE = eval_measures.mse(y_prediction_test, y_test, axis=0)
    testing_R2 = calculate_r_squared(y_test, y_prediction_test)

    print("Training MSE: ", str(training_MSE))
    print("Testing MSE: ", str(testing_MSE))
    print("Testing R-Squared: ", str(testing_R2))
    # return
    return training_MSE, testing_MSE, testing_R2



if __name__=='__main__':

    # DO not change this seed. It guarantees that all students perform the same
    # train and test split
    random.seed(1)
    matches = {}
    outcome = {}
    kills = {}
    deaths = {}
    assists = {}
    proNameSet = set()

    # TODO: Call load_file; x_var should be a list
    proNameSet, matches, outcome, kills, deaths, assists = load_file()
    winrate = {}
    tier = {}
    winrate, tier = load_file1()

    # x should be kills, deaths, assists, outcome
    # y should be winrate

    x_data = []
    y_data = []
    orderedName = []
    for name in proNameSet:
        temp = []
        orderedName.append(name)
        temp.append(kills[name])
        temp.append(deaths[name])
        temp.append(assists[name])
        temp.append(outcome[name])
        temp.append(tier[name])
        x_data.append(temp)
    for name in orderedName:
        y_data.append(winrate[name])
        
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)




#Simple regression part
    simp_outcome = []
    simp_kills = []
    simp_deaths = []
    simp_assists = []
    simp_tier = []

for name in proNameSet:
    simp_kills.append(kills[name])
    simp_deaths.append(deaths[name])
    simp_assists.append(assists[name])
    simp_outcome.append(outcome[name])
    simp_tier.append(tier[name])

data = pd.DataFrame(x_data, columns = ["Kills", "Deaths", "Assists", "Outcome", "Tier"])
data['Winrate'] = y_data

print("kills")
model2 = sm.OLS(y_data, simp_kills).fit()
predictions = model2.predict(simp_kills)
print(model2.summary())

print("deaths")
model3 = sm.OLS(y_data, simp_deaths).fit()
predictions = model3.predict(simp_deaths)
print(model3.summary())

print("assists")
model4 = sm.OLS(y_data, simp_assists).fit()
predictions = model4.predict(simp_assists)
print(model4.summary())

print("winrate")
model5 = sm.OLS(y_data, simp_outcome).fit()
predictions = model5.predict(simp_outcome)
print(model5.summary())

print("tier")
model6 = sm.OLS(y_data, simp_tier).fit()
predictions = model6.predict(simp_tier)
print(model6.summary())

#Creates a scatterpoint graph of ___ (tier)
model_graph = sm.OLS(data['Winrate'], sm.add_constant(data['Tier'])).fit()

p = model_graph.params
print(model_graph.summary())
p
x = np.arange(0,15)


ax = data.plot(kind='scatter', x="Tier", y="Winrate")
ax.plot(x, p.const + p.Tier * x)


#Seaborn
sns.lmplot(x='Tier', y='Winrate', data=data)
plt.show()

# TODO: Call multiple_regression
multiple_regression(x_test, x_train, y_test, y_train)

