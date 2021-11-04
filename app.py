from flask import Flask, request, render_template
import pickle 


app = Flask(__name__)

@app.route("/")
def create_html():
    return render_template("index.html")

@app.route("/prediction", methods=['POST'])
def data():
    info = request.form
    gender = info["gender"]
    gradeID = info["gradeID"]
    semester = info["semester"]
    raisedHands = info["raisedHands"]
    visitedResources = info["visitedResources"]
    announcementsView = info["announcementsView"]
    discussion = info["discussion"]
    parentParticipating = info["parentParticipating"]
    absenceDays = info["absenceDays"]

    def createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays):
    
        loadedModel = pickle.load(open('model.pkl', 'rb'))
        x_predict = np.array([gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays])
        x_predict = x_predict.reshape(1, -1)

        return loadedModel.predict(x_predict) 

    prediction = createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays)
    if prediction == 0:
        prediction_text = "Your student shows low achievement"
    elif prediction == 1:
        prediction_text = "Your student shows high achievement"
    
    return render_template("prediction.html", prediction_text = prediction_text)


