from flask import Flask, request, render_template
import model

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

    prediction = model.createPrediction(gender, gradeID, raisedHands, semester, visitedResources, announcementsView, discussion, parentParticipating, absenceDays)
    if prediction == 0:
        prediction_text = "Your student shows low achievement"
    elif prediction == 1:
        prediction_text = "Your student shows high achievement"
    
    return render_template("prediction.html", prediction_text = prediction_text)

if __name__ == "__main__": 
    app.run()
