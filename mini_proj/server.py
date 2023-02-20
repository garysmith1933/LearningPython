from flask import Flask

app = Flask(__name__)

@app.route("/data")
def get_data():
  return {"facts": ['today is cloudy', 'I love my wife', 'I am tired']}

if __name__ == "__main__":
  app.run(debug=True, port=8080)
