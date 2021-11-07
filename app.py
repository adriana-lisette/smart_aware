import json
from flask import Flask, request, render_template
import load_model

app = Flask(__name__)

@app.route("/")
def create_html():
    return render_template("index.html")

@app.route("/prediction", methods=['POST'])
def info():
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
 
    prediction = load_model.createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays)
    if prediction == 0:
        prediction_text = "Your student shows low achievement"
    elif prediction == 1:
        prediction_text = "Your student shows high achievement"
    
    return render_template("prediction.html", prediction_text = prediction_text)


@app.route("/smart_aware_app", methods=['POST'])
def data():
    data = request.json
    gender = data["gender"]
    gradeID = data["gradeID"]
    semester = data["semester"]
    raisedHands = data["raisedHands"]
    visitedResources = data["visitedResources"]
    announcementsView = data["announcementsView"]
    discussion = data["discussion"]
    parentParticipating = data["parentParticipating"]
    absenceDays = data["absenceDays"]

    prediction = load_model.createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays)
    predict_num = prediction[1]
    set_predict = {"predict":predict_num}
    json_predict = json.dumps(set_predict)
    return json_predict