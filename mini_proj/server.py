from flask import Flask
from flask_cors import CORS, cross_origin
import psycopg2

conn = psycopg2.connect(dbname='trivia')

with conn: # commits automatically when completed
  with conn.cursor() as cur: # closes cursor when completed
    cur.execute("DROP TABLE IF EXISTS question")
    cur.execute("CREATE TABLE question (id SERIAL PRIMARY KEY, title VARCHAR);")

    # add questions here
    cur.execute("INSERT INTO question (title) VALUES(%s)", ("What is my middle name?",))
    
    cur.execute("SELECT * FROM question")
    print(cur.fetchall())

conn.close()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/data")
@cross_origin()
def get_data():
  return {"facts": ['today is cloudy', 'I love my wife', 'I am tired']}

if __name__ == "__main__":
  app.run(debug=True, port=8080)
