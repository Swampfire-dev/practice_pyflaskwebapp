from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello All, this is python flask web application setup. If you reading this.You are on right track.Good Night"

if __name__== '__main__':
    app.run(host='0.0.0.0')

