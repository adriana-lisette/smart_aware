import json
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import load_model

app = Flask(__name__)
cors = CORS(app)

@app.route("/smart_aware_app", methods=['POST'])
@cross_origin()
def data():
    data = request.json
    gender = data["gender"]
    gradeID = data["gradeID"]
    raisedHands = data["raisedHands"]
    visitedResources = data["visitedResources"]
    announcementsView = data["announcementsView"]
    discussion = data["discussion"]
    parentParticipating = data["parentParticipating"]
    absenceDays = data["absenceDays"]

    prediction = load_model.createPrediction(gender, gradeID, raisedHands, visitedResources, announcementsView, discussion, parentParticipating, absenceDays)
    predict_num = prediction[1]
    set_predict = {"predict":predict_num}
    json_predict = json.dumps(set_predict)
    return json_predict