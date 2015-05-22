from flask import Flask
app = Flask(__name__)

@app.route("/highscore")
def hello():
    with open('highscore.txt','r') as f:
      return f.read()

@app.route('/update?highscore=<int:score>')
def show_post(score):
  with open('highscore.txt','w') as f:
      f.write(score)

if __name__ == "__main__":
    app.run()