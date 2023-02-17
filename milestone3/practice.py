from flask import Flask, render_template
import requests
import json

# python equivalent of express
app = Flask(__name__)

def get_activities():
  activities = ()
  url = "https://www.boredapi.com/api/activity"
 
  idx = 1
  while idx <= 3:
    res = json.loads(requests.request("GET", url).text)
    activities = (*activities, res["activity"])
    idx += 1

  print(activities)
  return activities

@app.route("/")
def index():
  activities = get_activities()
  print(activities)
  res1, res2, res3 = activities
  #renders the data to the html page, and variables that get passed down as props
  return render_template("index.html", activity1= res1, activity2=res2, activity3=res3)


app.run(host="0.0.0.0", port=8080)