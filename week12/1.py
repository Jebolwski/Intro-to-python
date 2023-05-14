from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestClassifier

fighters = pd.read_csv("fighters.csv")

modelL = LinearRegression()
modelM = MLPRegressor()
modelR = RandomForestClassifier()


x = fighters.iloc[:,[1,2]]
y = fighters.iloc[:,[1,2]]


xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=1)

modelR.fit(xtrain, ytrain)
modelL.fit(xtrain, ytrain)
modelM.fit(xtrain, ytrain)

print(modelL.score(xtest,ytest))