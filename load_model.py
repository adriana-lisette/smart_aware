import pickle 
import numpy as np

def createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays):
    
        loadedModel = pickle.load(open('model.pkl', 'rb'))
        x_predict = np.array([gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays])
        x_predict = x_predict.reshape(1, -1)

        return loadedModel.predict(x_predict)