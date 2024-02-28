import random
import pandas as pd
import sqlite3

def load_file():
    """
    input:
        file_path: the path to the data file
        x_var:
            - for simple linear regression: the name of the independent variable
            - for multiple linear regression: a list of the names of the independent
            variables
            NOTE: to access a column in a pandas dataframe (df), you do
                    df['column_name'].values;
                to access multiple columns, you need df[['column_name1',
                    'column_name2', ..., ]]

    output:
        X: python list of independent variables values
        y: python list of the dependent variable
            values (i.e. 'cnt')
    """
    # TODO: Use pandas to load data from the file
    proNameMatches = {}
    proNameOutcome = {}
    proNameKills = {}
    proNameDeaths = {}
    proNameAssists = {}
    S = set()
    connection = sqlite3.connect("/Users/Kev/cs1951/DVG_eSports_final_project/analysis_deliverable/statistics/finaldata1.db")
    #connection = sqlite3.connect("/Users/grass/Desktop/cs1951a/DVG_eSports_final_project/analysis_deliverable/tech_report/finaldata.db")
    cursor = connection.cursor()
    cursor.execute("SELECT matches.soloqueueName, matches.outcome, matches.kills, matches.deaths, matches.assists, matches.queueType FROM matches WHERE queueType IS 420;")
    results = cursor.fetchall()
    for r in results:
        if r[5] == 420: 
            if r[0] in S:
                proNameMatches[r[0]] += 1
                proNameKills[r[0]] += r[2]
                proNameDeaths[r[0]] += r[3]
                proNameAssists[r[0]] += r[4]
                if (r[1] == 'Win'):
                    proNameOutcome[r[0]] += 1
            else:
                S.add(r[0])
                proNameMatches[r[0]] = 1
                proNameKills[r[0]] = r[2]
                proNameDeaths[r[0]] = r[3]
                proNameAssists[r[0]] = r[4]
                if (r[1] == 'Win'):
                    proNameOutcome[r[0]] = 1
                else:
                    proNameOutcome[r[0]] = 0
    for name in S:
        proNameOutcome[name] /= proNameMatches[name]
        proNameKills[name] /= proNameMatches[name]
        proNameDeaths[name] /= proNameMatches[name]
        proNameAssists[name] /= proNameMatches[name]
    cursor.close()
    connection.close()
    return S, proNameMatches, proNameOutcome, proNameKills, proNameDeaths, proNameAssists

def load_file1():
    """
    input:
        file_path: the path to the data file
        x_var:
            - for simple linear regression: the name of the independent variable
            - for multiple linear regression: a list of the names of the independent
            variables
            NOTE: to access a column in a pandas dataframe (df), you do
                    df['column_name'].values;
                to access multiple columns, you need df[['column_name1',
                    'column_name2', ..., ]]

    output:
        X: python list of independent variables values
        y: python list of the dependent variable
            values (i.e. 'cnt')
    """
    # TODO: Use pandas to load data from the file
    proNameWinRate = {}
    proNameTier = {}

    connection = sqlite3.connect("finaldata1.db")
    cursor = connection.cursor()
    cursor.execute("SELECT players.soloQueueName, players.winrate, players.tier, players.rank, players.LP FROM players;")
    results = cursor.fetchall()
    for r in results:
        if r[0] != 'Not Available':
            proNameWinRate[r[0]] = r[1]
            proNameTier[r[0]] = 0
            if r[2] == 'PLATINUM':
                proNameTier[r[0]] = 0
                if r[3] == 'I':
                    proNameTier[r[0]] += 300
                if r[3] == 'II':
                    proNameTier[r[0]] += 200
                if r[3] == 'III':
                    proNameTier[r[0]] += 100
            if r[2] == 'DIAMOND':
                proNameTier[r[0]] = 400
                if r[3] == 'I':
                    proNameTier[r[0]] += 300
                if r[3] == 'II':
                    proNameTier[r[0]] += 200
                if r[3] == 'III':
                    proNameTier[r[0]] += 100
            if r[2] == 'MASTER':
                proNameTier[r[0]] = 800
            if r[2] == 'GRANDMASTER':
                proNameTier[r[0]] = 800
            if r[2] == 'CHALLENGER':
                proNameTier[r[0]] = 800
            proNameTier[r[0]] += r[4]

    cursor.close()
    connection.close()
    return proNameWinRate, proNameTier

def calculate_r_squared(y_test, y_predicted):
    """
    Calculate the r-squared value

    Note: use the funciont R-Squared = 1 - SSE/SSTO

    input:
        y_test (list): the actual y values
        y_predicted (list): the predicted y values from the model

    output:
        r-squared (float)
    """

    r_squared_value = 0.0 # placeholder
    mean = 0
    n = len(y_test)
    sse = 0.0
    ssto = 0.0
    for y in y_test:
        mean += y
    mean /= n
    for i in range(n):
        sse += (y_test[i] - y_predicted[i]) * (y_test[i] - y_predicted[i])
        ssto += (y_test[i] - mean) * (y_test[i] - mean)
    r_squared_value = 1 - (sse/ssto)
    return r_squared_value


def split_data_randomly(data, prob):
    """
    input:
    - data: a list of pairs of x,y values
    - prob: the fraction of the dataset that will be testing data, typically
    prob=0.2

    output:
    - a tuple of two lists with training data pairs and testing data pairs,
    respectively.
    """
    # placeholders - do not change this. first list: training data,
    # second list: testing data
    results = [], []
    # TODO: Split data randomly into fractions [prob, 1 - prob]. populate the lists
    # in the tuple
    training = int((len(data) * (1- prob)))
    random.shuffle(data)
    for i in range(0, training):
        results[0].append(data[i])
    for j in range(training,len(data)):
        results[1].append(data[j]) 
    # return - you should not change this
    return results

    
def train_test_split(x, y, test_pct=0.2):
    """
    input:
        x: list of x values
        y: list of independent values
        test_pct: percentage of the data that is testing data (0.2 by default).

    output: x_train, x_test, y_train, y_test lists
    """
    # placeholders
    x_train, x_test, y_train, y_test = [], [], [], []
    # TODO: Split the features X and the labels y into x_train, x_test and
    # y_train, y_test as specified by test_pct. You may want to use split_data_randomly
    # in this function
    zipped = zip(x,y)
    
    full = split_data_randomly(list(zipped), test_pct)
    for row in full[0]:
        x_train.append(row[0])
        y_train.append(row[1])
    for row in full[1]:
        x_test.append(row[0])
        y_test.append(row[1])
    # and then return :)
    return x_train, x_test, y_train, y_test