from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route("/data")
def get_data():
  return {"facts": ['today is cloudy', 'I love my wife', 'I am tired']}

if __name__ == "__main__":
  app.run(debug=True, port=8080)
