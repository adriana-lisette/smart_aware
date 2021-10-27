import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays):
    dataset = pd.read_csv('rendimiento - copia3.csv')
    
    #Create x and y
    
    x = dataset.iloc[:, [0,1,2,3,4,5,6,7,8]].values
    y = dataset.iloc[:, 9].values
    
    model = DecisionTreeClassifier(criterion = 'entropy')
    model.fit(x,y)
    
    x_predict = np.array([gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays])
    x_predict = x_predict.reshape(1, -1)
    
    return model.predict(x_predict)