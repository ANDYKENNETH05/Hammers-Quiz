from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return"<h1>new flask application<h1>"


if __name__ =='__main__':
    app.run(debug=True)