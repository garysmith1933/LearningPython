import psycopg2

def seed():
  conn = psycopg2.connect(dbname='trivia')

  with conn: # commits automatically when completed
    with conn.cursor() as cur: # closes cursor when completed
      cur.execute("DROP TABLE IF EXISTS question")
      cur.execute("CREATE TABLE question (id SERIAL PRIMARY KEY, title VARCHAR);")

      questions = ['What is my middle name?', 'How old am i?', 'What year did I get married?', 'What is my favorite food?', 'What is my favorite anime?']

      for question in questions:
        cur.execute("INSERT INTO question (title) VALUES(%s)", (question,))

      cur.execute("SELECT * FROM question")
      print(cur.fetchall())
      print('seeded')
  conn.close()